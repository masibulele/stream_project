import requests
from bs4 import BeautifulSoup


class StreamScraper:
    def __init__(self):
        self.url= 'https://store.steampowered.com/explore/new/'
        self.data = []
        self.response= self.connect_to_stream()


    def connect_to_stream(self):
        try:
            response=requests.get(self.url)
            return response
        except:
            print(response.status_code)


    def scrape_data(self):
        # get webpage
        soup= BeautifulSoup(self.response.text,'html.parser')
        #parse page
        new_release_doc= soup.find(id="tab_newreleases_content")
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

        for info in zip(titles,pictures,prices,plat_sep):
            resp= {}
            resp['title']= info[0]
            resp['image']= info[1]
            resp['price']= info[2]
            resp['themes']= info[3]
            self.data.append(resp)
        return self.data
    






if __name__ == '__main__':
    scraper= StreamScraper()
    data = scraper.scrape_data()
    print(data[0])

        



            





























