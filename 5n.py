#5题，自己不看，写下试试
import urllib.request
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
f = urllib.request.urlopen(url)
s = pickle.load(f)
print(s)
for line in s:
    print(' '.join(list(map(lambda x:x[0]*x[1],line))))