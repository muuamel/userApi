# UserApi [![Version](https://img.shields.io/pypi/v/UserApi?style=flat&logo=pypi)](https://pypi.org/project/UserAPi) [![Downloads](https://static.pepy.tech/personalized-badge/UserApi?period=month&units=none&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/UserApi)
### UserApi
```
This Semple Pkg For Telegram UserNames
Advantages :
    Check-UserName . Get-Info-UserName 
```
### Requirements
- Python 3.9+
- Fragment [NFT - AUCTION](https://fragment.com)
- [telegram](https://telegram.org)

### Installation
You can install UserAPi using pip:
```bash
pip install userapi
```
To install the development version from Github, use the following command:
```bash
pip install git+https://github.com/muamelameer/userapi/userapi.git
```

### Example
```python

from userapi import *

print(check().Nft(user)) #To Check If UserName Is 'NFT' Or not, Result >>> True - False

print(check().Fragment(user)) #To Check If UserName Is 'Fragment.com' Or not, Result >>> True - False

print(check().Fragment(user,proxy='123.123.123')) #Check If UserName Is 'Fragment.com' Or not 'With Proxis!', Result >>> True - False

print(info().auction(user))  #To Get Information UserName If in 'Fragment.com' , Result >>> Json Data

print(info().fragment(user)) #To Get Status UserName in 'Fragment.com' , Result >>> Onauction - Sold - For Sell - ect...

print(info().fragment(user,proxy='123.123.123')) #To Get Status UserName in 'Fragment.com' With Proxis! , Result >>> Onauction - Sold - For Sell - ect...

print(info().Nft()) #To Get Information UserName If is 'NFT' , Result >>> Json Data
```
For examples, check the [examples](https://github.com/muamelameer/userapi/test.py).

# Thanks to
- You for viewing or using this project.

### Follow me on social media accounts
- [@MuamelAmeer](https://github.com/muamelameer)
- [telegram](https://t.me/forkcode)
# License

MIT [License](https://github.com/muamelameer/userapi/blob/main/LICENSE)