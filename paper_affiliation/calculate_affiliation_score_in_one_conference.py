### This script calculates the shared score of each paper in the specified conference ###
### Calculation method: Count the appearance of each paper and assign the score share ###
### to each affiliation (to which the author belongs).                                ###

from __future__ import division
import operator

# class Affiliation:
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def add_score(self, input_score):
#         self.score = self.score + input_score
#
#     def set_name(self, input_name):
#         self.name = input_name



filename = "sigmod_paper_affiliations.txt"
# filename = "sigmod_paper_affiliations.txt"
# filename = "sigcomm_paper_affiliations.txt"

fo = open(filename, "r+")
fo_output = open("score/sigmod_affiliation_score.txt", "w")

# calculate total number of author per paper
# store the paper names in one list and the share in another
paper_list = []
share_list = []

for line in fo:
    line_split = line.split("	")
    paper_id = line_split[0]

    if paper_id in paper_list:
        idx = paper_list.index(paper_id)
        share_list[idx] += 1
    else:
        paper_list.append(paper_id)
        share_list.append(0)

for i in range(len(paper_list)):
    info_str = str(paper_list[i]) + "	" + str(share_list[i])
    print info_str

# print("Number of papers: " + str(len(paper_list)))

### So far, we have the number of the author per paper ###
### parse the (conference_name)_paper_affiliations.txt again to assign the score share to each affiliation ###

fo.seek(0,0)

affiliation_list = []
assigned_score_sum_list = []

for line in fo:
    line_split = line.split("	")
    paper_id = line_split[0]
    affiliation_id = line_split[1]

    # look up share value for the current paper parsed
    paper_idx = paper_list.index(paper_id)
    share_value = share_list[paper_idx] # share_value is the inverse of the actual score credited to the affiliation
    if share_value > 0:
        if affiliation_id in affiliation_list:
            idx = affiliation_list.index(affiliation_id)
            assigned_score_sum_list[idx] += 1/share_value  # as mentioned above, thus divide 1 by share_value as the value to add
        else:
            affiliation_list.append(affiliation_id)
            assigned_score_sum_list.append(1/share_value)
    else:
        print "share_value = 0"

# Verify if the number of affiliation equals to the number of share_value
if len(affiliation_list) == len(assigned_score_sum_list):
    print "# of affiliations matches # of score"
else:
    print "### [Error]: # of affiliations does not match # of score ###"

print "len = " + str(len(affiliation_list))

# Sort score value for affiliations by dictionary
affiliation_value_tuple_list = []

for i in range(len(affiliation_list)):
    affiliation_value_tuple_list.append((affiliation_list[i],assigned_score_sum_list[i]))

affiliation_value_tuple_list.sort(key=lambda x: x[1])

for i in range(len(affiliation_value_tuple_list)):
    # do output file writing
    reverse_order_idx = len(affiliation_value_tuple_list) - i - 1
    fo_output.write(affiliation_value_tuple_list[reverse_order_idx][0] + "\t" + str(affiliation_value_tuple_list[reverse_order_idx][1]) + "\n")
    print affiliation_value_tuple_list[reverse_order_idx][0] + "\t" + str(affiliation_value_tuple_list[reverse_order_idx][1])
