#to sum numbers i.e. 3 fingers > GESTURE > 5 fingers = 8
def fingerSum(first, last):
    return first+last

#to combine numbers i.e. 3 fingers > GESTURE > 5 fingers = 35
def fingerAppend(first, last):
    return int(str(first) + str(last))

from gestures import *

def createSeq(seq):
    i = 0
    prosSeq = []
    length = len(seq)-1
    for i in range(length):
        if seq[i] == Sum:
            prosSeq.append(fingerSum(seq[i-1], seq[i+1]))
        elif seq[i] == Append:
            prosSeq.append(fingerAppend(seq[i-1], seq[i+1]))
        elif seq[i] == Operations[0]:
            prosSeq.append("+")
            if i > (length -1):
                if isinstance(seq[i+1], int) and isinstance(seq[i+2], int):
                    prosSeq.append(seq[i+1])
            elif i == length:
                if isinstance(seq[i+1], int):
                    prosSeq.append(seq[i+1])
        elif seq[i] == Operations[1]:
            prosSeq.append("-")
            if i > (length -1):
                if isinstance(seq[i+1], int) and isinstance(seq[i+2], int):
                    prosSeq.append(seq[i+1])
            elif i == length:
                if isinstance(seq[i+1], int):
                    prosSeq.append(seq[i+1])
    return prosSeq



#calculate final result from built sequence
def calculateTotal(prosSeq):
    i = 0
    total = prosSeq[0] #initialize with first value
    for i in range(len(prosSeq)-1):
        if prosSeq[i] == "-":
            total -= prosSeq[i+1]
        if prosSeq[i] == "+":
            total += prosSeq[i+1]
    return total

