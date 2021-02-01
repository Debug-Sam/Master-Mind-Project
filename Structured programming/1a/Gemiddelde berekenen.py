
def average(lst):
    new_lst = []
    for i in lst:
        awn = sum(i)/len(i)
        new_lst.append([awn])
    return new_lst

lijst = [[1,2,3], [31,32,4], [31, 43, 55]]
print(average(lijst))