import re
import emoji
from rich import print
import random
class Bank_System:
    def __init__(self):
        self.bank_branches = [
                {"branch_number": "001", "branch_name": "Py National Bank - Main Branch", "ifsc_number": "PYNB000001", "manager": "Ravi Kumar", "branch_email": "mainbranch@pynationalbank.com", "address": "123 Python Ave, Code City, Telangana"},
                {"branch_number": "002", "branch_name": "Py National Bank - MG Road Branch", "ifsc_number": "PYNB000002", "manager": "Anita Sharma", "branch_email": "mgroad@pynationalbank.com", "address": "45 MG Road, Bengaluru, Karnataka"},
                {"branch_number": "003", "branch_name": "Py National Bank - Gachibowli Branch", "ifsc_number": "PYNB000003", "manager": "Suresh Babu", "branch_email": "gachibowli@pynationalbank.com", "address": "Plot 78, Gachibowli, Hyderabad, Telangana"},
                {"branch_number": "004", "branch_name": "Py National Bank - Anna Nagar Branch", "ifsc_number": "PYNB000004", "manager": "Lakshmi Devi", "branch_email": "annanagar@pynationalbank.com", "address": "12 Anna Nagar East, Chennai, Tamil Nadu"},
                {"branch_number": "005", "branch_name": "Py National Bank - Vizag Branch", "ifsc_number": "PYNB000005", "manager": "Nageswara Rao", "branch_email": "vizag@pynationalbank.com", "address": "Seethammadhara, Visakhapatnam, Andhra Pradesh"},
                {"branch_number": "006", "branch_name": "Py National Bank - Banjara Hills Branch", "ifsc_number": "PYNB000006", "manager": "Kavitha Reddy", "branch_email": "banjarahills@pynationalbank.com", "address": "Road No. 12, Banjara Hills, Hyderabad"},
                {"branch_number": "007", "branch_name": "Py National Bank - Powai Branch", "ifsc_number": "PYNB000007", "manager": "Nikhil Joshi", "branch_email": "powai@pynationalbank.com", "address": "Hiranandani, Powai, Mumbai"},
                {"branch_number": "008", "branch_name": "Py National Bank - Connaught Place Branch", "ifsc_number": "PYNB000008", "manager": "Preeti Arora", "branch_email": "connaught@pynationalbank.com", "address": "Block A, Connaught Place, Delhi"},
                {"branch_number": "009", "branch_name": "Py National Bank - Kothrud Branch", "ifsc_number": "PYNB000009", "manager": "Sameer Patil", "branch_email": "kothrud@pynationalbank.com", "address": "Paud Road, Kothrud, Pune"},
                {"branch_number": "010", "branch_name": "Py National Bank - Salt Lake Branch", "ifsc_number": "PYNB000010", "manager": "Niharika Das", "branch_email": "saltlake@pynationalbank.com", "address": "Sector V, Salt Lake City, Kolkata"}
            ]

    def branch_details(self):
        return self.bank_branches
    def add_branch(self,id,branch_name,ifsc_number,manager,branch_email,address,):
        for branch in self.bank_branches:
            if branch["id"]==id:
                print(f"[bold red]Branch ID {id} already exists..{emoji.emojize(':warning:')}[/bold red]")
                return
        self.bank_branches.append({"id":id,"branch_name":branch_name,"ifsc_number":ifsc_number,"manager":manager,"branch_email":branch_email,"address":address})
        return f"{branch_name} branch added successfully✅.."

    def delete_branch(self,id):
        for branch in self.bank_branches:
            if branch["id"] == id:
                branch_name = branch["branch_name"]
                self.bank_branches.remove(branch)
                return f"{branch_name} branch deleted successfully✅.."
        return f"Branch with {id} does not exists"
        
    def bank_details(self):
        return {
            "Bank_Name" : "Py National Bank",
            "Bank_code" : "PYBK702",
            "Bank_Type" : "Private",
            "Bank_Headquarters" : "Amaravati, Andhra Pradesh",   
            "Bank_IFSC" : "PYBK0001234",
            "Number_of_Branches" : "50",
            "Bank_Established" : "2005",
            "Bank_Contact" : "+91-9876543210",
            "Bank_Email" : "pynationalbank.1@pybank",
            "Bank_Website" : "www.pynationalbank.com",
            "Bank_Hours" : "Mon-Sat 9:00 AM - 5:00 PM",
            "Bank_Customer_Care" : "+91-9876543210"
        }
class Customer(Bank_System):
    def __init__(self):
        self.customers = {"PY001" : {"Name": "Nagarjuna", "Age": 25,"Account_Number" : "PYBACC12034567", "Address": "Hyderabad", "Balance": 2000, "Phone_Number": "+91-9876543210", "Email": "nagarjuna.123@gmail.com","password": None}}
        self.customer_id = "PY001"
    def add_customer(self,id, name, age,account_number, address, phone_number,branch, email,minimum_balance = 2000,password = None):
        if id in self.customers:
            return "Customer ID already exists! ❌"
        self.customers[id] = {
            "Name": name,
            "Age": age,
            "Account_Number": account_number,
            "Address": address,
            "Balance": minimum_balance,
            "Phone_Number": "+91-"+phone_number,
            "Branch" : branch,
            "Email": email,
            "password": password
        }
        self.customer_id = id
        return f"Customer {name} added successfully ✅.."
    def view_customers(self):
        if not self.customers:
            return "No customers found! ❌"
        for id, details in self.customers.items():
            print()
            print(f"Customer ID: {id}")
            for key, value in details.items():
                print(f"{key.replace('_',' ').title()}: {value}")
    def delete_customer(self, id):
        if id in self.customers:
            customer_name = self.customers[id]['Name']
            del self.customers[id]
            return f"Customer {customer_name} deleted successfully ✅.."
        else:
            return "Customer ID not found! ❌"
    def update_customer(self, id):
        if id not in self.customers:
            return f"Customer ID {id} not found! ❌"
        while True:
            try:
                print()
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Address")
                print("4. Update Phone Number")
                print("5. Update Email")
                print("0. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    while True:
                        print(f"Previous Name: {self.customers[id]['Name']}")
                        name = input("Enter new name: ").title().strip()
                        if not re.fullmatch(r"^[A-Za-z/s]+$",name):
                            print("Invalid name! Please enter a valid name. ❌")
                        else:
                            self.customers[id]['Name'] = name
                            break
                elif choice == 2:
                    while True:
                        print(f"Previous Age: {self.customers[id]['Age']}")
                        age = int(input("Enter new age: "))
                        if age < 18:
                            print("Age should be at least 18! ❌")
                        else:
                            break
                    self.customers[id]['Age'] = age
                elif choice == 3:
                    while True:
                        print(f"Previous Address: {self.customers[id]['Address']}")
                        address = input("Enter new address: ").title().strip()  
                        if not re.fullmatch(r"^[A-Za-z0-9/s]+$",address):
                            print("Invalid address! Please enter a valid address. ❌")
                        else:
                            self.customers[id]['Address'] = address
                            break
                elif choice == 4:
                    while True:
                        print(f"Previous Phone Number: {self.customers[id]['Phone_Number']}")
                        phone_number = input("Enter new phone number: ")
                        if not re.fullmatch(r"^[6-9][0-9]{9}$",phone_number):
                            print("Invalid phone number! Please enter a valid phone number. ❌")
                        else:
                            self.customers[id]['Phone_Number'] = "+91-"+phone_number
                            break
                elif choice == 5:
                    while True:
                        print(f"Previous Email: {self.customers[id]['Email']}")
                        email = input("Enter new email: ")
                        if not re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$",email):
                            print("Invalid email! Please enter a valid email. ❌")
                        else:
                            self.customers[id]['Email'] = email
                            break
                elif choice == 0:
                    print("Exiting update menu... 🏦")
                    break   
                else:
                    print("Invalid choice! ❌")
            except Exception as e:
                print(f"Invalid input: {e}")
        return f"Customer {id} updated successfully ✅.."
    def deposit(self, id, amount):
        if id not in self.customers:
            return "Customer ID not found! ❌"
        if amount<=0:
            return "Invalid amount! ❌"
        self.customers[id]['Balance'] += amount
        return f"Deposited {amount} to customer {id}'s account✅..."
    def withdraw(self,id,amount):
        if id not in self.customers:
            return "Customer ID not found! ❌"
        if amount<=0:
            return "Invalid amount! ❌"
        if self.customers[id]['Balance'] < amount:
            return "Insufficient balance! ❌"
        if self.customers[id]['Balance']-amount<2000:
            return "Minimum balance(2000) should be maintained! ❌"
        self.customers[id]['Balance'] -= amount
        return f"Withdrawn {amount} from customer {id}'s account✅..."
    def view_balance(self, id):
        if id not in self.customers:
            return "Customer ID not found! ❌"
        return f"Customer {id}'s balance: {self.customers[id]['Balance']}✅..."
    def transfer(self,from_id,to_id,amount):
        if from_id not in self.customers:
            return "Sender Customer ID not found! ❌"
        if to_id not in self.customers:
            return "Receiver Customer ID not found! ❌"
        if amount<=0:
            return "Invalid amount! ❌"
        if self.customers[from_id]['Balance'] < amount:
            return "Insufficient balance! ❌"
        if self.customers[from_id]['Balance']-amount<=2000:
            return "Minimum balance should be maintained! ❌"
        self.customers[from_id]['Balance'] -= amount
        self.customers[to_id]['Balance'] += amount
        return f"Transferred {amount} from customer {from_id} to customer {to_id}✅..."

class Mobile_Banking(Customer):
    def __init__(self):
        super().__init__()
    
    def login(self,id):
        if id not in self.customers:
            return "Customer ID not found! ❌"
        if self.customers[id]['password'] is None:
            print("Password not set! Please set a password to login. ❌")
            while True:
                choice = input("Do you want to create a password? (1/0): ")
                if choice == "1":
                    while True:
                        password = input("Enter password: ")
                        if not re.fullmatch(r"^[0-9A-Za-z!@#$%^&+=]{8,}$",password):
                            print("Password should be at least 8 characters long and contain letters, numbers, and special characters! ❌")
                        else:
                            break
                    return self.create_account(id,password)
                elif choice == "0":
                    return "Exiting... 🏦"
                    
                else:
                    print("Invalid choice! ❌")
        else:
            password = input("Enter password: ")
            if self.customers[id]['password'] == password:
                print("Login successful! ✅")
                try:
                    while True:
                        print()
                        print("1. Transfer")
                        print("2. Check Balance")
                        print("0. Exit")
                        choice = input("Enter your choice: ")
                        if choice == "1":
                            while True:
                                to_id = input("Enter Receiver Customer ID(PY001): ").upper()
                                if not re.fullmatch(r"^PY[0-9]+$",to_id):
                                    print(f"{to_id} is not a valid ID! Please enter a valid ID. ❌")
                                    print("Invalid ID! Please enter a valid ID. ❌")
                                else:
                                    break
                            amount = int(input("Enter amount to transfer: "))
                            print(self.transfer(id, to_id, amount))
                        elif choice == "2":
                            print(self.check_balance(id))
                        elif choice == "0":
                            return "Exiting... 🏦"
                        else:
                            print("Invalid choice! ❌")
                except Exception as e:
                    print(f"Invalid input: {e}")
            else:
                return "Invalid password! ❌"

    def create_account(self, id, password):
        if id not in self.customers:
            return "Customer ID not exists! ❌"
        self.customers[id]['password'] = password
        return f"Password set successfully for customer {id} ✅.."

    def check_balance(self, id):
        return super().view_balance(id)
    def transfer(self, from_id, to_id, amount):
        return super().transfer(from_id, to_id, amount)

    
# Main Program
c = Customer()
b = Bank_System()
m = Mobile_Banking()
while True:
    try:
        print()
        print(f"------------------[bold cyan]{emoji.emojize(":bank: Welcome to Py National Bank :bank:")}[/bold cyan]------------------")
        print("1. Bank")
        print("2. Customer")
        print("3. Mobile Banking")
        print("0. Exit")
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            print(f"[bold] Welcome to Bank class {emoji.emojize(":folded_hands:")}[/bold]")
            while True:
                print()
                print("1. Branch Details")
                print("2. Bank Details")
                print("0. Exit")
                print()
                choice = input("Enter your choice: ")
                print()
                if choice == "1":
                    for branch in b.branch_details():
                        print("")
                        for key,val in branch.items():
                            print(f"{key.replace('_',' ').title()} : {str(val).title()}")
                elif choice == "2":
                    for key,val in b.bank_details().items():
                        print(f"{key.replace('_',' ').title()} : {str(val).title()}")
                elif choice == "0":
                    print("Exiting bank menu... 🏦")
                    break
        elif choice == "2":
            print(f"[bold] Welcome to Customer class {emoji.emojize(":folded_hands:")}[/bold]")
            while True:
                print()
                print("1. Add Customer")
                print("2. View Customers")
                print("3. Update Customer")
                print("4. Delete Customer")
                print("5. Deposit")
                print("6. Withdraw")
                print("7. View Balance")
                print("8. Transfer")
                print("0. Exit")
                print()
                choice = input("Enter your choice: ")
                print()
                if choice == "1":
                    last_id = c.customer_id
                    while True:
                        print(f"Last Customer ID: {last_id}")
                        id = input("Enter Customer ID(PY001): ").upper()
                        if not re.fullmatch(r"^PY[0-9]+$",id):
                            print(f"{id} is not a valid ID! Please enter a valid ID. ❌")
                            print("Invalid ID! Please enter a valid ID. ❌")
                        else:
                            break
                    while True:
                        name = input("Enter name: ").title().strip()
                        if not re.fullmatch(r"^[A-Za-z/s]+$",name):
                            print("Invalid name! Please enter a valid name. ❌")
                        else:
                            break
                    while True:
                        age = int(input("Enter age: "))
                        if age < 18:
                            print("Age should be at least 18! ❌")
                        else:
                            break
                    while True:
                        address = input("Enter address: ").title().strip()
                        if not re.fullmatch(r"^[A-Za-z0-9/s]+$",address):
                            print("Invalid address! Please enter a valid address. ❌")
                        else:
                            break
                    while True:
                        phone_number = input("Enter phone number: ").strip()
                        if not re.fullmatch(r"^[6-9][0-9]{9}$",phone_number):
                            print("Invalid phone number! Please enter a valid phone number. ❌")
                        else:
                            break
                    
                    email = name.lower().replace(" ","")+"@gmail.com"
                    while True:
                        minimum_balance = int(input("Enter minimum balance: "))
                        if minimum_balance < 2000:
                            print("Minimum balance should be at least 2000! ❌")
                        else:
                            break   
                    account_number = "PYBACC" + str(random.randint(10**7, 10**8-1))
                    print(c.add_customer(id,name,age,account_number,address,phone_number,email,minimum_balance))
                elif choice == "2":
                    c.view_customers()
                elif choice == "3":
                    while True:
                        id = input("Enter Customer ID(PY001): ").upper()
                        if not re.fullmatch(r"^PY[0-9]+$",id):
                            print(f"{id} is not a valid ID! Please enter a valid ID. ❌")
                            print("Invalid ID! Please enter a valid ID. ❌")
                        else:
                            break
                    print(c.update_customer(id))
                elif choice == "4":
                    while True:
                        id = input("Enter Customer ID(PY001): ").upper()
                        if not re.fullmatch(r"^PY[0-9]+$",id):
                            print(f"{id} is not a valid ID! Please enter a valid ID. ❌")
                            print("Invalid ID! Please enter a valid ID. ❌")
                        else:
                            break
                    print(c.delete_customer(id))
                elif choice == "5":
                    while True:
                        id = input("Enter Customer ID(PY001): ").upper()
                        if not re.fullmatch(r"^PY[0-9]+$",id):
                            print(f"{id} is not a valid ID! Please enter a valid ID. ❌")
                            print("Invalid ID! Please enter a valid ID. ❌")
                        else:
                            break
                    amount = int(input("Enter amount to deposit: "))
                    print(c.deposit(id, amount))
                elif choice == "6":
                    while True:
                        id = input("Enter Customer ID(PY001): ").upper()
                        if not re.fullmatch(r"^PY[0-9]+$",id):
                            print(f"{id} is not a valid ID! Please enter a valid ID. ❌")
                            print("Invalid ID! Please enter a valid ID. ❌")
                        else:
                            break
                    amount = int(input("Enter amount to withdraw: "))
                    print(c.withdraw(id, amount))
                elif choice == "7":
                    while True:
                        id = input("Enter Customer ID(PY001): ").upper()
                        if not re.fullmatch(r"^PY[0-9]+$",id):
                            print(f"{id} is not a valid ID! Please enter a valid ID. ❌")
                            print("Invalid ID! Please enter a valid ID. ❌")
                        else:
                            break
                    print(c.view_balance(id))
                elif choice == "8":
                    while True:
                        from_id = input("Enter Sender Customer ID(PY001): ").upper()
                        if not re.fullmatch(r"^PY[0-9]+$",from_id):
                            print(f"{from_id} is not a valid ID! Please enter a valid ID. ❌")
                            print("Invalid ID! Please enter a valid ID. ❌")
                        else:
                            break
                    while True:
                        to_id = input("Enter Receiver Customer ID(PY001): ").upper()
                        if not re.fullmatch(r"^PY[0-9]+$",to_id):
                            print(f"{to_id} is not a valid ID! Please enter a valid ID. ❌")
                            print("Invalid ID! Please enter a valid ID. ❌")
                        else:
                            break
                    amount = int(input("Enter amount to transfer: "))
                    print(c.transfer(from_id, to_id, amount))
                elif choice == "0":
                    print("Exiting customer menu... 🏦")
                    break
                else:
                    print("Invalid choice! ❌")
        elif choice == "3":
            while True:
                print()
                print("1. Mobile Banking")
                print("0. Exit")
                print()
                choice = input("Enter your choice: ")
                if choice == "1":
                    while True:
                        id = input("Enter Customer ID(PY001): ").upper()
                        if not re.fullmatch(r"^PY[0-9]+$",id):
                            print(f"{id} is not a valid ID! Please enter a valid ID. ❌")
                            print("Invalid ID! Please enter a valid ID. ❌")
                        else:
                            break
                    print(m.login(id))
                elif choice == "0":
                    print("Exiting mobile banking menu... 🏦")
                    break
                else:
                    print("Invalid choice! ❌")
        elif choice == "0":
            print("Exiting... 🏦")
            break    
    except Exception as e:
        print(f"Invalid input: {e}")