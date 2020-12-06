#look at Kasey's day 1
#  passport counter =0
# for input:
# add contents to array index [passportCounter]
# if empty line, passport Counter += 1 
#flags for each item, if all true (except CID) accept

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

validID = 0
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
		# and cid > 0
		#print (id)
		validID += 1

print(validID)

#ecl
#pid
#eyr
#hcl
#byr
#iyr
#cid
#hgt