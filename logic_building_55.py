def frequency_of_digists(nums):
    string = str(nums)
    dici = {}
    for i in string:
        if i not in dici:
            dici[i] = 1
        else:
            dici[i]+=1
    print(dici)
nums = 12343213456
frequency_of_digists(nums)