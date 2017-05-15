l = 'map'
s=''
for i in l:
    a = ord(i)
    if a>=97 and a<=120:
        a=ord(i)+2
    elif a==121:
        a=97
    elif a==122:
        a=98
    s=s+chr(a)
print(s)