import sys
import math

if len(sys.argv) < 3:
    print("You must pass 2 arguments: readfile and writefile.")
    sys.exit()

try:
    read = open(sys.argv[1], "rb")
    write = open(sys.argv[2], "wb")
except IOError:
    print("Wrong filename or directory.")
    sys.exit()

dictionary = ["0", "1"]

gettingSize = False
countingZeros = True
numZeros = 1
size = ""
curr = ""
result = ""
til = 1
while True:
        ch = read.read(1)
        if not ch:
            break

        curr += '{0:08b}'.format(ord(ch))

        if countingZeros:
            for i in curr:
                if i == '0':
                    numZeros += 1
                    curr = curr[1:]
                else:
                    gettingSize = True
                    countingZeros = False
                    break
        
        if gettingSize:
            for i in curr:
                size += i
                numZeros -= 1
                curr = curr[1:]
                if numZeros == 0:
                    size = int(size, 2)
                    gettingSize = False
                    break

        if not gettingSize and not countingZeros:
            if len(curr) > til:
                ch = curr[:til]
                pos = dictionary[int(ch, 2)]
                result += pos

                dictionary[int(ch, 2)] = pos + "0"
                dictionary.append(pos + "1")

                curr = curr[til:]
                til = int(math.ceil(math.log(len(dictionary), 2)))

                while len(result) >= 8 and size > 0:
                    write.write(chr(int(result[:8], 2)))
                    size -= 1
                    result = result[8:]

read.close()
write.close()