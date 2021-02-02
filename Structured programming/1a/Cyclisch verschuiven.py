#TODO: Ik moet nog zorgen dat als een bitje verdwijnt die aan de andere kant van de lijst weer toegevoegd wordt.
def cyclisch(ch, n):
    lst = []
    for i in ch:
        i = int(i)
        lst.append(i)
    print(lst)

    for l in range(len(lst)):
        if n <= l:
            #rechts
            lst[l], lst[l+1] = lst[l+1], lst[l]
        elif n > l:
            #links
            lst[l-1], lst[l] = lst[l], lst[l-1]

    new_ch = ""
    for m in lst:
        new_ch += str(m)

    return new_ch

print(cyclisch('1011000', 3))
print(cyclisch('1011100', -4))