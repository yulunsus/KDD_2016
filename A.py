import json
import sys

AffList ={}
AffAuthorList = {}
file = open(sys.argv[1])
for line in file:
	IdList = line.split()
	AffList.update({IdList[0]:IdList[1]})
	AffAutorList
print AffList



'''
AuthorAffList = {}
AffAuthorList = {}
num = 0
with open(sys.argv[1]) as f:
	for line in f:
		if num >= 10: break
		while True:
			if not line[-1] == "}":
				line = line[:-1]
			else:
				break 	
		print line
		PaperInfo = json.loads(line)
		for author, aff in PaperInfo["authors"]:
			author = author.lower()
			aff = aff.lower()
			if author in AuthorAffList:
				if aff not in AuthorAffList[author]:
					AuthorAffList[author].append(aff)
			else:
				AuthorAffList.update({author:[aff]})

			if aff in AffAuthorList:
				if author not in AffAuthorList[aff]:
					AffAuthorList[aff].append(author)
			else:
				AffAuthorList.update({aff:[author]})
		num = num + 1
print AuthorAffList
print AffAuthorList
'''
