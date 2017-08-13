import random
import urllib.request
import requests
from bs4 import BeautifulSoup

searchTerm = input('Enter the search term: ')

search_url = "https://en.wikipedia.org/w/api.php?action=opensearch&search="+searchTerm+""

p = requests.get(search_url)

list=p.json()

main_url=list[3][0]

main_url_source_code = requests.get(main_url)


main_url_plain_text = main_url_source_code.text

# print(main_url_plain_text)

soup = BeautifulSoup(main_url_plain_text,"lxml")

image_list=[]

for link in soup.findAll('img',{'class':'thumbimage'}):

    image_list.append('https:'+link.get('src'))

# def dl_image(url,file_path , file_name):
#     full_path = file_path + file_name + '.jpg'
#     urllib.request.urlretrieve(url,full_path)



for i in range(len(image_list)):
    urllib.request.urlretrieve(image_list[i], "C:/Users/Dinesh Kumar Sah/Desktop/Python/Automatic-Image-downloader/downloaded images/"+str(random.randint(1,101))+".jpg")
