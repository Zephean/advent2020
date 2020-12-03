import csv
with open("/Users/codyhard/Documents/dev/advent2020/day1/Sheet.csv", newline='') as open_csv:
    csv_reader = csv.reader(open_csv)
    list_CSV = list(csv_reader)

    for row1 in list_CSV:
    	#print("row1 fired")
    	#print(row1)
    	for row2 in list_CSV:
    		#print("row2 fired")
    		#print(row2)
    		for row3 in list_CSV:
	    		if int(row1[0]) + int(row2[0]) + int(row3[0]) == 2020:
	    			print(int(row1[0]) * int(row2[0]) * int(row3[0]))
