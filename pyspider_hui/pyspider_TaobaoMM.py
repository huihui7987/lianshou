from pyspider.libs.base_handler import *
import os

N = 100
class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.baseurl =  'https://mm.taobao.com/json/request_top_list.htm?page='
        self.pageNum = 1
        self.pageTotle = 2
        self.deal = Deal()

    @every(minutes=24 * 60)
    def on_start(self):
        while self.pageNum <= self.pageTotle:
            url = self.baseurl+str(self.pageNum)
            print(url)
            self.crawl(url, callback=self.index_page)
            self.pageNum += 1

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.lady-name"]').items():
            print(each)
            self.crawl(each.attr.href, callback=self.detail_page,fetch_type='js')

    @config(priority = 2)
    def detail_page(self, response):
        domin = 'https:' + response.doc('.mm-p-domin-info li > span').text()
        self.crawl(domin,callable = self.domin_page)

    def domin_page(self,response):
        pass



class Deal:
    def __init__(self):
        self.path = '/home/exxxxx'
        if not self.path.endswith('/'):
            self.path = self.path + '/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def mkDir(self, path):
        path = path.strip()
        dir_path = self.path + path
        exists = os.path.exists(dir_path)
        if not exists:
            os.makedirs(dir_path)
            return dir_path
        else:
            return dir_path

    def saveImg(self, content, path):
        f = open(path, 'wb')
        f.write(content)
        f.close()

    def saveBrief(self, content, dir_path, name):
        file_name = dir_path + "/" + name + ".txt"
        f = open(file_name, "w+")
        f.write(content.encode('utf-8'))

    def getExtension(self, url):
        extension = url.split('.')[-1]
        return extension