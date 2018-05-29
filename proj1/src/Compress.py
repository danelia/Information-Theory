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
	readDat = codecs.open(sys.argv[2], encoding='utf-8', mode="r")
	write = open(sys.argv[3], mode="w")
except IOError:
	print("Wrong filename or directory.")
	sys.exit()

position = {" ":0, "ა":1, "ბ":2, "გ":3, "დ":4, "ე":5, "ვ":6, "ზ": 7, "თ": 8, "ი": 9, "კ": 10, "ლ": 11, "მ": 12, "ნ": 13,
				"ო": 14, "პ": 15, "ჟ": 16, "რ": 17, "ს": 18, "ტ": 19, "უ": 20, "ფ": 21, "ქ": 22, "ღ": 23, "ყ": 24, "შ": 25, "ჩ": 26, "ც": 27, "ძ": 28, "წ": 29, "ჭ": 30, "ხ": 31, "ჯ": 32, "ჰ": 33}

codes = [str(line.strip()) for line in readCode.readlines()]

temp = codecs.open('Temporary', encoding='utf-8', mode="w+")
temp.write(''.join(codes[position[ch.encode("utf-8")]] for ch in iter(lambda: readDat.read(1), '')))

temp.seek(0)

final = '10000000'

for ch in iter(lambda: temp.read(8), ''):
	write.write(chr(int(ch, 2)) if len(ch) == 8 else chr(int((ch + '1').ljust(8, '0'), 2)))
	k = len(ch)

write.write(chr(int(final, 2)) if k == 8 else '')
temp.close()
os.remove('Temporary')

readCode.close()
readDat.close()
write.close()