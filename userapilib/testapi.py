import requests,re
from bs4 import BeautifulSoup as S
from fake_useragent import UserAgent
user_agent = UserAgent()
random_user_agent = user_agent.random
# print(user_agent)
# headers = {'User-Agent': random_user_agent,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate, br','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','TE': 'trailers',}

# response = requests.get('https://fragment.com/username/cool', headers=headers)

# soup = S(response.content, 'html.parser')
# istaken = soup.find("og:description")
# ok = soup.find("meta", property="og:description").get("content")
# if "is taken" in ok:print("taken")
# elif "An auction to get the Telegram" in ok:print("An auction")
# elif "Find active auctions for Telegram usernames." in ok:print("unavailable")
# elif "Check the current availability of" in ok:print("sold")
# elif "Get the username" in ok:print("available")
# else:print("error")


# a = requests.get("https://nft.fragment.com/username/okay").ok
# print(a)


headers = {'User-Agent': random_user_agent,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate, br','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','TE': 'trailers',
}

response = requests.get('https://fragment.com/username/sydb', headers=headers)

soup = S(response.content, 'html.parser')
username = soup.find("span",attrs={'class':'subdomain'})
domain = soup.find("span",attrs={'class':'domain'})
status = soup.find('span',attrs={'class':'tm-section-header-status tm-status-avail'})

bidList = soup.findAll('div',attrs={'class':'table-cell-value tm-value icon-before icon-ton'})
Highest_Bid_ton = bidList[0].string
Bid_Step_ton = bidList[1].string
Minimum_Bid = bidList[4].string
spen = soup.find_all("span")
Time_day = re.findall('data-val="(.*?)">',str(spen[16]))
b = re.findall('data-val="(.*?)">',str(spen[17]))
c = re.findall('data-val="(.*?)">',str(spen[18]))
d = re.findall('data-val="(.*?)">',str(spen[19]))
print ('- Ends in {} : {}{} : {}{} : {}{}'.format(Time_day[0],b[0],b[1],c[0],c[1],d[0],d[1]))
#Bid_Step_dolar = soup.find('div',attrs={'class':'table-cell-desc'}).string
tbody = (soup.find_all('div',attrs={'table-cell'}))
#print(tbody[3:])

results = []
BinList = (soup.find_all('div',attrs={'class':'table-cell-value tm-value icon-before icon-ton'}))
timelist = (soup.find_all('time',attrs={'class':'short'}))
linklist = (soup.find_all('a',attrs={'class':'tm-wallet'}))
url = re.findall("href=\"(.*?)\"", str(linklist))
print(BinList)
binArray = []
timeArray = []
urlArray = []
hashArray = []
for i in BinList[3:]:
    print(i.string)
    binArray.append(i.string)
print(binArray)
for i in timelist:
    print(i.string)
    timeArray.append(i.string)
for i in url:
    print(i)
    urlArray.append(i)
for i in url:
    hashArray.append(i.replace('https://tonviewer.com/',''))

print(binArray)
print(timeArray)
print(urlArray)
print(hashArray)
# print(BinList)
# print(timelist)
# print(url)

data = {
    'bidHistory':{
                            'binArray':hashArray,
                            'historyArray':timeArray,
                            'urlArray':urlArray,
}}
print(data)


# # # table-cell-value tm-value icon-before icon-ton







# array = [<div class="table-cell">
#     <div class="table-cell-value tm-value icon-before icon-ton">5,303</div>
#     <div class="table-cell-desc"> ~ $7,318</div>
#     </div>, <div class="table-cell">
#     <div class="table-cell-value tm-value icon-before icon-ton">266</div>
#     <div class="table-cell-desc"> 5%</div>
#     </div>, <div class="table-cell">
#     <div class="table-cell-value tm-value icon-before icon-ton">5,569</div>
#     <div class="table-cell-desc"> ~ $7,685</div>
#     </div>, <div class="table-cell">
#     <div class="table-cell-value tm-value icon-before icon-ton">5,303</div>
#     </div>, <div class="table-cell">
#     <div class="tm-datetime"><span class="thin-only"><time class="short" datetime="2023-06-20T11:49:30+00:00">Jun 20 at 11:49</time></span><span class="wide-only"><time datetime="2023-06-20T11:49:30+00:00">20 Jun 2023 at 11:49</time></span></div>
#     </div>, <div class="table-cell">
#     <a class="tm-wallet" href="https://tonviewer.com/EQC7b3Tt0f-XtJnz2gJrgloLStlALO-w7YLpT0f2WK3Mnghu" target="_blank"><span class="head">EQC7b3Tt0f-XtJnz2gJrgloL</span><span class="middle"></span><span class="tail">StlALO-w7YLpT0f2WK3Mnghu</span></a>
#     </div>, <div class="table-cell">
#     <div class="table-cell-value tm-value icon-before icon-ton">5,050</div>
#     </div>, <div class="table-cell">
#     <div class="tm-datetime"><span class="thin-only"><time class="short" datetime="2023-06-19T18:08:28+00:00">Jun 19 at 18:08</time></span><span class="wide-only"><time datetime="2023-06-19T18:08:28+00:00">19 Jun 2023 at 18:08</time></span></div>
#     </div>, <div class="table-cell">
#     <a class="tm-wallet" href="https://tonviewer.com/EQDt5q0fGkSL4GFL6rDvHR0qnNTfM8Tt07jE3KC2zyx96wq8" target="_blank"><span class="head">EQDt5q0fGkSL4GFL6rDvHR0q</span><span class="middle"></span><span class="tail">nNTfM8Tt07jE3KC2zyx96wq8</span></a>
#     </div>]

# for n in array:
#     BinList = (soup.find_all('div',attrs={'class':'table-cell-value tm-value icon-before icon-ton'}))[n]
#     timelist = (soup.find('time',attrs={'class':'short'})).string
#     linklist = (soup.find('a',attrs={'class':'tm-wallet'})).strin
#     #d = re.findall('href="(.*?)">',str(linklist))
#     url = "".join(re.findall("href=\"(.*?)\"", str(linklist)))
#     print(BinList)
#     print(timelist)
#     print(url)
