import requests
from bs4 import BeautifulSoup
import lxml

url= 'https://store.steampowered.com/explore/new/'

# get webpage
response= requests.get(url)
print(response.status_code)

#parse page
soup= BeautifulSoup(response.text,'html.parser')

new_release_doc= soup.find(id="tab_newreleases_content")
# print(new_release_doc.prettify())
#get game titles 
title_tags = new_release_doc.find_all(class_="tab_item_name")
titles= [ tag.get_text() for tag in title_tags]

#get picture link
pic_tags= new_release_doc.find_all(class_="tab_item_cap_img")
pictures= [pic['src'] for pic in pic_tags]


#get price

price_tags= new_release_doc.find_all(class_="discount_final_price")

prices= [price.get_text() for price in price_tags]


platform_tags= new_release_doc.find_all(class_="tab_item_top_tags")
platforms= [tag.get_text() for tag in platform_tags]
plat_sep = [tags.split(',')for tags in platforms]


data= []

for info in zip(titles,pictures,prices,plat_sep):
    resp= {}
    resp['title']= info[0]
    resp['image']= info[1]
    resp['price']= info[2]
    resp['platform']= info[3]
    

    data.append(resp)


print(data[0])




