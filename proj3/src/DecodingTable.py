import sys

if len(sys.argv) < 4:
    print("You must pass 3 arguments: readfile and writefile.")
    sys.exit()

try:
    read = open(sys.argv[1], "rb")
    errorFile = open(sys.argv[2], "rb")
    write = open(sys.argv[3], "wb")
except IOError:
    print("Wrong filename or directory.")
    sys.exit()

def swap(matrix, pivNumb, row, col, perm):
	for target in range(pivNumb+1, col):
		if (matrix[pivNumb][target] == 1):
			break

	perm[target], perm[pivNumb] = perm[pivNumb], perm[target]

	for i in range(row):
		matrix[i][pivNumb], matrix[i][target] = matrix[i][target], matrix[i][pivNumb]

def getNth(col, vec, curr, error):
	if(len(curr) == col and error >= 0 ):
		vec.append(curr)
	else:
		getNth(col, vec, curr + "0", error)
		if(error > 0):
			getNth(col, vec, curr + "1", error - 1)

col, row = map(int, read.readline().split())

matrix = []
for i in range(row):
	matrix.append([int(j) for j in read.readline()[:col]])

perm = [i for i in range(col)]

error = int(errorFile.read())

for pivNumb in range(row):
	if (matrix[pivNumb][pivNumb] == 0):
		if (pivNumb != row - 1):
			for p in range (pivNumb + 1 , row):
				if(matrix[p][pivNumb] == 1):
					matrix[pivNumb], matrix[p] = matrix[p], matrix[pivNumb]
					break
		else:
			swap(matrix, pivNumb, row, col, perm)
	if (matrix[pivNumb][pivNumb] == 0):
		swap(matrix, pivNumb, row, col, perm)
	for i in range(row):
		if matrix[i][pivNumb] == 1 and i != pivNumb:
			for x in range(col):
				matrix[i][x] = (matrix[i][x] + matrix[pivNumb][x])%2

res = []
vec = []
s = 0
for i in range(row, col):
	for j in range(row):
		vec.append(matrix[j][i])

	for  k  in range(col - row):
		vec.append(1) if k == s else vec.append(0)
    	s += 1
    	res.append(vec)
    	vec = []

for i in range(len(perm)):
	if(perm[i] != i):
		for j in range(len(perm)):
			if (perm[j] == i):
				for k in range(len(res)):
					res[k][i], res[k][j] = res[k][j], res[k][i]
				perm[i], perm[j] = perm[j], perm[i]
				break

vec = []
table = {}
curr = ""
getNth(col, vec, curr, error)
for i in range(len(vec)):
	if (vec[i].count("1") <= error):
		v = [int(j) for j in vec[i]]
		temp = ""
		for row in res:
			temp += str(sum([row[k] * v[k] for k in range(len(row))]) % 2)
		table[vec[i]] = temp

write.write(str(len(table)) + '\n' + '\n'.join([table[i] + " " + i for i in table]))

read.close()
errorFile.close()
write.close()