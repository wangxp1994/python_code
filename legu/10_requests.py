
import requests
from lxml import etree

url = "http://desk.zol.com.cn/mingxing/"

headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
}

res = requests.get(url=url, headers=headers)

html =  etree.HTML(res.content)

result = html.xpath('//ul/li[@class="photo-list-padding"]/a/img/@src')

for u in result:
    res = requests.get(url=u, headers=headers)
    name = u.split("/")[-1]
    
    with open(name, "wb") as f:
        f.write(res.content)
