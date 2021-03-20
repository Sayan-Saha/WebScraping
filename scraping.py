import requests
import json
from bs4 import BeautifulSoup

#main home page of Advocate Khoj from where we will collect all data of IPC 1860
page = requests.get("https://www.advocatekhoj.com/library/bareacts/indianpenalcode/index.php?Title=Indian%20Penal%20Code,%201860")

soup = BeautifulSoup(page.content, 'html.parser')
#collecting all the anchor tags
anchor_tags = soup.find_all('a')
#List of extracted law object that will contain all the subsections with Type, Title and ActDescription
Detailed_law_obj_list = []
Detailed_law_obj_keys = ["Type","Title","ActDescription"]

#looping thru all the valid urls
for anchor in anchor_tags[3:-12]:
    #url for the subsections
    url = "https://www.advocatekhoj.com/library/bareacts/indianpenalcode/" + anchor['href']
    new_page = requests.get(url)
    new_soup = BeautifulSoup(new_page.content, 'html.parser')
    #fetching all paragraphs
    para_tags = new_soup.find_all('p')
    #temporary list to store the para contents
    temp_list = []
    for para in para_tags:
        #storing para content in temp_list
        temp_list.append(para.get_text())
    
    print(temp_list)
    try:
        #Detailed law object dictionary
        Detailed_law_obj = {}

        for i in range(temp_list):
            Detailed_law_obj[Detailed_law_obj_keys[i]] = temp_list[i]
        Detailed_law_obj_list.append(Detailed_law_obj)
        #print(Detailed_law_obj["Title"])
    except:
        break

#dump all the collected data
#with open("extractedData.json", "w") as file:
    #json.dump(Detailed_law_obj_list, file)