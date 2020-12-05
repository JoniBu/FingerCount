sums = ["fist", "palm"]
operations = ["call", 'vulcan']


#add validation that first and last are numbers TODO combine if conditions
def isValid(earlier2, earlier1, current):
    if isinstance(earlier2, int) and earlier1 in operations and isinstance(current, int):
        return True
    if isinstance(earlier2, int) and earlier1 in sums and isinstance(current, int):
        return True
    if isinstance(earlier2, int) and isinstance(earlier1, int) and current in sums:
        return True
    if earlier2 in sums and isinstance(earlier1, int) and isinstance(current, int):
        return True
    if earlier2 in sums and isinstance(earlier1, int) and current in operations:
        return True
    if earlier2 in operations and isinstance(earlier1, int) and current in operations:
        return True
    return False


#to iterate as groups
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))