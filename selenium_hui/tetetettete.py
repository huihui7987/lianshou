#-*-coding:utf-8-*-

import requests,time,re
from bs4 import BeautifulSoup
from multiprocessing import Pool
html_doc = '''
<li class="item">
<a class="item-link" href="//mm.taobao.com/self/aiShow.htm?userId=485581745" target="_blank">
<div class="item-wrap">
<div class="img"><img src="//gtd.alicdn.com/sns_logo/i6/TB1rD3DLXXXXXcqXFXXSutbFXXX.jpg_240x240xz.jpg"/></div>
<div class="info">
<span class="name">何小蕊</span>
<span class="city">杭州市</span>
</div>
<div class="info row2">
<span>168CM / 48KG</span>
<span class="fr"><i class="iconfont"></i>44618</span>
</div>
</div>
</a>
</li>

<li class="item">
<a class="item-link" href="//mm.taobao.com/self/aiShow.htm?userId=397762786" target="_blank">
<div class="item-wrap">
<div class="img"><img data-ks-lazyload="//gtd.alicdn.com/sns_logo/i1/TB1Xp3qJVXXXXbBXFXXSutbFXXX.jpg_240x240xz.jpg" src="//g.alicdn.com/s.gif"/></div>
<div class="info">
<span class="name">卡瑞纳</span>
<span class="city">北京市</span>
</div>
<div class="info row2">
<span>176CM / 50KG</span>
<span class="fr"><i class="iconfont"></i>13380</span>
</div>
</div>
</a>
</li>

'''

soup = BeautifulSoup(html_doc,'lxml')
#print(soup)
uu = soup.find_all("a")
for cc in uu:
    ii = cc.get('href')
    print(ii)

