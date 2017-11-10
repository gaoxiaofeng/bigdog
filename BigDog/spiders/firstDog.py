import scrapy
from scrapy.selector import  Selector
from os.path import join,dirname,abspath
class firstDog(scrapy.Spider):
    name = "first"
    def start_requests(self):
        urls = ["https://www.zhihu.com/",\
                ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.post_login, \
                headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
                "Referer":"https://www.zhihu.com/"
                })

    def parse(self, response):
        CurDir = dirname(abspath(__file__))
        cacheDir = join(dirname(CurDir),"cache")
        filename = "firstDog.html"
        filepath = join(cacheDir,filename)

        with open(filepath,"wb") as f:
            f.write(response.body)
        self.log("saved file %s"%filepath)
    def post_login(self,response):
        xsrf = Selector(response).xpath("//input[@name='_xsrf']/@value").extract()[0]
        print "xsrf:",xsrf
