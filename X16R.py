import  hashlib

algorithm=[0,'algorithm1'
,'algorithm2','algorithm3','algorithm4','algorithm5','algorithm6','algorithm7'
,'algorithm8','algorithm9','algorithm10','algorithm11','algorithm12','algorithm13'
,'algorithm14','algorithm15','algorithm16']
sha_256=hashlib.sha256()
hash_str="abcdefg"
sha_256.update(hash_str.encode('utf-8'))
hash_result=sha_256.hexdigest()
#print("Hash result:",hash_result)

last_16=hash_result[len(hash_result)-16:len(hash_result)]
#print("last 16 bytes:",last_16)
for i in range(0,len(last_16)):
	if last_16[i].isdigit():
		print(algorithm[int(last_16[i])])
	else:
		#print (ord(last_16[i])-ord('a')+10)
		print (algorithm[ord(last_16[i])-87])
