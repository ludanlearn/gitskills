import zipfile
import re
z = zipfile.ZipFile('D:/channel.zip','r')
txt = '90052.txt'
j = []
while True:
    j.append(z.getinfo(txt).comment.decode('utf-8'))
    file = z.read(txt).decode('UTF-8')
    
    print(file)
    next = re.findall(r'\d+',file)
    if next:
        txt = next[0] + '.txt'
 #       ''.join(txt.comment.encode('utf-8'))
    else:
        break
print(''.join(j))		