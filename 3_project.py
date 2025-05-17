# import tkinter as tk
# from tkinter import messagebox

# # Check credentials
# def login():
#     user = username_entry.get()
#     pwd = password_entry.get()

#     if user == "admin" and pwd == "1234":
#         messagebox.showinfo("Login", "✅ Login Successful!")
#     else:
#         messagebox.showerror("Login", "❌ Invalid Credentials")

# # Create GUI window
# root = tk.Tk()
# root.title("Login Form")
# root.geometry("500x500")

# # Username
# tk.Label(root, text="Username:").pack(pady=5)
# username_entry = tk.Entry(root)
# username_entry.pack(pady=5)

# # Password
# tk.Label(root, text="Password:").pack(pady=5)
# password_entry = tk.Entry(root, show="*")
# password_entry.pack(pady=5)

# # Login button
# tk.Button(root, text="Login", command=login).pack(pady=10)

# root.mainloop()

import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

def say_hi():
    label.config(text="Hello, hi")

def close_window():
    root.destroy()  # Closes the application window

root = tk.Tk()
root.title("Tkinter Exit Button Example")
root.geometry("300x150")

label = tk.Label(root, text="Click a button")
label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

btn1 = tk.Button(button_frame, text="Say Hello", command=say_hello)
btn1.pack(side="right", padx=5)

btn2 = tk.Button(button_frame, text="Say Hi", command=say_hi)
btn2.pack(side="left", padx=5)

exit_btn = tk.Button(root, text="Exit", command=close_window)
exit_btn.pack(pady=10)

root.mainloop()
