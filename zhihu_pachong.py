#-*- coding:utf-8 -*-
import requests

class Zhihu_spider():

    def __init__(self,url,option = 'print_data_out'):

        self.option = option
        self.url = url
        self.header={}
        self.header['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36'
        self.header['Host'] = 'www.zhihu.com'
        self.header['Referer'] = 'www.zhihu.com'

        self.cookies = {
            "z_c0": '"Mi4wQUFBQURNdzNBQUFBUU1EV2ZxWVBDaGNBQUFCaEFsVk5LckhvVndEeE1CQ2ltZFlvR0lKU0hGU3VSbzZ1ZWFJYVl3|1472282491|c0f540e9d5f8b3cc493e905379fe2f2dd7bdb954"',
            #"unlock_ticket": 'QUZDQUp3czV3QWtYQUFBQVlRSlZUZnBxQ2xmSWNXX3NuVXo3SVJleUM5Uy1BLUpEdXJEcEpBPT0',
            "login": '"NTZkMWEyOTNiMzU5NGU4MWEzZGIzZTQ0OTRkNGE4MGE=|1472275498|2475c748854722812681b2abfbad3fdfdfb2b78a"',
            "n_c": "1",
            "q_c1": "71edacb85d74442cb118e290f770445f|1472105819000|1472105819000",
            "l_cap_id": '"ZWQyY2UyM2Q3NTI4NDczOWI5ZmU4NWUwYmFiZDhhNDM=|1472275473|641ba574445444647799d705746c11ce50a315cd"',
            "d_c0": '"AEDA1n6mDwqPTkcLWzFE2cPqqTPu6Dn34Ig=|1465628970"',
            "cap_id": '"YTA3NjFlYzhkYjAxNGQxYmIxODczYmE4MTE2OTMwYzQ=|1472275473|d60ad3ece5848d9aac67ad1766f77caf8dad1372"'

        }

        def send_request(self):


             added_followee_url = self.url + '/followees'
             try:
                 r = requests.get(added_followee_url,cookies = self.cookies,headers = self.header,verify = false)
             except:
                 re_crawl_url(self.url)
                 return

             content = r.text

             if r.status_code == 200:
                 self.parse_user_profile(content)


