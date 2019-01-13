num=int(raw_input())
rev=0
while (num>0):
	rm=num%10
	rev=(rev*10)+rm
	num=num/10
print rev
