from __future__ import division
from sets import Set
from time import sleep
import sys

filename = "PaperAuthorAffiliations.txt"
# filename_2 = "extraction_of_each_conference/fse_selected.txt"
# filename_3 = "extraction_of_each_conference/mm_selected.txt"
# filename_4 = "extraction_of_each_conference/icml_selected.txt"
# filename_5 = "extraction_of_each_conference/mobicom_selected.txt"
# filename_6 = "extraction_of_each_conference/kdd_selected.txt"
filename_7 = "extraction_of_each_conference/sigcomm_selected.txt"
filename_8 = "extraction_of_each_conference/sigmod_selected.txt"
filename_1 = "extraction_of_each_conference/sigir_selected.txt"


file_paper_author_affiliation = open(filename, "r+")

# fo_2 = open("paper_affiliation/paper_affiliation/fse_paper_affiliations.txt", "w")
# fo_3 = open("paper_affiliation/paper_affiliation/mm_paper_affiliations.txt", "w")
# fo_4 = open("paper_affiliation/paper_affiliation/icml_paper_affiliations.txt", "w")
# fo_5 = open("paper_affiliation/paper_affiliation/mobiom_paper_affiliations.txt", "w")
# fo_6 = open("paper_affiliation/paper_affiliation/kdd_paper_affiliations.txt", "w")
fo_7 = open("paper_affiliation/sigcomm_paper_affiliations.txt", "w")
fo_8 = open("paper_affiliation/sigmod_paper_affiliations.txt", "w")
fo_1 = open("paper_affiliation/sigir_paper_affiliations.txt", "w")

counter = 0
# -------------- SIGIR --------------- #

file_selected_papers = open(filename_1, "r+")

selected_paper_set = Set([])
num_selected_paper = 0

for line in file_selected_papers:
    line_split = line.split("	")
    selected_paper_set.add(line_split[0])
    num_selected_paper += 1

print "#####  SIGIR paper IDs added to the set  #####"

for line_1 in file_paper_author_affiliation:

    line_split_1 = line_1.split("	")
    if line_split_1[0] in selected_paper_set:
        counter += 1
        print line_split_1[0] + "  " + "SIGIR  "
        print counter
        fo_1.write(line_split_1[0] + "	" + line_split_1[2] + "	" + line_split_1[5])

# # -------------- FSE --------------- #
# counter = 0
# file_selected_papers = open(filename_2, "r+")
# file_paper_author_affiliation.seek(0, 0)
# selected_paper_set = Set([])
# num_selected_paper = 0
#
# for line in file_selected_papers:
#     line_split = line.split("	")
#     selected_paper_set.add(line_split[0])
#     num_selected_paper += 1
#
# print "#####  FSE paper IDs added to the set  #####"
#
# for line_1 in file_paper_author_affiliation:
#
#     line_split_1 = line_1.split("	")
#     if line_split_1[0] in selected_paper_set:
#         counter += 1
#         print line_split_1[0] + "  " + "FSE  "
#         print counter
#         fo_2.write(line_split_1[0] + "	" + line_split_1[2] + "	" + line_split_1[5])

# # -------------- MM --------------- #
# counter = 0
# file_selected_papers = open(filename_3, "r+")
# file_paper_author_affiliation.seek(0, 0)
#
# selected_paper_set = Set([])
# num_selected_paper = 0
#
# for line in file_selected_papers:
#     line_split = line.split("	")
#     selected_paper_set.add(line_split[0])
#     num_selected_paper += 1
#
# print "#####  MM paper IDs added to the set  #####"
#
# for line_1 in file_paper_author_affiliation:
#
#     line_split_1 = line_1.split("	")
#     if line_split_1[0] in selected_paper_set:
#         counter += 1
#         print line_split_1[0] + "  " + "MM  "
#         print counter
#         fo_3.write(line_split_1[0] + "	" + line_split_1[2] + "	" + line_split_1[5])


# # -------------- ICML --------------- #
# counter = 0
# file_selected_papers = open(filename_4, "r+")
# file_paper_author_affiliation.seek(0, 0)
#
# selected_paper_set = Set([])
# num_selected_paper = 0
#
# for line in file_selected_papers:
#     line_split = line.split("	")
#     selected_paper_set.add(line_split[0])
#     num_selected_paper += 1
#
# print "#####  ICML paper IDs added to the set  #####"
#
# for line_1 in file_paper_author_affiliation:
#
#     line_split_1 = line_1.split("	")
#     if line_split_1[0] in selected_paper_set:
#         counter += 1
#         print line_split_1[0] + "  " + "ICML  "
#         print counter
#         fo_4.write(line_split_1[0] + "	" + line_split_1[2] + "	" + line_split_1[5])

# -------------- MOBICOM --------------- #
# counter = 0
# file_selected_papers = open(filename_5, "r+")
# file_paper_author_affiliation.seek(0, 0)
#
# selected_paper_set = Set([])
# num_selected_paper = 0
#
# for line in file_selected_papers:
#     line_split = line.split("	")
#     selected_paper_set.add(line_split[0])
#     num_selected_paper += 1
#
# print "#####  MOBICOM paper IDs added to the set  #####"
#
# for line_1 in file_paper_author_affiliation:
#
#     line_split_1 = line_1.split("	")
#     if line_split_1[0] in selected_paper_set:
#         counter += 1
#         print line_split_1[0] + "  " + "MOBICOM  "
#         print counter
#         fo_5.write(line_split_1[0] + "	" + line_split_1[2] + "	" + line_split_1[5])
#
# # -------------- KDD --------------- #
# counter = 0
# file_selected_papers = open(filename_6, "r+")
# file_paper_author_affiliation.seek(0, 0)
#
# selected_paper_set = Set([])
# num_selected_paper = 0
#
# for line in file_selected_papers:
#     line_split = line.split("	")
#     selected_paper_set.add(line_split[0])
#     num_selected_paper += 1
#
# print "#####  KDD paper IDs added to the set  #####"
#
# for line_1 in file_paper_author_affiliation:
#
#     line_split_1 = line_1.split("	")
#     if line_split_1[0] in selected_paper_set:
#         counter += 1
#         print line_split_1[0] + "  " + "KDD  "
#         print counter
#         fo_6.write(line_split_1[0] + "	" + line_split_1[2] + "	" + line_split_1[5])
#
# -------------- SIGCOMM --------------- #
counter = 0
file_selected_papers = open(filename_7, "r+")
file_paper_author_affiliation.seek(0, 0)

selected_paper_set = Set([])
num_selected_paper = 0

for line in file_selected_papers:
    line_split = line.split("	")
    selected_paper_set.add(line_split[0])
    num_selected_paper += 1

print "#####  SIGCOMM paper IDs added to the set  #####"

for line_1 in file_paper_author_affiliation:

    line_split_1 = line_1.split("	")
    if line_split_1[0] in selected_paper_set:
        counter += 1
        print line_split_1[0] + "  " + "SIGCOMM  "
        print counter
        fo_7.write(line_split_1[0] + "	" + line_split_1[2] + "	" + line_split_1[5])

# -------------- SIGMOD --------------- #
counter = 0
file_selected_papers = open(filename_8, "r+")
file_paper_author_affiliation.seek(0, 0)

selected_paper_set = Set([])
num_selected_paper = 0

for line in file_selected_papers:
    line_split = line.split("	")
    selected_paper_set.add(line_split[0])
    num_selected_paper += 1

print "#####  SIGMOD paper IDs added to the set  #####"

for line_1 in file_paper_author_affiliation:

    line_split_1 = line_1.split("	")
    if line_split_1[0] in selected_paper_set:
        counter += 1
        print line_split_1[0] + "  " + "SIGMOD  "
        print counter
        fo_8.write(line_split_1[0] + "	" + line_split_1[2] + "	" + line_split_1[5])

# for line in file_selected_papers:
#     line_split = line.split("	")
#     target_paper_id = line_split[0]
#     author_num = 0
#     shared_affiliation_list = []
#     for line_1 in file_paper_author_affiliation:
#             line_1_split = line_1.split("	")
#             paper_id = line_1_split[0]
#             affiliation_id = line_1_split[2]
#
#             if target_paper_id == paper_id:
#                 author_num = author_num + 1
#                 shared_affiliation_list.append(affiliation_id)
#
#     shared_score = 1/author_num
#     score_str = str(round(shared_score, 4))
#
#     print target_paper_id
#
#     for i in range(len(shared_affiliation_list)):
#         fo.write(target_paper_id + "	" + shared_affiliation_list[i] + "	" + score_str)
