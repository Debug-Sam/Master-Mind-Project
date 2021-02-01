def count(lst, x):
    counter = 0
    for i in lst:
        if i == x:
            counter += 1
    return counter

def difference(lst):
    lst_min = lst[0]
    lst_max = 0
    for i in range(len(lst)):
        if (lst[i] < lst_min):
            lst_min = lst[i]
        elif (lst[i] - lst_min > lst_max):
            lst_max = lst[i] - lst_min
    return lst_max

def lst_check(lst):

    lst_zero = []
    lst_one = []

    for i in lst:
        if i != 1:
            if i != 0:
                return "De lijst bestaat niet alleen uit nullen, de lijst heeft ook: ", i

    for a in lst:
        if a == 1:
            lst_one.append(a)
        elif a == 0:
            lst_zero.append(a)

    if len(lst_one) < len(lst_zero):
        return "Er zijn meer nullen dan enen"
    if len(lst_zero) > 12:
        return "Er zijn teveel nullen in de lijst"
    else:
        return "De lijst klopt"


lijst = [0, 1, 2, 3 , 4, 5, 4, 6, 3, 2, 2, 2]

lijst2 = [0,0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1]

print(count(lijst, 2))

print(difference(lijst))

print(lst_check(lijst2))