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

while True:
	ch = read.read(1)
	if not read.read(1):
		write.write(format(ord(ch), "08b").rstrip('0')[:-1])
		break
	else:
		write.write(format(ord(ch), "08b"))
		read.seek(read.tell()-1)

read.close()
write.close()