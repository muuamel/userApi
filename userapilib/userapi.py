from .exception import *
from requests import get
from bs4 import BeautifulSoup as S
from fake_useragent import UserAgent
import re, requests
class check():
    def anime(self,user):
        """
        just i test the except method
        """
        try:
            self.username = user
            self.a = False
            if self.a == True:return True
            elif self.a == False:
                raise Exception("The MYUAMel")
        except requests.exceptions.ConnectionError:return 'Connection Error!'
   
    def Nft(self,user):
        """
        check if telgram username is NFT or not
        #Ex:
            #print(check.cNft(user))
            #Result If status == True: True
            #Result If status == False: False
        """
        try:
            self.username = user
            self.a = get(f"https://nft.fragment.com/username/{self.username}.webp")
            if self.a.ok == True:return True
            elif self.a.ok == False: return False
        except requests.exceptions.ConnectionError:raise Exception('Connection Error!')

    def Fragment(self,user, proxy=''): 
        """
        to checking username is on fragment.com or not
        
        #Ex without proxi :
        print(check.checkFragment(user))
        
        #Ex with proxi :
        print(check.checkFragment(user,proxy='123.123.123'))
        
        #Result: True - False
        """
        self.user_agent = UserAgent();self.random_user_agent = self.user_agent.random
        self.headers = {'User-Agent': self.random_user_agent,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate, br','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','TE': 'trailers',}
        self.username = user
        if not proxy: #check without proxis
            try:
                self.response = get(f'https://fragment.com/username/{self.username}', headers=self.headers)
                soup = S(self.response.content, 'html.parser')
                self.des = soup.find("og:description")
                self.ok = soup.find("meta", property="og:description").get("content")
                if "An auction to get the Telegram" in self.ok:return True
                elif "Telegram and secure your ownership " in self.ok:return True
                elif "Find active auctions for Telegram usernames." in self.ok:return False
                elif "Check the current availability of" in self.ok:return False
                else:return False
            except requests.exceptions.URLRequired: raise Exception('A valid URL is required to make a request!')
            except requests.exceptions.ConnectionError:raise Exception('Connection Error!')
            except: raise ErrorUnKnown()

        elif proxy: #check with proxis
            try:
                self.response = get(f'https://fragment.com/username/{self.username}', headers=self.headers,timeout=15,proxies={'http':f'http://{proxy}', 'https':f'http://{proxy}'})
                soup = S(self.response.content, 'html.parser')
                self.des = soup.find("og:description")
                self.ok = soup.find("meta", property="og:description").get("content")
                if "An auction to get the Telegram" in self.ok:return True
                elif "Telegram and secure your ownership " in self.ok:return True
                elif "Find active auctions for Telegram usernames." in self.ok:return False
                elif "Check the current availability of" in self.ok:return False
                else:return False
            except requests.exceptions.ProxyError: raise BadProxy(proxy)
            except requests.exceptions.ConnectionError: raise BadProxy(proxy)
            except requests.exceptions.ConnectTimeout: raise Exception('Timeout!')
            except requests.exceptions.SSLError: raise Exception('SSL Error!')
 
    def Telegram(self,user, proxy=''):

        """
        to checking username is on https://t.me/username or not
        
        #Ex without proxi :
        print(check.Telegram(user))
        
        #Ex with proxi :
        print(check.Telegram(user,proxy='123.123.123'))
        
        #Result: True - False
        
        """
        return 'soon in v0.2'

class info:
    def Nft(self,user):
        """
        :get username NFT information
        
        #Ex:
        print(check.NftInfo(user))
        
        #Result as JISON If status == True: {'name': 'muamel ameer','description':'this pkg by amo','image':fragment.amo.jpg,'ok':'True'}
        #Result as JISON If status == False: {'msg':'Error','ok': 'False'}
        
        
        """
        self.username = user
        try:
            self.req = get(f"https://nft.fragment.com/username/{self.username}")
            if self.req.ok == True:
                self.res = self.req.json()
                return {'name': self.res['name'],'description':self.res['description'],'image':self.res['image'],'ok':'True'}
                # def name(self):self.name = self.res['name']
                # def description(self):self.description = self.res['description']
                # def image(self):self.image = self.res['image']
            else:return {'msg':'Error','ok': 'False'}
        except requests.exceptions.URLRequired: return 'A valid URL is required to make a request!'
        except requests.exceptions.ConnectTimeout: return 'Timeout!'
        except requests.exceptions.ConnectionError:return 'Connection Error!'
        except:return {'msg':'Error','ok': 'False'}
    
    def auction(self,user): #get information user on auction like: price, time end, how the bid and bid history
        """
        THis Func For Get Information Any UserName On Auction in Fragment.com .
        Ex :
            print(info.auction(user))
        Result : ('''{dict}''')
        DataType The Result As Json .
        """
        self.user_agent = UserAgent();self.random_user_agent = self.user_agent.random
        self.headers = {'User-Agent': self.random_user_agent,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate, br','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','TE': 'trailers',}
        self.username = user
        try:
                self.response = get(f'https://fragment.com/username/{self.username}', headers=self.headers)
                self.test = check().Fragment(self.username)
                if self.test == True:
                    self.soup = S(self.response.content, 'html.parser')
                    self.username = self.soup.find("span",attrs={'class':'subdomain'}).string
                    self.domain = self.soup.find("span",attrs={'class':'domain'}).string
                    self.status = self.soup.find('span',attrs={'class':'tm-section-header-status tm-status-avail'}).string
                    self.bidList = self.soup.findAll('div',attrs={'class':'table-cell-value tm-value icon-before icon-ton'})
                    self.Highest_Bid_ton = self.bidList[0].string
                    self.Bid_Step = self.bidList[1].string
                    self.Minimum_Bid = self.bidList[2].string
                    self.spen = self.soup.find_all("span")
                    self.Days = re.findall('data-val="(.*?)">',str(self.spen[16]))[0]
                    self.b = re.findall('data-val="(.*?)">',str(self.spen[17]))
                    self.c = re.findall('data-val="(.*?)">',str(self.spen[18]))
                    self.d = re.findall('data-val="(.*?)">',str(self.spen[19]))
                    self.hours = f'{self.b[0]}{self.b[1]}'
                    self.minutes = f'{self.c[0]}{self.c[1]}'
                    self.seconds = f'{self.d[0]}{self.d[1]}'
                    self.tbody = (self.soup.find_all('div',attrs={'table-cell'}))
                    self.BinList = (self.soup.find_all('div',attrs={'class':'table-cell-value tm-value icon-before icon-ton'}))
                    self.timelist = (self.soup.find_all('time',attrs={'class':'short'}))
                    self.linklist = (self.soup.find_all('a',attrs={'class':'tm-wallet'}))
                    self.url = re.findall("href=\"(.*?)\"", str(self.linklist))
                    self.binArray = []
                    self.historyArray = []
                    self.urlArray = []
                    self.hashArray = []
                    for i in self.BinList[3:]:self.binArray.append(i.string)
                    for i in self.timelist:self.historyArray.append(i.string)
                    for i in self.url:self.urlArray.append(i)
                    for i in self.url:self.hashArray.append(i.replace('https://tonviewer.com/',''))
                    data = {
                            'ok':True,
                            'info':{
                                'username':self.username,
                                'domain':self.domain,
                                'status':self.status,
                                'price':{
                                    'Highest_Bid':self.Highest_Bid_ton,
                                    'Bid_Step':self.Bid_Step,
                                    'Minimum_Bid':self. Minimum_Bid,    
                                },
                                'dataTime':{
                                    'days':self.Days,
                                    'hours':self.hours,
                                    'minutes':self.minutes,
                                    'seconds':self.seconds
                                },
                                'bidHistory':{
                                    'binArray':self.binArray,
                                    'historyArray':self.historyArray,
                                    'urlArray':self.urlArray,
                                    'hashArray':self.hashArray
                                }
                            }
                        }
                    return data
                elif self.test == False:raise UserNotFound(self.username)
        except requests.exceptions.URLRequired: return 'A valid URL is required to make a request!'
        except AttributeError:return 'Try again!'

    
    def fragment(self,user, proxy=''): 
        """
        Check If UserName In Fragment.com or not with status like: is sold or on auction, act...
        Ex :
            print(info.auction(user))
        Result : ('''{dict}''')
        DataType The Result As Json .
        """
        self.user_agent = UserAgent();self.random_user_agent = self.user_agent.random
        self.headers = {'User-Agent': self.random_user_agent,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate, br','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','TE': 'trailers',}
        self.username = user
        if not proxy: #check without proxis
            try:
                self.response = get(f'https://fragment.com/username/{self.username}', headers=self.headers)
                soup = S(self.response.content, 'html.parser')
                self.des = soup.find("og:description")
                self.ok = soup.find("meta", property="og:description").get("content")
                if "is taken" in self.ok:return "Taken"
                elif "An auction to get the Telegram" in self.ok:return "OnAuction"
                elif "Find active auctions" in self.ok:return "UnAvailable"
                elif "Check the current availability of" in self.ok:return "Sold"
                elif "Get the username" in self.ok:return "Available"
                else:return "Error In Username"
            except requests.exceptions.URLRequired: return 'A valid URL is required to make a request!'

        elif proxy: #check with proxis
            try:
                self.response = get(f'https://fragment.com/username/{self.username}', headers=self.headers,timeout=15,proxies={'http':f'http://{proxy}', 'https':f'http://{proxy}'})
                soup = S(self.response.content, 'html.parser')
                self.des = soup.find("og:description")
                self.ok = soup.find("meta", property="og:description").get("content")
                if "is taken" in self.ok:return "Taken"
                elif "An auction to get the Telegram" in self.ok:return "OnAuction"
                elif "Find active auctions" in self.ok:return "UnAvailable"
                elif "Check the current availability of" in self.ok:return "Sold"
                elif "Get the username" in self.ok:return "Available"
                else:return "Error In Username"
            except requests.exceptions.ProxyError: raise BadProxy(proxy)
            except requests.exceptions.ConnectionError: raise BadProxy(proxy)
            except requests.exceptions.ConnectTimeout: raise Exception('Timeout!')
            except requests.exceptions.SSLError: raise Exception('SSL Error!')

class TelegramAcc:
    def login():pass
    
    def send(self,hash,Id,Message):
        return 'soon on v0.2'
    
    def SetUserName(self,hash,username):
        return 'soon on v0.2'

class TelegramBot:
    """
    Any Method From https://core.telegram.org/bots/api .
    """
    def ListMethods(self):
        """
        List Method .
        Ex : send : message - photo - vid
        """
