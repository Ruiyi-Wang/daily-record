import io
import sys
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
url = 'http://www.cntour.cn/'     #中国旅游网网站
strhml = requests.get(url)
print(strhml.text)
