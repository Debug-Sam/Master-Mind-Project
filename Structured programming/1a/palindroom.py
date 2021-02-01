
def palindroom(x):
    return x == x[::-1]

def turn_palindroom(x):
    str_len = len(x)
    rev_str = x[str_len::-1]
    return rev_str

print(palindroom("samas"))
print(turn_palindroom("Sam"))