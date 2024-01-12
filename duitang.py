from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup


ua = UserAgent()




url = 'https://www.duitang.com/category/?cat=animation'
headers = {'User-Agent': ua.random}


response = requests.get(url, headers=headers)

mysoup = BeautifulSoup(response.text, 'lxml')




for i in range(30):
    print(mysoup.find_all(attrs={'alt':'动漫'})[i].attrs['src'])
    imgurl = mysoup.find_all(attrs={'alt':'动漫'})[i].attrs['src']
    imgresponse = requests.get(imgurl)
    with open('img'+str(i)+'.ico', 'wb') as f:
        f.write(imgresponse.content)


