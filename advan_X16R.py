import hashlib
import base64
algorithm=[0,'algorithm1'
,'algorithm2','algorithm3','algorithm4','algorithm5','algorithm6','algorithm7'
,'algorithm8','algorithm9','algorithm10','algorithm11','algorithm12','algorithm13'
,'algorithm14','algorithm15','algorithm16']
sha_256=hashlib.sha256()

hash_str="abcdefg"
xor_result=''
sha_256.update(hash_str.encode('utf-8'))
hash_result=sha_256.hexdigest()
#print("Hash result:",hash_result)
first_16=hash_result[0:16]
second_16=hash_result[16:32]
third_16=hash_result[32:48]
last_16=hash_result[48:64]
for i in range(0,16):
	xor_result+=chr(ord(first_16[i])^ord(second_16[i])^ord(third_16[i])^ord(last_16[i]))
base_result=base64.b16encode(bytes(xor_result,encoding='utf-8'))
base_result_str=base_result.decode('utf-8')
for i in range(0,len(base_result_str[0:16])):
	if base_result_str[0:16][i].isdigit():
		if base_result_str[0:16][i]=='0' and base_result_str[16:32][i]=='0':
			print(algorithm[16])
		elif base_result_str[0:16][i]=='0' and base_result_str[16:32][i]!='0':
			print(algorithm[int(base_result_str[16:32][i])])
		else:
			print(algorithm[int(base_result_str[0:16][i])])
	else:
		print (algorithm[ord(base_result_str[0:16][i])-ord('A')+10])
