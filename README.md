# UserApi Version 0.0.1

### UserApi
```
This Semple Pkg For Telegram UserNames
Advantages :
    Check-UserName . Get-Info-UserName 

```
### Features
- **Easy** and **Fast**

### Requirements

- Python 3.9+
- Fragment [NFT - AUCTION](https://fragment.com)
- [telegram](https://telegram.org)

### Installation

To install the development version from Github, use the following command:
```bash
pip install git+https://github.com/mooamel/userapi/userapilib.git
```

### Examples
Basic example:
```python

from userapilib import *

print(check().Nft(user)) #To Check If UserName Is 'NFT' Or not, Result >>> True - False

print(check().Fragment(user)) #To Check If UserName Is 'Fragment.com' Or not, Result >>> True - False

print(check().Fragment(user,proxy='123.123.123')) #Check If UserName Is 'Fragment.com' Or not 'With Proxis!', Result >>> True - False

print(info().auction(user))  #To Get Information UserName If in 'Fragment.com' , Result >>> Json Data

print(info().fragment(user)) #To Get Status UserName in 'Fragment.com' , Result >>> Onauction - Sold - For Sell - ect...

print(info().fragment(user,proxy='123.123.123')) #To Get Status UserName in 'Fragment.com' With Proxis! , Result >>> Onauction - Sold - For Sell - ect...

print(info().Nft(user)) #To Get Information UserName If is 'NFT' , Result >>> Json Data



```
For examples, check the [examples](https://github.com/mooamel/userapi/test.py).

# Thanks to
- You for viewing or using this project.

- [@MuamelAmeer](https://github.com/mooamel)
- [@D_DDDD](https://t.me/D_DDDD)
# License

MIT [License](https://github.com/mooamel/userapi/blob/main/LICENSE)
