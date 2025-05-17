def sum_of_digits_divisible_by_3(string):
    Sum = 0
    for i in range(len(string)):
        num = int(string[i])
        Sum+=num
    if(Sum%3==0):
        print("True")
    else:
        print("False")
string = "1234"
sum_of_digits_divisible_by_3(string)