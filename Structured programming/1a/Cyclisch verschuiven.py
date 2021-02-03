
def cyclisch(ch, n):

    for l in range(abs(n)):
        if n < 0:
            ch = ch[-1] + ch
            ch = ch[:-1]
        elif n > 0:
            ch = ch + ch[0]
            ch = ch[1:]

    return ch

print(cyclisch('1011000', 3))
print(cyclisch('1011100', -4))