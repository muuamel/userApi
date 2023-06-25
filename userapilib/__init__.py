__title__ = "userapi"
__author__ = "Muamel Ameer"
__copyright__ = "Copyright 2023 Muamel Ameer"
__version__ = "0.0.1"
__github__ = "https://github.com/muamelameer/userapi"
# __pypi__ = "https://pypi.python.org/pypi/userapi"
from .userapi import *
from requests import get
# __newest__=get(f"{__pypi__}/json").json()["info"]["version"]

# if __newest__ != __version__:
#     print(f"""
#     New version of UserApi is out : {__newest__} (Using {__version__}
#     To Install : pip install userapi
#     Info Lib :
#     This Pkg For Telegram UserNames
#        Title : {__title__}
#        GitHub : {__github__}
#        Author : {__author__}
#        PyPi : {__pypi__}
#        CopyRight : {__copyright__}
#        """)
