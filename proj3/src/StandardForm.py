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

def swap(matrix, pivNumb, row, col, perm):
	for target in range(pivNumb+1, col):
		if (matrix[pivNumb][target] == 1):
			break

	perm[target], perm[pivNumb] = perm[pivNumb], perm[target]

	for i in range(row):
		matrix[i][pivNumb], matrix[i][target] = matrix[i][target], matrix[i][pivNumb]

col, row = map(int, read.readline().split())

matrix = []
for i in range(row):
	matrix.append([int(j) for j in read.readline()[:col]])

perm = [i for i in range(col)]

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


write.write(str(col) + " " + str(row) + '\n' 
				+ ''.join([''.join([str(j) for j in i]) + '\n' for i in matrix]) 
					+ ''.join([str(i+1) + " " for i in perm]))

read.close()
write.close()