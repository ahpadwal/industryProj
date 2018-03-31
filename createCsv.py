import csv


with open("desc.txt",'r') as raw_desc:
	new_line = (line.strip() for line in raw_desc)
	csv_line = (line.split(",") for line in new_line if line)
	with open('desc.csv','w') as output:
		writer = csv.writer(output)
		writer.writerows(csv_line)
