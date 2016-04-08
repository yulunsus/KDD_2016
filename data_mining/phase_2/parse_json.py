from __future__ import division

filename = "kdd.json"

fin = open(filename,"r+")

for line in fin:
    line = line.split("\n")
    comma_separated = line[0].split(",")

    # extract keywords
    idx_keywords = 0
    idx_series = 0
    for item in comma_separated:
        if(item.find("keywords") != -1):
            break
        else:
            idx_keywords += 1

    for item in comma_separated:
        if(item.find("series") != -1):
            break
        else:
            idx_series += 1

    double_quote_separated  = line[0].split("\"")
    print double_quote_separated[3]

    keywords_colon_separated = comma_separated[idx_keywords].split(":")
    keywords_str = keywords_colon_separated[1].split("\"")


    # if(len(keywords_str[0]) == 0):
    #     keywords = "NO KEYWORD"
    #
    # keywords = keywords_str[1]


    # extract year
    idx_year = 0
    for item in comma_separated:
        if(item.find("year") != -1):
            break
        else:
            idx_year += 1

    year_colon_separated = comma_separated[idx_year].split(": ")
    year_str = year_colon_separated[1].split("\"")
    year_num = int(year_str[1])
