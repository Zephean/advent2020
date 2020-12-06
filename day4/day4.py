#this is pure sin and I should've just done regex from the start

file = open('input.csv')

ids = []
ids.append("")
counter = 0

for line in file.readlines():
	if line == '\n':
		#print("empty")
		counter += 1
		ids.append("")
		continue
	#print(counter, line, sep=" ")
	ids[counter] = ids[counter] + " " + line

def isValid(type, position, string):
	validlength = 0
	value = ""
	properSize = False
	#byr (Birth Year) - four digits; at least 1920 and at most 2002.
	if type == "byr":
		validlength = 4
		try:
			value = int(string[position : position+validlength])
		except:
			value = 0
		if position+validlength >= len(string):
			properSize = True
		elif string[position+validlength] == " " or string[position+validlength] == "\n":
			properSize = True
		if (value >= 1920 and value <= 2002) and properSize:
			return True
		else:
			return False
	#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	if type == "iyr":
		validlength = 4
		try:
			value = int(string[position : position+validlength])
		except:
			value = 0
		if position+validlength >= len(string):
			properSize = True
		elif string[position+validlength] == " " or string[position+validlength] == "\n":
			properSize = True
		if (value >= 2010 and value <= 2020) and properSize:
			return True
		else:
			return False
	#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	if type == "eyr":
		validlength = 4
		try:
			value = int(string[position : position+validlength])
		except:
			value = 0
		if position+validlength >= len(string):
			properSize = True
		else:
			#print(string[position+validlength])
			if string[position+validlength] == " " or string[position+validlength] == "\n":
				properSize = True
		#print (value, properSize, sep = " ")
		if (value >= 2020 and value <= 2030) and properSize:
			return True
		else:
			return False
	#hgt (Height) - a number followed by either cm or in:
	#	If cm, the number must be at least 150 and at most 193.
	#	If in, the number must be at least 59 and at most 76.

	#TODO - second from last should be valid w/ 174cm
	if type == "hgt":
		if id.find("in") > 0:
			validlength = 2
		elif id.find("cm") > 0:
			validlength = 3
		try:
			value = int(string[position : position+validlength])
		except:
			value = 0
		print(value)
		if position+validlength+2 >= len(string):
			properSize = True
		else:
			print(print(string[position+validlength+2]))
			if string[position+validlength+2] == " " or string[position+validlength+2] == "\n":
				properSize = True
		if value >= 150 and value <= 193 and properSize:
			print("within")
			return True
		elif value >= 59 and value <= 76 and properSize:
			return True
		else:
			return False
	#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	if type == "hcl":
		validlength = 7
		firstchar = 0
		try:
			value = string[position : position+validlength]
		except:
			value = ""
		for char in value:
			if firstchar == 0 and char == "#":
				firstchar = 1
				continue
			elif firstchar == 0:
				return False
			#from this point on in this function, forgive me...
			if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
				continue
			if char == "a" or char == "b" or char == "c" or char == "d" or char == "e" or char == "f":
				continue
			return False
		if position+validlength >= len(string):
			properSize = True
		elif string[position+validlength] == " " or string[position+validlength] == "\n":
			properSize = True
		if properSize:
			return True
		return False
	#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	if type == "ecl":
		validlength = 3
		try:
			value = string[position : position+validlength]
		except:
			value = ""
		if position+validlength >= len(string):
			properSize = True
		elif string[position+validlength] == " " or string[position+validlength] == "\n":
			properSize = True
		if value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth":
			if properSize:
				return True
		return False
	#pid (Passport ID) - a nine-digit number, including leading zeroes.
	if type == "pid":
		validlength = 9
		try:
			value = int(string[position : position+validlength])
		except:
			value = 0
		if position+validlength >= len(string):
			properSize = True
		else:
			#print(string[position+validlength], value)
			if string[position+validlength] == " " or string[position+validlength] == "\n":
				properSize = True
		if value > 0 and properSize:
			return True
		return False
	#cid (Country ID) - ignored, missing or not.

validID = 0
idcounter = 0
for id in ids:
	ecl = id.find("ecl")
	pid = id.find("pid")
	eyr = id.find("eyr")
	hcl = id.find("hcl")
	byr = id.find("byr")
	iyr = id.find("iyr")
	cid = id.find("cid")
	hgt = id.find("hgt")
	if ecl > 0 and pid > 0 and eyr > 0 and hcl > 0 and byr > 0 and iyr > 0 and hgt > 0:
		#print ("all fields present, checking validity...")
		if isValid("ecl", ecl+4, id) and isValid("pid", pid+4, id) and isValid("eyr", eyr+4, id) and isValid("hcl", hcl+4, id) and isValid("byr", byr+4, id) and isValid("iyr", iyr+4, id) and isValid("hgt", hgt+4, id):
			validID += 1
		print(idcounter, "ecl", isValid("ecl", ecl+4, id), "pid", isValid("pid", pid+4, id), "eyr", isValid("eyr", eyr+4, id), "hcl", isValid("hcl", hcl+4, id), "byr", isValid("byr", byr+4, id), "iyr", isValid("iyr", iyr+4, id), "hgt", isValid("hgt", hgt+4, id), sep = ": ")
	else:
		print(idcounter, " does not have all fields")
	idcounter += 1
print(validID)