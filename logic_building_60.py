def sum_of_second_max_and_second_min(nums):
    min_1 = min(nums)
    max_1 = 0
    max_2 = 0
    min_2 = []
    for i in nums:
        if i !=min_1:
            min_2.append(i)
        if i > max_1:
            max_2 = max_1
            max_1 = i
    result = min(min_2)+max_2
    print(result)
nums = [8,1,3,9,11,5]
sum_of_second_max_and_second_min(nums)