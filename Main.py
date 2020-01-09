

choose = 9
while choose != 1 or choose !=2:
    choose = input("press 1 for IBM function or 2 for Bubble sort")

if choose == 1:
    height = input("Enter height: ")
    weight = input("Enter weight: ")
    print(IBM(height, weight))
else:
    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    print(bubble_sort(lst))









