#swa
n,k=map(str,input().split(" "))
count=0
for i in range(0,len(n)):
	if n[i]==k:
		count=count+1
print(count)		
