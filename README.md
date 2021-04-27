# scrapy-redis----fang.com
scrapy-redis分布式，爬取房天下网站上的所有新房跟二手房信息
需要安装：
pip install scrapy==1.8
pip install scrapy-redis==0.7.1
开启redis，在你的redis插入：lpush fang_url https://www.fang.com/SoufunFamily.htm
启动爬虫：scrapy crawl fang
如果要保存数据，在pipelines.py下配置你的数据库

