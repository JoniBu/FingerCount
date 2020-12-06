from gestures import *



#add validation that first and last are numbers TODO combine if conditions
def isValid(prev, chain):
    if prev == "Number":
        if isinstance(chain, int):
            return prev, False 
        if chain in Operations:
            return "Operation", True
    if prev == "Operation":
        if len(chain) == 3:
            if isinstance(chain[0], int) and chain[1] == Sum and isinstance(chain[2], int):
                return "Number", True
            elif isinstance(chain[0], int) and chain[1] == Append and isinstance(chain[2], int):
                return "Number", True
    return prev, False 
    