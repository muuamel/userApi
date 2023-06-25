from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'With This Package Can You GET Info Username And Checking '
LONG_DESCRIPTION = 'This PKG for checker telegram usernames .'

# Setting up
setup(
    name="userapi",
    version=VERSION,
    author="Muamel Ameer",
    author_email="amowallet@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests','fake_useragent','re','bs4'],
    keywords=['telegram','username','checker','fragment','api','telegram-username'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    url='https://github.com/muamelAmeer/userapi',
    project_urls={
        'Source': 'https://github.com/muamelAmeer/userapi',
        'Dev Lib': 'https://github.com/muamelAmeer',
        'Documentation': 'https://github.com/muamelAmeer/userApi/tree/main#example'
    },
)