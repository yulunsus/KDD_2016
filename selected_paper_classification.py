

filename = "2016KDDCupSelectedPapers.txt"
file_selected_papers = open(filename, "r+")

fo = open("parsed_files/mm_selected.txt", "w")

for line in file_selected_papers:
    line_split = line.split("	")
    conf_name = line_split[len(line_split)-1]
    if conf_name == "MM\r\n":
        fo.write(line)
