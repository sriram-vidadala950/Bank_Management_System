# class calculator:
#     def __init__(self,a,b):
#         self.a = int(a)
#         self.b = int(b)
#     def addition(self):
#         return f"addition of {self.a,self.b} = {self.a+self.b}"
#     def subtraction(self):
#         return f"subtraction  of {self.a, self.b} = {self.a-self.b}"
#     def multiplication(self):
#         return f"Multiplication of {self.a, self.b} = {self.a*self.b}"
#     def division(self):
#         if self.b == 0:
#             return "denominator can't be Zero(0)"
#         else:
#             return f"Division of {self.a, self.b} = {self.a/self.b}"
# addition = calculator("3","4")
# print(addition.addition())
# subtraction = calculator(3,5)
# print(subtraction.subtraction())
# product = calculator(5,3)
# print(product.multiplication())
# division = calculator(3,4)
# print(division.division())
class Moblie_Banking:
    def __init__(self):
        self.customers = {}
class hi(Moblie_Banking):
    def __init__(self):
        super().__init__()
        self.customers = {"PY001" : {"Name": "Nagarjuna", "Age": 25,"Account_Number" : "PYBACC12034567", "Address": "Hyderabad", "Balance": 2000, "Phone_Number": "+91-9876543210", "Email": "nagarjuna.123@gmail.com"}}
    def display(self,id):
        if id in self.customers:
            print("yes")
        else:
            print("No")
m = Moblie_Banking()
h = hi()
while True:
    try:
        choice = int(input("Enter 1 to continue or 0 to stop : "))
        if choice == 1:
            id = input("enter id : ")
            h.display(id)

        elif choice == 0:
            break
        else:
            print("Enter proper value ")
    except Exception as e:
        print(f"Error : {e}")