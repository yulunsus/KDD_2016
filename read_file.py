import numpy as np
from sklearn import cross_validation, datasets, svm

filename = "2016KDDCupSelectedPapers.txt"
filename_1 = "PaperAuthorAffiliations.txt"

file_selected_papers = open(filename, "r+")
file_paper_author_affiliation = open(filename_1, "r+")

counter_sigir = 0
counter_sigmod = 0
counter_sigcomm = 0
counter_kdd = 0
counter_icml = 0
counter_fse = 0
counter_mobicom = 0
counter_mm = 0

counter = 0
for line in file_paper_author_affiliation:
	if counter < 13:
		print line
	else:
		break
	counter = counter + 1

for line in file_selected_papers:

		split_line = line.split('	')
		# print split_line
		for i in range(len(split_line)):
			if split_line[i] == "SIGIR\r\n":
				# print line
				counter_sigir = counter_sigir + 1
				break
			elif split_line[i] == "SIGCOMM\r\n":
				# print line
				counter_sigcomm = counter_sigcomm + 1
				break
			elif split_line[i] == "SIGMOD\r\n":
				# print line
				counter_sigmod = counter_sigmod + 1
				break
			elif split_line[i] == "KDD\r\n":
				# print line
				counter_kdd = counter_kdd + 1
				break
			elif split_line[i] == "ICML\r\n":
				# print line
				counter_icml = counter_icml + 1
				break
			elif split_line[i] == "FSE\r\n":
				# print line
				counter_fse = counter_fse + 1
				break
			elif split_line[i] == "MOBICOM\r\n":
				# print line
				counter_mobicom = counter_mobicom + 1
				break
			elif split_line[i] == "MM\r\n":
				# print line
				counter_mm = counter_mm + 1
				break

print "Number of SIGIR = "
print counter_sigir
print "Number of SIGCOMM = "
print counter_sigcomm
print "Number of SIGMOD = "
print counter_sigmod
print "Number of KDD = "
print counter_kdd
print "Number of ICML = "
print counter_icml
print "Number of FSE= "
print counter_fse
print "Number of MobiCom = "
print counter_mobicom
print "Number of MM = "
print counter_mm
