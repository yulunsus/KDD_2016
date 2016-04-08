import numpy as np
from sklearn import cross_validation, datasets, svm

filename = "PaperAuthorAffiliations.txt"

file_paper_author_affiliations = open(filename, "w")

counter = 0

for line in file_paper_author_affiliations:
	if counter < 100:
		print line
	counter = counter + 1
