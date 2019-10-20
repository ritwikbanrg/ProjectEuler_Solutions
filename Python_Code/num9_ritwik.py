f=0
for a in range(1,1000):
	for b in range(a,1000):
		csq=a**2+b**2
		c=csq**0.5
		if a+b+c==1000:
			f=1
			break
	if f==1:
		break
ans=a*b*c
print(int(ans))
