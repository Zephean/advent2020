import csv
with open("/Users/codyhard/Documents/dev/advent2020/day2/input.csv", newline='') as open_csv:
	csv_reader = csv.reader(open_csv)
	list_CSV = list(csv_reader)

	validStrings = 0
	for row in list_CSV:
		#[0] min, [1] max, [2] letter, [3] code
		charCount = 0
		for i in row[3]:
			if i == row[2]:
				charCount += 1
		if charCount >= int(row[0]):
			if charCount <= int(row[1]):
				print(row[0] + " " + row[1] + " " + row[2] + " " + row[3])
				validStrings += 1
	print(validStrings)