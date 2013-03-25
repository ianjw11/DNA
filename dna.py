from array import array
import sys
import itertools
from pprint import pprint
from struct import *
from bson.binary import Binary

import binascii

class Dna(object):
    def __init__(self):
        self.makedicts()
        
    def makedicts(self):
        self.decoder = list(map("".join, itertools.product("AGTC", repeat=4) ))
        self.coder = {val:idx for idx, val in enumerate(self.decoder)}

    def single_dec(self,x):
        """ used to decode bases that are not in blocks of 4  """
        return {0: 'A',64: 'G',129: 'T',192: 'C'}[x]
    def single_enc(self,x):
        """ used to encode bases that are not in blocks of 4  """
        return {'A':0,'G':64,'T':129,'C':192}[x]
    

    def pack(self,seq,file=False):
        bytearray = array("B") # makes unsigned char(1 byte) array
        """  local variables/functions are faster """
        senc = self.single_enc
        coder = self.coder
        BA = bytearray.append
        """  first array element is the modulus of seqlen and 4(used for decoding) """
        BA(len(seq) % 4)
        """ set up generator to grab blocks of 4 bases """
        for s in (seq[i:i+4] for i in range(0, len(seq), 4)):
            length = len(s)
            if length == 4:
                BA(coder[s])
            else:
                """  if bases not block of 4 use single encode method  """
                for base in str(s):
                    BA(senc(base))
        self.packed = bytearray
        
        if file:
            """ write binary sequence to file """
            f = open(file,"wb")
            bytearray.tofile(f)
            
    def unpack(self,bytearray):
        decoder = self.decoder
        sdec = self.single_dec
        seqlist = list() # lists are faster to add to than string concat
        sappend = seqlist.append
        remainer = bytearray.pop(0)
        """ end = last element in the array that represents 4 bases """
        end = len(bytearray) - remainer
        for s in bytearray[:end]:
            """ convert from unsigned char back to string of 4 bases  """
            sappend(decoder[s])
        for s in bytearray[end:]:
            """ convert single character bases """
            sappend(sdec(s))
        self.seq = ''.join(seqlist)
        
    def unpackfromfile(self,filename):
        f = open(filename,"rb")
        sarray = array("B") # empty byte array
        try:
            sarray.fromfile(f,99999999)
        except:
            pass
        self.unpack(sarray)
 