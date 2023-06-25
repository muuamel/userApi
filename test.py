
from userapi import *

print(check().Nft(user)) #To Check If UserName Is 'NFT' Or not, Result >>> True - False

print(check().Fragment(user)) #To Check If UserName Is 'Fragment.com' Or not, Result >>> True - False

print(check().Fragment(user,proxy='123.123.123')) #Check If UserName Is 'Fragment.com' Or not 'With Proxis!', Result >>> True - False

print(info().auction(user))  #To Get Information UserName If in 'Fragment.com' , Result >>> Json Data

print(info().fragment(user)) #To Get Status UserName in 'Fragment.com' , Result >>> Onauction - Sold - For Sell - ect...

print(info().fragment(user,proxy='123.123.123')) #To Get Status UserName in 'Fragment.com' With Proxis! , Result >>> Onauction - Sold - For Sell - ect...

print(info().Nft(user)) #To Get Information UserName If is 'NFT' , Result >>> Json Data