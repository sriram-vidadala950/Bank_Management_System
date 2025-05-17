def intersection_of_3_lists(num1,num2,num3):
    li1 = set(num1)
    li2 = set(num2)
    li3 = set(num3)
    intersection = []
    for i in li1:
        if i in li2 and li3:
            intersection.append(i)
    print(intersection)
num1 = [1,2,2,3,4]
num2 = [1,2,8,5,4]
num3 = [1,2,6,7,4]
intersection_of_3_lists(num1,num2,num3)