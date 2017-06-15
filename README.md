# Setup

```
git clone git@github.com:TheGoodHoustonians/crawler.git
cd crawler
virtualenv -p python3 <your-base-virtualenv-path>/crawler
source <your-base-virtualenv-path>/crawler/bin/activate
pip install -r requirements.txt
scrapy runspider aggregate/spider.py
```
