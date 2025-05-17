def return_min_number_and_index(li):
    minimum = min(li)
    index = li.index(minimum)
    return f"minimum number is {minimum} and its index is {index}"
li = [2,4,5,6,1,2]
result = return_min_number_and_index(li)
print(result)