import sys
import itertools

if len(sys.argv) < 4:
	print("You must pass 3 arguments: readfile and writefile.")
	sys.exit()

try:
	readPol = open(sys.argv[1], "rb")
	readDist = open(sys.argv[2], "rb")
	write = open(sys.argv[3], "wb")
except IOError:
	print("Wrong filename or directory.")
	sys.exit()

p, n, g, dist = int(readPol.readline()), int(readPol.readline()), [int(x) for x in readPol.readline().split()], int(readDist.readline())
N = p**n - 1

while g[len(g)-1] == 0:
	g.pop()

poly = [[]] * (dist - 1)
for r in range(dist - 1):
	alfas = [[1]]

	temp = [0] * (p**n - 1)
	temp[r+1] = 1
	for j in range(len(temp) - 1, len(g)-2, -1):
		for k in range(len(g)):
			temp[j-(len(g)-1) + k]-=((g[len(g)-1]**(p-2))*temp[j]) % p * g[k]
		temp = [x % p for x in temp]

	curr = [1]
	for i in range(n):
		result = [0] * (len(temp) + len(curr))
		for j in range(len(temp)):
			for k in range(len(curr)):
				result[j + k] = (result[j + k] + temp[j] * curr[k]) % p
		curr = result

		for j in range(len(curr) - 1, len(g)-2, -1):
			for k in range(len(g)):
				curr[j-(len(g)-1) + k]-=((g[len(g)-1]**(p-2))*curr[j]) % p * g[k]
			curr = [x % p for x in curr]

		while curr[len(curr)-1] == 0:
			curr.pop()

		alfas.append(curr)


	for i in list(itertools.product(range(p), repeat = n+1))[1:]:
		i = i[::-1]

		temp = [[]] * (n + 1)
		for a in range(n + 1):
			temp[a] = [0] * (len([i[a]]) + len(alfas[a]))
			for j in range(len([i[a]])):
				for l in range(len(alfas[a])):
					temp[a][j + l] = (temp[a][j + l] + [i[a]][j] * alfas[a][l]) % p

			temp[a] = temp[a][:n] + [0] * (n - len(temp[a]))

		for j in range(n):
			k = sum([temp[l][j] for l in range(n + 1)]) % p
			if k != 0:
				break

		if(k == 0):
			i = list(i)
			while i[len(i)-1] == 0:
				i.pop()
			poly[r] = i
			break

result = [1]
for i in range(dist - 1):
	if(poly[i + 1:].count(poly[i]) == 0):
		temp = [0] * (len(poly[i]) + len(result))
		for t in range(len(poly[i])):
			for k in range(len(result)):
				temp[t + k] = (temp[t + k] + poly[i][t] * result[k]) % p
		result = temp

result = result[:N] + [0] * (N - len(result))

write.write(str(p) + "\n" + str(N) + "\n" + " ".join([str(i) for i in result]) + "\n")

readPol.close()
readDist.close()
write.close()