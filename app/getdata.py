import usr_list
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def pat1(text):
    result = re.search(r'(.*?)>', text)
    if result:
        extracted_data = result.group(1)
    return extracted_data

def check_pattern_in_string(pattern, text):
    if re.match(pattern, text) != None:
        return True
    else:
        return False
    
def ptr(a,pat):
    fl = [item for item in a if not pat.search(item)]
    return fl

def remove_numbers_from_start(text):
    index = 0
    while index < len(text) and text[index].isdigit():
        index += 1
    return text[index+1:]


#main
data_dict={}
driver = webdriver.Chrome()
c=0
for i in range(0,len(usr_list.custom_list)):
    driver = webdriver.Chrome()
    user=usr_list.custom_list[i]
    url=f"https://myanimelist.net/animelist/{usr_list.custom_list[i]}"
    driver.get(url)
    time.sleep(1)
    try:
        nns = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/table")
        data = nns.text.split("\n")
        strings_to_remove = ["#", "Add - More", "ufotable", "TV", "OVA", "Movie","TV Special","Special", "airing", "completed", "dropped", "plan to watch", "childhood nostalgia", "classic", "favorite", "recommended", "ongoing", "rewatch", "must watch", "hidden gem", "hype", "masterpiece", "personal favorite"]
        data = [item for item in data if item not in strings_to_remove]
        pattern = re.compile(r'^\d{2}-\d{2}-\d{2}')
        data = [item for item in data if not pattern.match(item)]
        driver.close()
        i=2
        res = []
        #print(data)
        pattern = r'^(-|\d+) / \d+$'
        for i in range(len(data)):
            if check_pattern_in_string(pattern,data[i]):
                res.append(data[i-2])
                res.append(data[i-1])
                res.append(data[i])
                #print(data[i])
        data = res
        time.sleep(1)
        c+=1
    except NoSuchElementException:
        #this is all good apply dictionary
        try:
            nns = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/table")
        except NoSuchElementException:
            try:
                nns = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/table")
            except:
                #check if user has a private list
                try:
                    badnews=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div")
                    if badnews.text == "Access to this list has been restricted by the owner.":
                        continue
                except NoSuchElementException:
                    try:
                        nns = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/table")
                    except NoSuchElementException:
                        continue
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
        i=0
        while i<=len(data)-2:
            data[i]=remove_numbers_from_start(data[i])
            i=i+3
        #print(data)
        c+=1
    finally:
        groups_of_3 = [data[i:i+3] for i in range(0, len(data), 3)]
        data=groups_of_3
        data_dict[user] = data
#add some limit here and run to avoid captcha
        if c==0:
            break
print(data_dict)
