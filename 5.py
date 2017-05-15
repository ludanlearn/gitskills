import pickle
import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
#request= urllib.request.Request(url)
# my pc must use proxy to connect
#request.set_proxy('172.16.0.252:80', 'http')
            
response= urllib.request.urlopen(url)
banner= pickle.load(response)
print(banner)
response.close()
for line in banner:
    print(''.join(map(lambda x: x[0]* x[1], line)))
             
#except Exception as ex:
 #   print(ex)