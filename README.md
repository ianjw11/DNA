DNA
===

Tools for working with DNA sequences

DNA.py - Binary encoding scheme for DNA text data
takes any arbitrary DNA
 text sequence as text and converts it to a packed array of 8 bit integers.
 Each 8 bit integer is able to store 4 base pairs(A,C,T, or G).
 Whereas storing them as text requires 8 bits for only one base pair.
 
 Since bases must be encoded in groups of 4, if the amount of bases is not divisible by 4, there is a mapping created where the integers at the end of the array will represent only one base pair per integer.  
 
 The first integer of the array stores the modulus of the length of the array and 4 so that we can reconstruct the sequence later.


test.py shows usage and an example
