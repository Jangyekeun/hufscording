line=int(input())
s=1
while line:
	if line>=0:
		print(' '*line, '*'*s)
		s+=2
		line-=1
	else :
		break
