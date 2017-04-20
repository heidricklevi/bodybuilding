# bodybuilding
web scraper using scrapy/selenium, grabbing exercises

This is a basic example using scrapy and selenium. 
I am primarily using this as a learning tool for myself, but I felt it would be great to put it out there for others to use/improve/learn
as well. 

Two main dependencies: scrapy and selenium.

From terminal/cmd: pip install scrapy
                   pip install selenium
                   
Find more information about crawling and these two modules:


https://docs.scrapy.org/en/latest/
http://selenium-python.readthedocs.io/getting-started.html


running the spider:

from root dir of project in terminal type: scrapy crawl bodybuilding

if you want output to JSON file: scrapy crawl bodybuilding -o bb.json

where 'bb' is an arbitrary file name
