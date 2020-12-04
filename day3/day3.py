import csv

def slope_check(list_CSV, xOffset, yOffset):
	xPosition = 0
	trees = 0
	firstLine = 0
	linecounter = 0
	for y in list_CSV:
		if firstLine == 0:
			firstLine = 1
			linecounter += 1
			continue
		if linecounter % yOffset != 0:
			print(linecounter, yOffset, linecounter % yOffset, sep = " " )
			linecounter += 1
			continue
		xPosition += xOffset
		linecounter += 1
		if xPosition > 30:
			xPosition -= 31
#		print(linecounter, y[xPosition], xPosition, sep=" ")
		if y[xPosition] == "#":
			trees += 1
	return trees

with open("/Users/codyhard/Documents/dev/advent2020/day3/input.csv", newline='') as open_csv:
	csv_reader = csv.reader(open_csv)
	csv = list(csv_reader)

	slope1 = slope_check(csv, 1, 1)
	slope2 = slope_check(csv, 3, 1)
	slope3 = slope_check(csv, 5, 1)
	slope4 = slope_check(csv, 7, 1)
	slope5 = slope_check(csv, 1, 2)
	print(slope1,slope2,slope3,slope4,slope5, sep = " * ")
	print(slope1*slope2*slope3*slope4*slope5)
