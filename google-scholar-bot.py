from bs4 import BeautifulSoup
import requests
# from fetch_gs_links import get_google_scholar_links
import urllib.parse

MAIN_URL = "https://scholar.google.co.in"
# links = get_google_scholar_links()

link = "https://scholar.google.co.in/citations?user=UKrBuMEAAAAJ&hl=en"

profile = {
    "Scholar Name": "",
    "Area of Intrest": "",
    "Publications Link": [],
    "Publications Data": []
}


def get_profile(link):
    pub_links_list = []
    start = True
    param = {
        "cstart": 0,
        "pagesize": 100
    }
    r = requests.get(link)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    print(soup)
    # Scholar Name
    profile["Scholar Name"] = soup.find(
        id="gsc_prf_in").text.strip()

    # aoi
    aoi_a = soup.find(id="gsc_prf_int").find_all('a')
    aoi = []
    for i in aoi_a:
        aoi.append(i.text.strip())
    profile["Area of Intrest"] = aoi

    while(start or len(pub_links_list) != 0):
        start = False

        r = requests.get(link, param)
        data = r.content
        soup = BeautifulSoup(data, 'html.parser')

        # Scholar Name
        profile["Scholar Name"] = soup.find(
            id="gsc_prf_in").text.strip()

        # aoi
        aoi_a = soup.find(id="gsc_prf_int").find_all('a')
        aoi = []
        for i in aoi_a:
            aoi.append(i.text.strip())
        profile["Area of Intrest"] = aoi

        # publications
        pub_t = soup.find(id="gsc_a_b").find_all(class_="gsc_a_t")
        pub_links_list = []
        for pub in pub_t:
            d = urllib.parse.urljoin(MAIN_URL, pub.a["href"].strip())
            pub_links_list.append(d)
            profile["Publications Link"].append(d)
        param["cstart"] += 100
    for link in profile['Publications Link']:
        try:
            profile["Publications Data"].append(extract_publication_data(link))
        except Exception as e:
            print("An exception occurred: ", e)
    f = open("demofile2.txt", "w")
    f.write(str(profile))
    f.close()


def extract_publication_data(link):
    pub_data = {
        "Title": "",
        "Link": ""
    }

    r = requests.get(link)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    title = soup.find("a", class_="gsc_oci_title_link")
    pub_data["Title"] = title.text.strip()
    pub_data["Link"] = title["href"]
    for x in soup.find(id="gsc_oci_table").find_all(class_="gs_scl"):
        key = x.find(class_="gsc_oci_field").text.strip()
        value = ""
        if key == 'Total citations':
            value = x.find(class_="gsc_oci_value").find("a").text.strip()
        else:
            value = x.find(class_="gsc_oci_value").text.strip()
        pub_data[key] = value
    return pub_data


get_profile(link)

# Test for all

# for link in links:
#     get_profile(link)
