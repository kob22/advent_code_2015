import hashlib
key = 'yzbqklnj'
i =0
while hashlib.md5((key + str(i)).encode('UTF-8')).hexdigest()[:5] != '00000':
    i+=1
print(i)
while hashlib.md5((key + str(i)).encode('UTF-8')).hexdigest()[:6] != '000000':
    i+=1
print(i)