from PIL import Image
im = Image.open('d:/oxygen.png')
w,h = im.size
print(w,h)
L,g= [],[]
n = 0
for i in [(x,50) for x in range(1,w)]:
    s = im.getpixel(i)
    if s[0] == s[1] == s[2]:
       L.append(chr(s[0]))
while n < len(L):
    g.append(L[n])
    n = n + 7
print(''.join(g).encode('utf-8'))
    
    
