import sys

if len(sys.argv) < 3:
	print("You must pass 2 arguments: readfile and writefile.")
	sys.exit()

try:
	read = open(sys.argv[1], "r")
	write = open(sys.argv[2], "w")
except IOError:
	print("Wrong filename or directory.")
	sys.exit()

final = '10000000'

for ch in iter(lambda: read.read(8), ''):
	write.write(chr(int(ch, 2)) if len(ch) == 8 else chr(int((ch + '1').ljust(8, '0'), 2)))
	k = len(ch)

write.write(chr(int(final, 2)) if k == 8 else '')

read.close()
write.close()