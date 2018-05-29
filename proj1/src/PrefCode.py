# -*- coding: utf-8 -*-
from __future__ import division
import codecs
import sys
import math

if len(sys.argv) < 3:
	print("You must pass 2 arguments: readfile and writefile.")
	sys.exit()

try:
	read = codecs.open(sys.argv[1], encoding='utf-8', mode="r")
	write = codecs.open(sys.argv[2], encoding='utf-8', mode="w")
except IOError:
	print("Wrong filename or directory.")
	sys.exit()

firstList = [int(word) for word in read.readline().split()]
list = firstList[:]
list.sort(reverse=True)

kraft = sum(math.pow(2, -1 * i) for i in list)

output = []
if kraft <=1:
	first = True
	for i in list:
		if first:
			curr = '0' * i
			first = False
		else:
			new = (''.join('0' for j in range(0, len(curr[:i]) - len(curr[:i].rstrip('1')))) + '1')[::-1]
			curr = curr[:i - len(new)] + new
		output.append(curr)

for i in firstList:
	for j in output:
		if len(j) == i:
			write.write(j + '\n')
			output.remove(j)
			break

read.close()
write.close()