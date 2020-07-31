
import os, re
from pprint import pprint

path1 = r'E:\foo\bar'
path2 = r'E:\foo\fred'

def readU():
	listdir = os.listdir(path1) + os.listdir(path2)
	lst = []
	for i in listdir:
		ii = re.findall('\w+-\d+', i)[0].lower()
		lst.append(ii)
	return lst

def getRepeat(lst):
	slst =set(lst)
	for i in slst:
		lst.remove(i)
	print(lst)

def saveF(lst):
	lst_to_str = "\n".join(lst)
	with open("secret.txt", 'w') as f:
		f.write(lst_to_str)

def getF():
	with open("secret.txt", 'r') as f:
		lst = f.readlines()
		return [i.strip() for i in lst]

def printDict():
	lst = getF()
	dic = {}
	for i in lst:
		head = re.findall('\w+', i)[0]
		if head in dic:
			dic[head].append(i)
		else:
			dic[head] = [i]

	for k, v in dic.items():
		v.sort(key=lambda x:int(re.findall('\d+', x)[0]))
	pprint(dic)
	return dic

def printList():
	lst = getF()
	lst.sort(key=lambda x:(re.findall('\w+', x)[0],int(re.findall('\d+', x)[0])))
	pprint(lst)
	return lst

# lst = readU()
lst = printList()
saveF(lst)