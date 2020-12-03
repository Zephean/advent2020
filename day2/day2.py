import csv
with open("/Users/codyhard/Documents/dev/advent2020/day2/input.csv", newline='') as open_csv:
	csv_reader = csv.reader(open_csv)
	list_CSV = list(csv_reader)

	validStrings = 0
	for row in list_CSV:
		#[0] min, [1] max, [2] letter, [3] code
		charPosition = 0
		instances = 0

		for i in row[3]:
			charPosition += 1
			if charPosition == int(row[0]) or charPosition == int(row[1]):
				if i == row[2]:
					instances += 1
		if instances == 1:
			validStrings += 1
	print(validStrings)