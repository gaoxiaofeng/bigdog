from scrapy.selector import  Selector
from os.path import join,dirname,abspath
from scrapy.http import Request,FormRequest
from scrapy.spider import BaseSpider
# from selenium import webdriver
class JDdog(BaseSpider):
    name = "jd"
    headers_jd = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
                "Connection":"keep-alive",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding":"en,zh-CN;q=0.9,zh;q=0.8",
                "Cache-Control":"max-age=0",
                }
    urls = ["https://www.jd.com/"]
    def start_requests(self):
        for url in self.urls:
            yield Request(url=url,callback=self.parse, \
                headers=self.headers_jd)

    def parse(self, response):
        CurDir = dirname(abspath(__file__))
        cacheDir = join(dirname(CurDir),"cache")
        filename = "jd.html"
        filepath = join(cacheDir,filename)

        with open(filepath,"wb") as f:
            f.write(response.body)
        self.log("saved file %s"%filepath)
