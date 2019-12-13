import csv
from itertools import combinations
csvfile=open("/Users/sanketmishra/Desktop/project/assignments/datamining/Apriori/groceries.csv",'r')
def itetolis(comb):
	z=[]*len(comb)
	for i in comb:
		x1=[]
		for j in i:
			x1.append(j)
		z.append(x1)
	return z
def createitemset(db,num):				#returns list of candidate
		comb=[]
		for i in list(db[1]):
			comb.append(i)
		comb=list(combinations(comb,num))
		z=itetolis(comb)
		return z
def findfreq(z,db,num):
	previous=db[num-1]
	comb=[]
	final=[]
	f=0
	for i in previous:
		prev_without_and=[]
		prev_without_and=i.split(" Aand ")
		for j in prev_without_and:
			if j not in comb:
				comb.append(j)
	comb=list(combinations(comb,num))
	list_of_cnum=itetolis(comb)
	for i in list_of_cnum:
#		print i
		y= list(combinations(i,num-1))
		y=itetolis(y)
		f=0
		for j in y:
			st=str(j[0])
			for j1 in range(1,len(j)):
				st=st+" Aand "+str(j[j1])
			if st not in list(db[num-1]):				#creation of sub itemset and then checking
				f=1
			st=""
		if f==0 and i not in final:
			final.append(i)
	#search db for values
	d={}
	for i in final:
		c=0
		for row in raw:
			f=0
			for j in i:
				if j not in row:
					f=1
			if f==0:
				c+=1
		st=str(i[0])
		for j1 in range(1,len(i)):
			st=st+" Aand "+str(i[j1])
		d[st]=c
	return d
items=[]
i1=[]
z=[]
raw=[]
d1={}
db=[""]*2
reader=csv.reader(csvfile)
for row in reader:
#	print(row)
	x=[]
	for item in row:
		if item != '':
			x.append(item)
			i1.append(item)
			if item not in items:
				items.append(item)
	raw.append(x)
#for i in raw:
#	print(i)
items.sort()
l1=[]
count=0
for i in items:						#adding count for 1-itemset
	l1.append(i)
	for z in i1:
		if i==z:
			count+=1
	d1[i]=count
	count=0
for i in list(d1):
	if d1[i]<40:
		d1.pop(i)
#for i in list(d1):
#	print i,d1[i]
db[1]=d1
for i in range(2,5):
	d={}
	c=0
	if i==2:
		print(i)
		z=createitemset(db,i)
		for i in z:
			for row in raw:
				if i[0] in row and i[1] in row:
					c+=1
			x2=str(i[0])+" Aand "+str(i[1])
			d[x2]=c
			c=0
			for x in list(d):		#pruning
				if d[x]<40:
					d.pop(x)
		db.append(d)
#		for i in db:
#			for j in i:
#				print j,i[j]
#			print "..."
	else:				#2freq done work for more than 2
		print(i)
		z=createitemset(db,i)
		d=findfreq(z,db,i)
		for x in list(d):		#pruning
				if d[x]<8:
					d.pop(x)
#		print d
		db.append(d)
for i in db:
	for j in i:
		print j," : ",i[j]
	print "...______________________________"
print "...________________________________"
for i in items:
	print i
print "..._____________________________"
z=list(db[1])
for i in items:
	if i not in z:
		print i
	
		
	

