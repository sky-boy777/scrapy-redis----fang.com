from scrapy import signals
import random  # 用来设置随机的头跟ip


# 这里是下载中间件
class FangComDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # 这是我弄得，其他的默认没动
    def process_request(self, request, spider):
        '''在这里设置代理ip跟随机请求头'''
        # 随机请求头
        request.headers["User-Agent"] = random.choice(spider.settings.get("UA_LIST"))
        
        # 随机代理ip（但是我没钱买，穷哦，也懒得爬）
        # request.meta["proxy"] = random.choice(代理IP列表)

    def process_response(self, request, response, spider):
        '''可以查看请求头有没有设置成功'''
        #print(request.headers["User-Agent"])
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
