import scrapy
from os.path import join,dirname,abspath
class firstDog(scrapy.Spider):
    name = "first"
    def start_requests(self):
        urls = ["https://www.zhihu.com/",\
                "http://baidu.com/"
                ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        CurDir = dirname(abspath(__file__))
        cacheDir = join(CurDir,"cache")

        page = response.url.split("/")[-1]
        filename = "firstDog-%s.html"%page
        filepath = join(cacheDir,filename)

        with open(filepath,"wb") as f:
            f.write(response.body)
        self.log("saved file %s"%filepath)