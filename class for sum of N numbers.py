class sum_of_N_numbers:
    def __init__(self,num):
        self.num = int(num)
    @property
    def result(self):
        total = 0
        for i in range(self.num+1):
            total = total+i
        return f"sum of {self.num} Number is {total}"
nums = sum_of_N_numbers("10")
print(nums.result)