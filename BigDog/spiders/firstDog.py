from scrapy.selector import  Selector
from os.path import join,dirname,abspath
from scrapy.http import Request,FormRequest
from scrapy.spider import BaseSpider
class firstDog(BaseSpider):
    name = "zhihu"
    headers_zhihu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
                "Referer":"https://www.zhihu.com/",
                "Connection":"keep-alive",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding":"en,zh-CN;q=0.9,zh;q=0.8",
                "Cache-Control":"max-age=0",
                "Host":"www.zhihu.com",

                }
    urls = ["https://www.zhihu.com/"]
    def start_requests(self):
        for url in self.urls:
            yield Request(url=url,callback=self.post_login, \
                headers=self.headers_zhihu,meta={"cookiejar":1})

    def parse(self, response):
        CurDir = dirname(abspath(__file__))
        cacheDir = join(dirname(CurDir),"cache")
        filename = "firstDog.html"
        filepath = join(cacheDir,filename)

        with open(filepath,"wb") as f:
            f.write(response.body)
        self.log("saved file %s"%filepath)
    def post_login(self,response):
        self.log_response("post_login.txt",response)


        xsrf = Selector(response).xpath("//input[@name='_xsrf']/@value").extract()[0]
        xsrf = "65303736363330342d333333352d343464392d396233622d316438373639636166653065"
        # print "meta:",response.meta
        return  [FormRequest("https://www.zhihu.com/login/phone_num",
                            method="POST",
                            meta={"cookiejar":response.meta["cookiejar"],"_xsrf":xsrf},
                            headers=self.headers_zhihu,
                            formdata={"phone_num":"13982133221","password":"newmedia","_xsrf":xsrf,"captcha_type:":"cn"},
                            callback=self.after_login,

                             )]

    def after_login(self,response):
        self.log_response("after_login.txt",response)


    def log_response(self,logName,response):
        CurDir = dirname(abspath(__file__))
        cacheDir = join(dirname(CurDir), "cache")
        filepath = join(cacheDir, logName)
        log = "header:\n" + str(response.headers) + "\n" + "body" + str(response.body)
        with open(filepath, "wb") as f:
            f.write(log)
