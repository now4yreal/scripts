import os

table = 'abcdefghijklmnopqrstuvwxyz-_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#_abcdefghijklmnopqrstuvwxyz{}ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
#'_abcdefghijklmnopqrstuvwxyz{}ABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^\`\|~0123456789'

def Print(str):
	str='\033[31m'+str
	print str

def getCount(flag):
    os.system('echo '+flag+' | ./pin -t inscount0.so -o result -- ./easyparser >bin')
    with open("result") as f:
        count = int(f.read().split(" ")[1])
    return count


flag=list('flag{'+'1'*32+'}')
co=803161
for j in range(32):
	for i in range(len(table)):
		flag[5+j]=table[i]
		kk=''.join(flag)
		tmp=getCount(kk)
		print tmp,tmp-co,kk
		if tmp-co>1000:
			co=tmp
			break
		co=tmp


'''
record=0
co=2825621
for kk in range(12,16):
	for pointer in range(0,len(table)):
		succ=0
		flag_list=list(flag)
		flag_list[1+kk*2]=table[pointer]
		flag=''.join(flag_list)
		for i in range(len(table)):
			flag_list=list(flag)
			flag_list[0+kk*2]=table[i]
			flag=''.join(flag_list)
			temp=getCount(flag)
			print temp,temp-co,table[i],flag
			co=temp
			
			if abs(temp-co)>5000:
				if flag[1+kk*2]=='0' and flag[kk*2] =='0':
					continue
				succ=1
				co=temp
				break
			
			co=temp
			if succ==1:
			break
			
'''

	
				

