import sys

if len(sys.argv) < 3:
	print("You must pass 2 arguments: readfile and writefile.")
	sys.exit()

try:
	read = open(sys.argv[1], "rb")
	write = open(sys.argv[2], "wb")
except IOError:
	print("Wrong filename or directory.")
	sys.exit()

p, n, g = int(read.readline()), int(read.readline()), [int(x) for x in read.readline().split()]

while g[len(g)-1] == 0:
	g.pop()

reminder = [p-1] + [0] * (n - 1) + [1]

result = [0] * n
for i in range(n, len(g)-2, -1):
	result[i-(len(g)-1)] = ((g[len(g)-1]**(p-2))*reminder[i])%p
	for j in range(len(g)):
		reminder[i-(len(g)-1) + j]-=((g[len(g)-1]**(p-2))*reminder[i]) % p * g[j]
	reminder = [x % p for x in reminder]

write.write("NO\n") if(reminder.count(0) != len(reminder)) else write.write("YES\n" + ' '.join(str(i) for i in result) + '\n')

read.close()
write.close()