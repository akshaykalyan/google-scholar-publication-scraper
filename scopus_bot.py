from bs4 import BeautifulSoup
import requests
# from fetch_gs_links import get_google_scholar_links
import urllib.parse
from requests.structures import CaseInsensitiveDict
import json

url = "https://www.scopus.com/api/documents/search"

headers = CaseInsensitiveDict()
headers["authority"] = "www.scopus.com"

headers["accept"] = "application/json"
headers["x-requested-with"] = "XMLHttpRequest"
headers["sec-ch-ua-mobile"] = "?0"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
headers["content-type"] = "application/json"
headers["origin"] = "https://www.scopus.com"
headers["sec-fetch-site"] = "same-origin"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-dest"] = "empty"
headers["referer"] = "https://www.scopus.com/authid/detail.uri?authorId=7006087147"
headers["accept-language"] = "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
headers["cookie"] = "scopus.machineID=B422FFA281B2776982E1809E3537BD8D.i-047ed26299e330b99; at_check=true; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; __cfruid=da1384acadf2868c2ffc497057412f4e6fea9dde-1628021501; SCSessionID=6043BA96B9C7B2E8B3582F38B2295BF9.i-0c457d55893bfb95f; scopusSessionUUID=415e549d-0ae5-4afb-a; AWSELB=CB9317D502BF07938DE10C841E762B7A33C19AADB172A9988624FD36958ABEF5B7F882DF887A69D29F6C219F8621C4D9D2E21468BDA934D92BA26A54E56FF7F9DDF53B01D7C2C702692CA9DFC30983FEF90DC59785; SCOPUS_JWT=eyJraWQiOiJjYTUwODRlNi03M2Y5LTQ0NTUtOWI3Zi1kMjk1M2VkMmRiYmMiLCJhbGciOiJSUzI1NiJ9.eyJhbmFseXRpY3NfaW5mbyI6eyJhY2Nlc3NUeXBlIjoiYWU6QU5PTjo6SU5TVDpJUCIsInVzZXJJZCI6ImFlOjExNDMzNzEiLCJhY2NvdW50SWQiOiI1MTc4MSIsImFjY291bnROYW1lIjoiSW5kaWFuIEluc3RpdHV0ZSBvZiBUZWNobm9sb2d5IFJvb3JrZWUifSwic3ViIjoiMTE0MzM3MSIsImluc3RfYWNjdF9uYW1lIjoiSW5kaWFuIEluc3RpdHV0ZSBvZiBUZWNobm9sb2d5IFJvb3JrZWUiLCJzdWJzY3JpYmVyIjp0cnVlLCJkZXBhcnRtZW50SWQiOiI3MzA5OCIsImlzcyI6IlNjb3B1cyIsImluc3RfYWNjdF9pZCI6IjUxNzgxIiwiaW5zdF9hc3NvY19tZXRob2QiOiJJUCIsInBhdGhfY2hvaWNlIjpmYWxzZSwiYXVkIjoiU2NvcHVzIiwibmJmIjoxNjI4MTY2NDM5LCJpbmR2X2lkZW50aXR5X21ldGhvZCI6IiIsImluc3RfYXNzb2MiOiJJTlNUIiwiaW5kdl9pZGVudGl0eSI6IkFOT04iLCJleHAiOjE2MjgxNjczMzgsImF1dGhfdG9rZW4iOiJhODQ4OWJhZTliNjFkODQ5NzM2YjQ5ZDgzYTA3ZjljNTQ1NjVneHJxYSIsImlhdCI6MTYyODE2NjQzOX0.BvuoMcDVtGF3jOHdwAD_I3NdiM8gGqmRlwbguG5qBqTDl3xO5_y8ixppJYryEs5gC-mGS_MDmVdPU2vk6lZ--CYk1iMz22BWitvscodYZo8o--qi1buQAMfoopwczaRKQS_uYbzMI3W1XTKKEptoUZsNfMRPtSA0HrKyPHZzHjOnB8SJ-FnDpX3nCkhdMQHz698alIVwaTZBlKyFB3sxici7d-4RtP7sfNDLcgIvFcdg1GS3T2M6iCfJgcZvGoxLnxHISRC04YCfGBBvsJnr-x1dLgtBraAuGdJjgMrZI9YA5ggoeBh04ueuzSneGif0-kooD-Nn5azShM1qcnmpHQ; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-1124106680%7CMCIDTS%7C18845%7CMCMID%7C10890182162656387364714450618470715954%7CMCAID%7CNONE%7CMCOPTOUT-1628173640s%7CNONE%7CvVersion%7C5.2.0; mbox=PC#1a3ef025c438498e97f0ad500cea92d6.31_0#1691411243|session#0a428561d132492cba04884c28951241#1628168301"

data = '{"authorid":"7006087147","sort":"plf-f","itemcount":100000,"offset":0}'


resp = requests.post(url, headers=headers, data=data)

if resp.status_code != 200:
    raise "Try changing cookie"
data = resp.json()
print(type(data))
