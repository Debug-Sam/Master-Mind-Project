
def tekstcheck(a_string, b_string):

    if len(a_string) >= len(b_string):
        length = len(a_string)
    else:
        length = len(b_string)

    index = 0
    for i in range(length):
        if a_string[i] != b_string[i]:
            index = a_string.index(a_string[i])
            break
    return index

result_a = input("Geef een string: ")
result_b = input("Geef een string: ")
print(f"Het eerste verschil zit op index: {tekstcheck(result_a, result_b)}")
