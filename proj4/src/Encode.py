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

write.write(str(int(k/(n - len(g) + 1) * n)) + "\n")
for i in range(int(k/(n - len(g) + 1))):
	curr = data[i * (n - len(g) + 1) : (i + 1) * (n - len(g) + 1)]
	result = [0] * (len(g) + len(curr))
	for j in range(len(g)):
		for l in range(len(curr)):
			result[j + l] = (result[j + l] + g[j] * curr[l]) % p
	result = result[:n] + [0] * (n - len(result))
	write.write(" ".join(str(x) for x in result))
	write.write("\n") if (i == int(k/(n - len(g) + 1)) - 1) else write.write(" ")

readPol.close()
readDat.close()
write.close()