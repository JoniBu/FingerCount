import util

#to sum numbers i.e. 3 fingers > GESTURE > 5 fingers = 8
def fingerSum(first, last):
    return first+last

#to combine numbers i.e. 3 fingers > GESTURE > 5 fingers = 35
def fingerAppend(first, last):
    return int(str(first) + str(last))


#def plusCalculation(firstNumber, secondNumber)
#def minusCalculation(firstNumber, secondNumber)
#...

def createSeq(seq):
    if (len(seq) % 3) != 1:
        return "Incorrect sequence length."
    sum = []
    for grp in util.chunker(seq, 3):
        if len(grp) == 3:
            if grp[1] == "fist":
                sum.append(fingerSum(grp[0], grp[2]))
            elif grp[1] == "palm":
                sum.append(fingerAppend(grp[0], grp[2]))
            elif grp[1] == "call":
                sum.append("+")
            elif grp[1] == "vulcan":
                sum.append("-")
        if grp[0] == "rock":
            calculateTotal(sum)

#calculate final result of everything inputted
def calculateTotal(sequence):

    return ""
