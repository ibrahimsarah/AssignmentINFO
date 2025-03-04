import itertools

# Hardcoded password for the program
correct_password = "abcde"

# Predefined dictionary of passwords
dictionary = r"C:\Users\DELL\Desktop\100_common_passwords"

def dictionary_attack(username):
    print(f"Trying dictionary attack for user: {username}")
    for password in dictionary:
        print(f"Trying password: {password}")
        if password == correct_password:
            print("Success! Password found in dictionary.")
            return True
    print("Failed to find password using dictionary.")
    return False

def brute_force_attack():
    print("Starting brute force attack...")
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for password_tuple in itertools.product(chars, repeat=5):
        password = ''.join(password_tuple)
        print(f"Trying password: {password}")
        if password == correct_password:
            print("Success! Password found using brute force.")
            return True
    print("Failed to find password using brute force.")
    return False

def main():
    username = input("Enter your username: ")
    
    if not dictionary_attack(username):
        brute_force_attack()

if __name__ == "__main__":
    main()
    import tkinter as tk
from tkinter import messagebox
import itertools

correct_password = "abcde"
dictionary = r"C:\Users\DELL\Desktop\100_common_passwords"

def dictionary_attack(username):
    for password in dictionary:
        if password == correct_password:
            return True
    return False

def brute_force_attack():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for password_tuple in itertools.product(chars, repeat=5):
        password = ''.join(password_tuple)
        if password == correct_password:
            return True
    return False

def attempt_login():
    username = entry_username.get()
    if dictionary_attack(username):
        messagebox.showinfo("Success", "Password found in dictionary!")
    else:
        if brute_force_attack():
            messagebox.showinfo("Success", "Password found using brute force!")
        else:
            messagebox.showerror("Failure", "Failed to find password.")

# GUI setup
root = tk.Tk()
root.title("Password Cracker")

label_username = tk.Label(root, text="Enter your username:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

button_login = tk.Button(root, text="Attempt Login", command=attempt_login)
button_login.pack()

root.mainloop()