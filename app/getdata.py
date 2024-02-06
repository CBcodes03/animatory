import usr_list
import time
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def pat1(text):
    result = re.search(r'(.*?)>', text)
    if result:
        extracted_data = result.group(1)
    return extracted_data

def ptr(a,pat):
    fl = [item for item in a if not pat.search(item)]
    return fl

testurl = "https://myanimelist.net/animelist/---DANIEL---"
driver = webdriver.Chrome()
c=0
for i in range(0,len(usr_list.custom_list)):
    driver = webdriver.Chrome()
    #res = remove_dash_padding(i)
    #print(res)
    print(usr_list.custom_list[i])
    url=f"https://myanimelist.net/animelist/{usr_list.custom_list[i]}"
    driver.get(url)
    time.sleep(3)
    try:
        nns = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/table")
        data = nns.text.split("\n")
        strings_to_remove = ["#", "Add - More", "ufotable", "TV", "OVA", "Movie","TV Special","Special", "-", "airing", "completed", "dropped", "plan to watch", "childhood nostalgia", "classic", "favorite", "recommended", "ongoing", "rewatch", "must watch", "hidden gem", "hype", "masterpiece", "personal favorite"]
        data = [item for item in data if item not in strings_to_remove]
        pattern = re.compile(r'^\d{2}-\d{2}-\d{2}')
        data = [item for item in data if not pattern.match(item)]
        print(data)
        driver.close()
        time.sleep(1)
        c+=1
    except NoSuchElementException:
        nns = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/table")
        data = nns.text.split("\n")
        data = data[1:]
        pat1 = re.compile(r'\b(?:Winter|Spring|Summer|Fall)\s+\d{4}\b')
        pat3 = re.compile(r'.*\b\d{2}-\d{2}-\d{2}\s+\d{2}-\d{2}-\d{2}\b$')
        data = [pat3.sub('', item) for item in data]
        data = [item for item in data if item != "Add - More" and item !='']
        data = ptr(data,pat1)
        data = ptr(data,pat3)
        rs=["TV","OVA","Movie","TV Special","Special"]
        for j in data:
            for i in rs:
                if i in j:
                    data[(data.index(j))]=j[0:(len(j)-len(i)-1)]
                    break
        print(data)
        c+=1
    finally:
        if c==2:
            break