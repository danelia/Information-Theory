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

write.write(''.join(chr(int(chars, 2)) for chars in iter(lambda: read.read(8), '')))

read.close()
write.close()