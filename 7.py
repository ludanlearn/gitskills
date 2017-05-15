from PIL import Image
im = Image.open('d:/oxygen.png')
w,h = im.size
print(w,h)
L = []
for i in [(x,y) for x in range(1,w) for y in range(1,h)]:
    s = im.getpixel(i)
    if s[0] == s[1] ==s[2]:
        L.append(chr(i[0]))
k = ''.join(L)
print(K.decode('utf-8'))