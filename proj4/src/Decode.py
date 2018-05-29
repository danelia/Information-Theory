import sys

if len(sys.argv) < 4:
	print("You must pass 3 arguments: readfile and writefile.")
	sys.exit()

try:
	readPol = open(sys.argv[1], "rb")
	readDat = open(sys.argv[2], "rb")
	write = open(sys.argv[3], "wb")
except IOError:
	print("Wrong filename or directory.")
	sys.exit()

p, n, g = int(readPol.readline()), int(readPol.readline()), [int(x) for x in readPol.readline().split()]

while g[len(g)-1] == 0:
	g.pop()

k, data = int(readDat.readline()), [int(x) for x in readDat.readline().split()]

write.write(str(int(k/n * (n - len(g) + 1))) + "\n")
for i in range(int(k/n)):
	reminder = data[i * n : (i + 1) * n]
	result = [0] * n
	for j in range(len(reminder) - 1, len(g)-2, -1):
		result[j-(len(g)-1)] = ((g[len(g)-1]**(p-2))*reminder[j])%p
		for l in range(len(g)):
			reminder[j-(len(g)-1) + l]-=((g[len(g)-1]**(p-2))*reminder[j]) % p * g[l]
		reminder = [x % p for x in reminder]
	result = result[:n - len(g) + 1] + [0] * (n - len(g) + 1 - len(result))
	write.write(" ".join(str(x) for x in result))
	write.write("\n") if (i == int(k/n - 1)) else write.write(" ")

readPol.close()
readDat.close()
write.close()