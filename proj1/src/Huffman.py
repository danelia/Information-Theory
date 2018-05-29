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

n = int(read.readline())
list = [(float(word), str(k)) for word, k in zip(read.readline().split(), range(0, n))]
list.sort(key = lambda x:x[0])

while len(list) > 1 :
	firstTwo, rest = tuple(list[0:2]), list[2:]
	list = [(firstTwo[0][0] + firstTwo[1][0],firstTwo)] + rest
	list.sort()

def trim (tree):
    return tree[1] if isinstance(tree[1], str) else (trim(tree[1][0]), trim(tree[1][1]))

def getOutput (node, pat=""):
    if isinstance(node, str):
        output[node] = pat
    else:
        getOutput(node[0], pat + "0")
        getOutput(node[1], pat + "1")

output = {}
getOutput(trim(list[0]))

write.write(''.join((output[x] + '\n') for x in sorted(output.iterkeys())))

read.close()
write.close()