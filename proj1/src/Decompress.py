# -*- coding: utf-8 -*-
from __future__ import division
import codecs
import sys
import os

if len(sys.argv) < 3:
	print("You must pass 2 arguments: readfile and writefile.")
	sys.exit()

try:
	readCode = codecs.open(sys.argv[1], encoding='utf-8', mode="r")
	readDat = codecs.open(sys.argv[2], mode="r")
	write = codecs.open(sys.argv[3], encoding='utf-8', mode="w")
except IOError:
	print("Wrong filename or directory.")
	sys.exit()

position = {0: " ", 1: "ა", 2: "ბ", 3: "გ", 4: "დ", 5: "ე", 6: "ვ", 7: "ზ", 8: "თ", 9: "ი", 10: "კ", 11: "ლ", 12: "მ", 13: "ნ",
				14: "ო", 15: "პ", 16: "ჟ", 17: "რ", 18: "ს", 19: "ტ", 20: "უ", 21: "ფ", 22: "ქ", 23: "ღ", 24: "ყ", 25: "შ", 26: "ჩ", 27: "ც", 28: "ძ", 29: "წ", 30: "ჭ", 31: "ხ", 32: "ჯ", 33: "ჰ"}

codes = [str(line.strip()) for line in readCode.readlines()]

temp = codecs.open('Temporary', mode="w+")
while True:
	ch = readDat.read(1)
	curr = readDat.tell()
	if not readDat.read(1):
		temp.write(format(ord(ch), "08b").rstrip('0')[:-1])
		break
	else:
		temp.write(format(ord(ch), "08b"))
		readDat.seek(curr)

temp.seek(0)
curr = ""
while True:
	ch = temp.read(1)
	if not ch:
		break
	curr += ch
	if curr in codes:
		write.write(position[codes.index(curr)].decode("utf-8"))
		curr = ""

temp.close()
os.remove('Temporary')

readCode.close()
readDat.close()
write.close()