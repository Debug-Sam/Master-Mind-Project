from itertools import permutations
from itertools import combinations_with_replacement
from itertools import product


def list_combinations():
    combinations = list(product(['A', 'B', 'C', 'D', 'E', 'F'], repeat=4))
    lst = []
    for i in combinations:
        b = list(i)
        lst.append(b)
    return lst

def split_lst(lst):
    lst_aabb = []
    for i in lst:
        if i[0] == i[1] and i[1] != i[2] and i[2] == i[3] or i[0] == i[2] and i[1] == i[3] and i[1] != i[2] or i[0] == i[3] and i[1] == i[2] and i[0] != i[1]:
            lst_aabb.append(i)



print(split_lst(list_combinations()))