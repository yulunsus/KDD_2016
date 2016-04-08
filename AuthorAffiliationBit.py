import json
import sys
from difflib import SequenceMatcher

AffList ={}
AffAuthorList = {}
AuthorAffList = {}
#read affiliations from affiliations.txt
file = open('Affiliations.txt')
for line in file:
	line = line.rstrip('\n')
	IdList = line.split("\t")
	AffList.update({IdList[0]:IdList[1]})
	#print IdList[0], AffList[IdList[0]]
	AffAuthorList.update({IdList[1]:[]})

num = 0
with open(sys.argv[1]) as f:
	for line in f:
		if num >= 10: break
		while True:
			if not line[-1] == "}":
				line = line[:-1]
			else:
				break 	
		#print line
		PaperInfo = json.loads(line)
		#print PaperInfo["authors"]
		if type(PaperInfo["authors"]) is list:
			print num, "is list"
		elif type(PaperInfo["authors"]) is dict:
			print num,"is dict"
			for author, aff in PaperInfo["authors"].iteritems():
				author = author.lower()
				aff = aff.lower()
				aff = aff.split(",")[0]
				print "&", author, "\t", aff
				if author in AuthorAffList:
					if aff not in AuthorAffList[author]:
						AuthorAffList[author].append(aff)
						#print "Aff Can't not be recognized:", aff
				else:
					AuthorAffList.update({author:[aff]})

				if aff in AffAuthorList:
					if author not in AffAuthorList[aff]:
						AffAuthorList[aff].append(author)
		num = num + 1

print ""
for author, aff in AuthorAffList.iteritems():
	print "* ", author,"\t", aff

for aff, author in AffAuthorList.iteritems():
	if author:
		print "->", aff, "\t", author
