from bs4 import BeautifulSoup
import requests
# from fetch_gs_links import get_google_scholar_links
import urllib.parse

MAIN_URL = "https://scholar.google.co.in"
# links = get_google_scholar_links()

link = "https://scholar.google.co.in/citations?user=UKrBuMEAAAAJ&hl=en"

profile = {
    "scholar_name": "",
    "aoi": "",
    "publications_link": []
}


def get_profile(link):
    pub_links_list = []
    start = True
    param = {
        "cstart": 0,
        "pagesize": 100
    }
    while(start or len(pub_links_list) != 0):
        start = False

        r = requests.get(link, param)
        data = r.content
        soup = BeautifulSoup(data, 'html.parser')

        # Scholar Name
        profile["scholar_name"] = soup.find(
            id="gsc_prf_in").text.strip()

        # aoi
        aoi_a = soup.find(id="gsc_prf_int").find_all('a')
        aoi = []
        for i in aoi_a:
            aoi.append(i.text.strip())
        profile["aoi"] = aoi

        # publications
        pub_t = soup.find(id="gsc_a_b").find_all(class_="gsc_a_t")
        pub_links_list = []
        for pub in pub_t:
            d = urllib.parse.urljoin(MAIN_URL, pub.a["href"].strip())
            pub_links_list.append(d)
            profile["publications_link"].append(d)
            print(d)
        print(len(pub_links_list))
        param["cstart"] += 100

    print(profile)


def extract_publication_data(link):
    link = "https://scholar.google.co.in/citations?view_op=view_citation&hl=en&oe=ASCII&user=UKrBuMEAAAAJ&citation_for_view=UKrBuMEAAAAJ:W7OEmFMy1HYC"
    r = requests.get(link)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')


# get_profile(link)

# Test for all

# for link in links:
#     get_profile(link)
