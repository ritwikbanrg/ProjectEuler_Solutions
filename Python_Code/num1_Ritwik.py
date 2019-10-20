s=0
for i in range(0,1000,3):
	s=s+i
for i in range(0,1000,5):
	if i%3==0:
		continue
	s=s+i
print(s)
