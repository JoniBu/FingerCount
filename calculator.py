import util

#to sum numbers i.e. 3 fingers > GESTURE > 5 fingers = 8
def fingerSum(first, last):
    return first+last

#to combine numbers i.e. 3 fingers > GESTURE > 5 fingers = 35
def fingerAppend(first, last):
    return int(str(first) + str(last))

def createSeq(seq):
    i = 0
    prosSeq = []
    length = len(seq)-1
    for i in range(length):
        if seq[i] == "fist":
            prosSeq.append(fingerSum(seq[i-1], seq[i+1]))
        elif seq[i] == "palm":
            prosSeq.append(fingerAppend(seq[i-1], seq[i+1]))
        elif seq[i] == "call":
            prosSeq.append("+")
            if seq[i] == length:
                prosSeq.append(seq[i-1])
        elif seq[i] == "vulcan":
            prosSeq.append("-")
            if seq[i] == length:
                prosSeq.append(seq[i-1])
    if isinstance(prosSeq[-1], str): #dirty check if the last item is not number
        prosSeq.pop()
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

