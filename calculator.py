#temp file

#all inputs/results of inputs, this is so we can build rewind function


#add validation that first and last are numbers TODO combine if conditions
def isValid(earlier2, earlier1, current):
    if isinstance(earlier2, str) and isinstance(earlier1, int) and isinstance(current, int):
        return True
    if isinstance(earlier2, int) and isinstance(earlier1, str) and isinstance(current, int):
        return True
    if isinstance(earlier2, int) and isinstance(earlier1, int) and isinstance(current, str):
        return True
    return False

#to sum numbers i.e. 3 fingers > GESTURE > 5 fingers = 8
def fingerSum(first, last):
    return first+last

def calculate(seq):
    if len(seq) < 2:
        return "Incorrect sequence."
    sums = []
    for i in range(0, len(seq)-3, 3):
        if seq[i+1] == "fist":
            sums.append(fingerSum(seq[i], seq[i+2]))
    return sums





#to combine numbers i.e. 3 fingers > GESTURE > 5 fingers = 35

#def plusCalculation(firstNumber, secondNumber)
#def minusCalculation(firstNumber, secondNumber)
#...

#calculate the total sum of everything inputted
#def finalSum(sequence)