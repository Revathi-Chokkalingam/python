num=int(raw_input())
temp=num
rev=0
while (num>0):
	rm=num%10
	rev=(rev*10)+rm
	num=num/10
if(temp==rev):
	print "yes"
else:
	print"no"
