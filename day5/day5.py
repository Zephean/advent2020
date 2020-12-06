file = open('input.txt')

seats = []
for line in file.readlines():
	seats.append(line)

def findRow(boardingpass):
	floor = 0
	ceiling = 127
	var = 128
	row = 0
	for char in boardingpass:
		var /= 2
		if ceiling - floor == 1:
			if char == "F":
				row = floor
			if char == "B":
				row = ceiling
		elif char == "F":
			ceiling -= var
		elif char == "B":
			floor += var
	return row

def findCol(boardingpass):
	seats = boardingpass[7:10]
	floor = 0
	ceiling = 7
	var = 8
	col = 0
	for char in seats:
		var /= 2
		if ceiling - floor == 1:
			if char == "L":
				col = floor
			if char == "R":
				col = ceiling
		elif char == "L":
			ceiling -= var
		elif char == "R":
			floor += var
	return col

seatmap = [[0 for a in range(128)] for b in range(8)]
for boardingpass in seats:
	row = int(findRow(boardingpass))
	col = int(findCol(boardingpass))
	seatID = row * 8 + col
	#print (col, row, seatID, sep=" ")
	seatmap[col][row] = 1

colCounter = 0
rowCounter = 0
for seatrow in seatmap:
	rowCounter = 0
	for seat in seatrow:
		if seat == 0:
			seatID = int(rowCounter) * 8 + int(colCounter)
			print(int(colCounter), int(rowCounter), seatID, sep=" ")
			#print("Empty seat found. ID: ", seatID)
		rowCounter += 1
	colCounter += 1
