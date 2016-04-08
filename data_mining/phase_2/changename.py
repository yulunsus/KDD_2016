import pprint
import json
from difflib import SequenceMatcher

def similar(a,b):
	return SequenceMatcher(None, a, b).ratio()

name_replace = [
		["technische universit\\u00e4t dortmund","technical university of dortmund"],
		["national & kapodistrian university of athens", "national and kapodistrian university of athens"],
		["link\u00f6ping university","linkoping university"]		
]


fileRead = open('kdd.json','r')
fileWrite = open('kdd_filtered.json','w')
fileCheck = open('kdd_problem_list','w')
num = 0
count = 0

AffList =[]
#read affiliations from affiliations.txt
file = open('../../Affiliations.txt')
for line in file:
        line = line.rstrip('\n')
        IdList = line.split("\t")
        AffList.append(IdList[1])


for line in fileRead:
	line = line.lower()
	while True:
		if line[-1] == "}":
			break
		else:
			line = line[:-1]
	
	line = json.loads(line)
	print num
	pprint.pprint(line)
	index = 0
	prob = 0
	if type(line["authors"]) is dict:
		for auth, aff in line["authors"].iteritems():
			auth = auth.split(",")[0]
			aff = aff.split(",")[0]
			index = 0
			prob = 0
			for i, Aff_cand in enumerate(AffList):
				p = similar(Aff_cand, auth)
				if p > prob:
					prob = p
					index = i
			print auth," : ", AffList[index]
			print prob
	print ""
	raw_input()
				 		
	'''
	index = line.find("authors")
	if index < 0:
		index = 0
	for name in name_replace:
		while True:
			if name[0] in line:	
				line = line.replace(name[0],name[1])
				print num
			else:
				break
	
	num = num + 1
	fileWrite.write(line)
	if "\\" in line[index:]:
		print num,line
		count+=1
	'''
	num += 1
#print count
	
