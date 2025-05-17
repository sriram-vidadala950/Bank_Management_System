# # class library:
# #     def __init__(self):
# #         self.books = []
# #         self.noBooks = 0
# #     def addDSbooks(self,books):
# #         self.DS_books = []
# #         self.DS_books.append(books) 
# #         self.no_DS_books = len(self.DS_books)
# #     def getDSinfo(self):
# #         print(f"Total Number of DS books are : {self.no_DS_books}")
# #         print("Available DS books are : ")
# #         for i in self.DS_books:
# #             print(i)
# # books = library()
# # books.addDSbooks("stak and queuq")
# # books.addDSbooks("divide and conquer")
# # books.addDSbooks("knapsack Algorithms")
# # books.addDSbooks("brute force Algorithms")
# # books.getDSinfo()


# print(f"An Error occured in modifications. ERROR :  {emoji.emojize(":warning:")}")



# # ans = next((staff for staff in self.library_staff if self.role.lower() == staff["role"].lower()),"Not Found")
#         # print(ans)
#         # bok = next((b for b in self.books.values() if self.author.lower() == b["author"].lower()),"Not found")
#         # print(bok)

import re
import emoji
contact = input("enter a number : ").strip()
if not re.fullmatch(r"^[6-9]\d{9}$",contact):
    print(f"{emoji.emojize(':cross_mark:')}")
else:
    print(f"{emoji.emojize(':white_check_mark:')}")