import pymongo
from urllib import parse


def get_google_scholar_links():
    mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    mied_db = mongoClient["iitr_mied"]
    faculty_gs_col = mied_db["faculty_iitr_web"]
    links = []
    for x in faculty_gs_col.find():
        if x['Google Scholar ID'] != '':
            link = 'https://scholar.google.co.in/citations?' + \
                parse.urlencode({'user': x['Google Scholar ID'], 'hl': 'en'})
            links.append(link)
    return links
