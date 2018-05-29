# Information Theory

## Proj 0

### SimpleRead.py

Usage:

```
SimpleRead.py <inputFile> <outputFile>
```

Reads bits from input file and writes them in '0', '1' format in output file. If in inputFile is written “hello”,
in outputFile “0110100001100101011011000110110001101111” will be written.

### SeimpleWrite.py

Usage:

```
SeimpleWrite.py <inputFile> <outputFile>
```

Does the oposite of SimpleRead. If inputFile contains "0110100001100101011011000110110001101111", in outputFile "hello" will be written.

### CompleteWrite.py, CompleteRead.py

Usage:

```
CompleteWrite.py\CompleteRead.py <inputFile> <outputFile>
```

SimpleRead and SimpleWrite will only work when bits in file is divisible by 8. CompleteWrite and CompleteRead will work for everything.

## Proj 1

### Distrib.py

Usage
```
Distrib.py <inputFile> <outputFile>
```

Reads Georgian text from inputFile and computes probability of each charachter and every pair of charachters and writes them in outputFile.

## Entropy.py

Usage
```
Entropy.py <inputFile> <outputFile>
```
Computes entropy of every charachter, every pair of charachters and every charachter relative to previous charachter(`H(Xn∣Xn−1)`).

### PrefCode.py

Usage
```
PrefCode.py <inputFile> <outputFile>
```

Reads 34 (33 letters in Georgian alphabet + space) and if they satisfy the Kraft inequality we build non-prefix code on alphabet {0, 1} and write it in outputFile.

### Huffman.py

Usage
```
Huffman.py <inputFile> <outputFile>
```

In this case we read probabilities and just like in PrefCode we build non-prefix code.

### Compress.xxx

Usage
```
Compress.py <code> <inputFile> <outputFile>
```

Reads non-prefix code from first file, Georgian text from inputFile and using Huffman algorithm compresses it and puts in outputFile.

### Decompress.py

Usage
```
Decompress.py <code> <inputFile> <outputFile>
```

Reads code from first file and using it decompresses inputFile and writes it in the outputFile.

## Proj 2

### LZcompress.py,  LZdecompress.py

Usage:

```
LZcompress.py\LZdecompress.py <inputFile> <outputFile>
```

Slightly different Lempel–Ziv Compression algorithm.

## Proj 3

### StandardForm.py

Usage:

```
StandardForm.py <inputFile> <outputFile>
```

Reads binary code generator matrix, and we find generator matrix that will give us binary code equivalent to that one.

### ParityCheck.py

Usage:

```
ParityCheck.py <inputFile> <outputFile>
```

Given code generator matrix, we find checker matrix for that code.

### DecodingTable.py

Usage:

```
DecodingTable.py <inputFile> <errorFile> <outputFile>
```
Reads generator matrix from inputFile and error count 'e' from errorFile. Using this information we compute data which includes 
how to get syndrome (checker matrix) from code word and წhich syndrome corresponds to which position (decoding table).

### Encode.py

Usage:

```
Encode.py <matrix> <inputFile> <outputFile>
```

Using matrix as first argument we encode inputFile and write it to outputFile.

### Decode.py

Usage:

```
Decode.py <data> <inputFile> <outputFile>
```

Using data (generated in DecodingTable.py) we find errors, correct them and restore defailt data (not the original).

## Proj 4

### ParityCheck.py

Usage:

```
ParityCheck.py <inputFile> <outputFile>
```

Given polynomial expression and length of code we check if we can generate that code with given expression and if we can we find 
checker polynomial expression for that code.

### Encode.py

Usage:

```
Encode.py <data> <inputFile> <outputFile>
```

In data we will get code parameters, length of alphabet (p), length of code (n) and polynomial expression. In inputFile, on first line will 
be `k_in`, on second that many integers in range [0, p]. It is guaranted that `k_in` is multiple of `n*r` where r is effectiveness of code.
We will encode information in second file and write `k_out` in outputFile and that many encoded information on second line in range [0, p].

### Decode.py

Usage:

```
Decode.py <data> <inputFile> <outputFile>
```

We will assume that errors are corrected and decode inputFile using data.

### MinimalPolynomial.py

Usage:

```
MinimalPolynomial.py <inputFile> <pos> <outputFile>
```

Given primitive polynomial and position `i` we find minimal polynomial for `α^i`.

### BCH.py

Usage:

```
BCH.py <inputFile> <distance> <outputFile>
```

In inputFile we get alphabet size (p), integer `n` (our code size `N` should be `p^n - 1`) and `n+1` coefficient. In second file we have
minimal distance that our BCH code should give us. in outputFile we write `p`, number `N=p^n - 1`, and coefficient of generator matrix for our BCH code.
