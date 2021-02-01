def sort(lst):
    lst_sorted = lst.copy()

    true_false = True
    while true_false:
        true_false = False
        for x in range(len(lst_sorted) - 1):
            if lst_sorted[x] > lst_sorted[x + 1]:
                lst_sorted[x], lst_sorted[x + 1] = lst_sorted[x + 1], lst_sorted[x]
                true_false = True
    return lst_sorted

lijst = [1,23, 43, 12, 54,32, 1323]

print(sort(lijst))