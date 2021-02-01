
def pyramide(a):
    for i in range(0, a):
        for j in range(0, i):
            print("* ", end="")
        print("\r")

    for n in range(a, 0, -1):
        for m in range(0, n ):
            print("* ", end="")
        print("\r")

def pyramide_reverse(a):

    spaces = 2 * a - 2
    for i in range(0, a):
        for j in range(0, spaces):
            print(end=" ")
        spaces = spaces - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

    spaces_reverse = 2 // a + 2
    for n in range(a, 0, -1):
        for m in range(0, spaces_reverse):
            print(end=" ")
        spaces_reverse = spaces_reverse + 2
        for v in range(n, 1, -1):
            print("* ", end="")
        print("\r")

pyramide(5)
pyramide_reverse(5)