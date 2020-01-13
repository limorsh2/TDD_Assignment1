import BubblesSort
import IBMfunc

choose = 3
while choose != 1 and choose != 2:
    choose = int(input("press 1 for IBM function or 2 for Bubble sort: "))

if choose == 1:
    height = float(input("Enter height: "))
    weight = float(input("Enter weight: "))
    print(IBMfunc.BMI(height, weight))
else:
    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    print(BubblesSort.bubble_sort(lst))









