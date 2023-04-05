
mylist=[[1],[0,1],[0,1,1],[0,1,1,1]]
num=4
total=3
while True:
	mylist.append([0,1])
	total+=1
	k=2
	while k<num//2+1:
		mylist[num].append(mylist[num-k][k]+mylist[num-1][k-1])
		total+=mylist[num-k][k]
		k+=1
	while k<num+1:
		mylist[num].append(mylist[num-1][k-1])
		k+=1
	if total%10000==0:
		break

	num+=1

print(num)
print(total)


