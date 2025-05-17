def second_highest_frequency(nums):
    dici = {}
    for i in nums:
        if i not in dici:
            dici[i] = 1
        else:
            dici[i]+=1
    second_max = 0
    first_max = 0
    for key,value in dici.items():
        if value>first_max:
            second_max = first_max
            first_max = value
    print("Second_Highest_frequency : ",second_max)   
nums = [1,2,3,4,4,5,5,5] 
second_highest_frequency(nums)