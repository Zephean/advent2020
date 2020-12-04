import csv
with open("/Users/codyhard/Documents/dev/advent2020/day3/input.csv", newline='') as open_csv:
	csv_reader = csv.reader(open_csv)
	list_CSV = list(csv_reader)

	#right 3 down 1
	xPosition = 0
	trees = 0
	firstLine = 0
	linecounter = 0

	for y in list_CSV:
		if firstLine == 0:
			firstLine = 1
			linecounter += 1
			#print("first line skipped")
			continue
		xPosition += 3
		if xPosition > 30:
			xPosition -= 31
		linecounter += 1
		print(linecounter, y[xPosition], xPosition, sep=" ")
		if y[xPosition] == "#":
			trees += 1
	print(trees)