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

write.write(''.join(format(ord(ch), "08b") for ch in iter(lambda: read.read(1), '')))

read.close()
write.close()