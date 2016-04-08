from __future__ import division

selected_affiliation_filename = "2016KDDCupSelectedAffiliations.txt"
file_selected = open(selected_affiliation_filename,"r+")
sigir_rank_filename = "data_mining/affiliation_paper_counts/affiliation_paper_count_sigkdd.txt"

sigir_rank_file = open(sigir_rank_filename,"r+")

fo = open("result_kdd.tsv","w")

aff_id_list = []
aff_name_list = []
aff_check_list = []
for line in file_selected:
    line_split = line.split("	")
    aff_id_list.append(line_split[0])
    aff_name = line_split[1].split("\r\n")
    aff_name_list.append(aff_name[0])
    aff_check_list.append(0)

idx = 0
max_sigir = 0
sigir_id = "436976F3"

for line in sigir_rank_file:

    line_split = line.split("\n")
    aff_name = line_split[0]

    count_str = next(sigir_rank_file)
    count = count_str.split("\n")
    count_int = int(count[0])

    if idx == 0:
        idx += 1
        max_sigir = count_int

    aff_lower_case = aff_name.lower()
    aff_idx = aff_name_list.index(aff_lower_case)
    aff_id = aff_id_list[aff_idx]
    aff_check_list[aff_idx] = 1

    if idx == 0:
        prob_score = count_int/max_sigir
    else:
        prob_score = (count_int-1)/max_sigir

    fo.write(sigir_id + "\t" + aff_id + "\t" + str(round(prob_score,3)) + "\n")

zeros = 0
aff_remain = []
for i in range(len(aff_check_list)):
    if aff_check_list[i] == 0:
        zeros += 1
        fo.write(sigir_id + "\t" + aff_id_list[i] + "\t" + str(0.001) + "\n")
        aff_remain.append(aff_name_list[i])

print zeros
