from bs4 import BeautifulSoup
import requests
import json
import re

#getting raw html of ce listing
course_page = requests.get("https://www.powerpak.com/courses/all")
#grabbing the json array in one of script tag and parse it as python list
soup = BeautifulSoup(course_page.text, "html.parser").find_all("script")[19]
data = soup.text
jsonString = "{\"result\" : [" + re.findall(r'let allActivities = \[(.*?)\];', data)[0] + "]}"
lst = json.loads(jsonString)["result"]
filteredlst = [ce for ce in lst if "Pharmacist" in ce["professions"] and ce["price"] == 0]

