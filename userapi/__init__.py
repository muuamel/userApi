
_version = 'v2.1'
_d = 'Muamel <3'

from bs4 import BeautifulSoup as S
import re , cloudscraper
from userapi.models import ok , info

class Fragment():
    """
    The `Fragment` class provides methods to interact with the Fragment platform,
    checking usernames, auctions, and NFT status.

    Attributes:
    - sender (cloudscraper.CloudScraper): HTTP client for making requests.
    """
    def __init__(self):
        self.headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
        self.f_api: str = "https://fragment.com/username/{}".format
        self.n_api: str = "https://nft.fragment.com/username/{}.webp".format
        self.sender: cloudscraper.create_scraper = cloudscraper.create_scraper()

### -

    def is_nft(self, username: "Username") -> ok:
        """
        Checks if a given username is associated with an NFT on Fragment.

        Args:
        - username (str): The username to check.

        Returns:
        - ok: An `ok` object indicating the NFT status of the username.
        """
        try:
            if self.sender.get(self.n_api(username)).ok == True:
                return ok(status=True, username=username, note='00: Is NFT',real_status='NFT')
            else:
                return ok(status=False, username=username, note='100: Not NFT')

        except Exception as e:
            raise Exception(f'An unknown error occurred: {e}') 

### - 

    def check_fragment(self, username) -> ok:
        """
    Checks the status of a username on the Fragment.

    Args:
    - username (str): The username to check.

    Returns:
    - ok: An `ok` object indicating the status of the username:
      - If username is on auction: status=True, real_status='OnAuction'
      - If username not in fragment.com: status=False, real_status='UnAvailable'
      - If username is an NFT: status=False, real_status='SOLD'
      - If username is available: status=False, real_status='Available'

    Raises:
    - Exception: If an unknown error occurs during the process.
        """
        try:
            soup = S(self.sender.get(self.f_api(username)).content, 'html.parser')
            if soup.title.text.strip() != 'Just a moment...':
                
                meta = soup.find("meta", property="og:description").get("content")
                if any(key in meta for key in ["An auction to get the Telegram", "Telegram and secure your ownership"]):
                    return ok(status=True, username=username, note='11: In Fragment !!!',real_status='OnAuction')
                elif 'Find active auctions' in meta:
                    return ok(status=False, username=username ,note='22: Username not in fragment.com',real_status='UnAvailable')
                elif 'Check the current availability of' in meta:
                    return ok(status=False, username=username ,note='22: Username is NFT',real_status='SOLD')
                else:
                    return ok(status=False, username=username ,note='22: Username Available',real_status='Available')
            else:
                return ok(status=False, username=username, note="33: Please try again later <3, We got blocked from fragment.com.")

        except Exception as e:
            raise Exception(f'An unknown error occurred: {e}') 

### - 

def auction(self, username) -> info or ok:
    """
    Retrieves auction details for a username on the Fragment.

    Args:
    - username (str): The username to check.

    Returns:
    - info or ok: Depending on the auction status:
      - If username is in auction: Returns `info` with auction details.
      - If username is not in auction: Returns `ok` with status=False.

    Raises:
    - Exception: If an unknown error occurs during the process.
    """
    try:
        soup = S(self.sender.get(self.f_api(username)).content, 'html.parser')
        if soup.title.text.strip() != 'Just a moment...':
            mete = soup.find("meta", property="og:description").get("content")
            if "An auction to get the Telegram" in mete:
                spen = soup.find_all("span")
                a = re.findall('data-val="(.*?)">', str(spen[17]))
                b = re.findall('data-val="(.*?)">', str(spen[18]))
                c = re.findall('data-val="(.*?)">', str(spen[19]))
                return info(
                    status=True,
                    username=soup.find("span", attrs={'class': 'subdomain'}).string,
                    domain=soup.find("span", attrs={'class': 'domain'}).string,
                    highest_bid=soup.findAll('div', attrs={'class': 'table-cell-value tm-value icon-before icon-ton'})[0].string,
                    bid_step=soup.findAll('div', attrs={'class': 'table-cell-value tm-value icon-before icon-ton'})[1].string,
                    minimum_bid=soup.findAll('div', attrs={'class': 'table-cell-value tm-value icon-before icon-ton'})[2].string,
                    days=re.findall(r'data-val="(.*?)"', str(soup.find_all("span")[16]))[0],
                    hours=f"{a[0]}{a[1]}",
                    minutes=f"{b[0]}{b[1]}",
                    seconds=f"{c[0]}{c[1]}",
                    bid_history={
                        'binArray': [item.string for item in soup.findAll('div', attrs={'class': 'table-cell-value tm-value icon-before icon-ton'})[3:]],
                        'historyArray': [item.string for item in soup.findAll('time', attrs={'class': 'short'})],
                        'urlArray': [re.findall("href=\"(.*?)\"", str(item))[0] for item in soup.findAll('a', attrs={'class': 'tm-wallet'})],
                        'hashArray': [re.findall("href=\"(.*?)\"", str(item))[0].replace('https://tonviewer.com/', '') for item in soup.findAll('a', attrs={'class': 'tm-wallet'})]
                    },
                    note='434: Username In Auction.'
                )
            else:
                return ok(status=False, username=username, note='443: Username not in auction.')
        else:
            return ok(status=False, username=username, note="33: Please try again later <3, We got blocked from fragment.com.")
    except Exception as e:
        raise Exception(f'An unknown error occurred: {e}')
