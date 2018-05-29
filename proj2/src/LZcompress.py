import sys
import math

if len(sys.argv) < 3:
	print("You must pass 2 arguments: readfile and writefile.")
	sys.exit()

try:
	read = open(sys.argv[1], "rb")
	write = open(sys.argv[2], "wb")
except IOError:
	print("Wrong filename or directory.")
	sys.exit()


length = '{0:08b}'.format(len(read.read()))
result = (len(length) - 1) * "0" + "1" + length[1:]

read.seek(0)

dictionary = {'0' : 0, "1" : 1}

code = ""
last = 0
length = 0
curr = ""
while True:
	ch = read.read(1)
	pos = read.tell()
	if not ch:
		break

	length += 1

	if not read.read(1):
		last = 1

	read.seek(pos)

	curr += '{0:08b}'.format(ord(ch))
	index = 0
	for c in curr:
		code += c
		if last == 1 and index == len(curr) - 1:
			last = 2
			while code not in dictionary:
				code += "0"

		if code in dictionary:
			size = math.ceil(math.log(len(dictionary), 2))
			temp = '{0:0b}'.format(dictionary[code])
			result += '0' * int((size - len(temp))) + temp

			dictionary[code + '0'] = dictionary.pop(code)
			dictionary[code + '1'] = len(dictionary)

			curr = curr[len(code):]
			index -= len(code)
			code = ""

			result += "1" + "0" * (7 - len(result) % 8) if last == 2 else ""
			while len(result) >= 8:
				write.write(chr(int(result[:8], 2)))
				result = result[8:]
		
		index += 1
	
	code = ""

read.close()
write.close()