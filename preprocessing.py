import itertools

desired_countries = ["England", "Belgium", "France", "Spain", "Switzerland","Russia"]

result_file = open("preprocessed_data.csv", "w")

with open("./FIFA 2018 Statistics.csv","r") as f:
    header = f.readline()
    result_file.write("Date,Team,Scored,Ball Possession %\n")
    #read every 2 lines
    for line in f:
        line_splited = line.split(",")
        if line_splited[1] in desired_countries:
            result_file.write(",".join([line_splited[0], line_splited[1], line_splited[3], line_splited[4]]) + "\n")

