#add validation that first and last are numbers TODO combine if conditions
def isValid(earlier2, earlier1, current):
    if isinstance(earlier2, str) and isinstance(earlier1, int):
        if current in ["call", "rock"]:
            return True
        if earlier2 not in ["call", "rock"] and isinstance(current, int):
            return True
    if isinstance(earlier2, int) and isinstance(earlier1, str) and isinstance(current, int):
        return True
    if isinstance(earlier2, int) and isinstance(earlier1, int) and isinstance(current, str) and current not in ["call", "rock"]:
        return True
    return False

#to iterate as groups
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

#def operations