import requests      #导入requests包
import codecs
url = 'http://192.168.0.112:8000'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
r = requests.get(url,headers=headers)        #Get方式获取网页数据
print ((r.text.encode(r.encoding).decode(r.apparent_encoding)))

# with open('xx.txt', 'w') as f:
#     f.write(r.text.encode(r.encoding).decode(r.apparent_encoding))

