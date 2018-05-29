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

position = {" ":0, "ა":1, "ბ":2, "გ":3, "დ":4, "ე":5, "ვ":6, "ზ": 7, "თ": 8, "ი": 9, "კ": 10, "ლ": 11, "მ": 12, "ნ": 13,
				"ო": 14, "პ": 15, "ჟ": 16, "რ": 17, "ს": 18, "ტ": 19, "უ": 20, "ფ": 21, "ქ": 22, "ღ": 23, "ყ": 24, "შ": 25, "ჩ": 26, "ც": 27, "ძ": 28, "წ": 29, "ჭ": 30, "ხ": 31, "ჯ": 32, "ჰ": 33}

lex = [0] * 34
lexCouples = [0] * (34 * 34)

while True:
	first = read.read(1)
	curr = read.tell()
	second = read.read(1)
	if not first:
		break
	lex[position[first.encode("utf-8")]] += 1
	if second:
		lexCouples[position[first.encode("utf-8")] * 34 + position[second.encode("utf-8")]] += 1
	read.seek(curr)

en = "{0:.7f}".format(-sum(float(i/sum(lex)) * math.log(float(i/sum(lex)), 2) for i in lex if float(i/sum(lex)) != 0))
enCouples = "{0:.7f}".format(-sum(float(i/sum(lexCouples)) * math.log(float(i/sum(lexCouples)), 2) for i in lexCouples if float(i/sum(lexCouples)) != 0))

write.write(en + "\n" + enCouples + "\n" + "{0:.7f}".format(float(enCouples) - float(en)))

read.close()
write.close()