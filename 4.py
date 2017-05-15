import urllib.request
t = '''http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=45439'''
next = ''
while True:
    response = urllib.request.urlopen(t)
    html = response.read()
    s = html.decode('utf-8')
    print(s)
    for i in s :
        if ord(i) >=48 and ord(i)<=57:
            next = next + i
    t = '''http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=''' + next
    next=''
    print(t)