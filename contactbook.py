import tkinter as tk
from tkinter import messagebox

contacts = {}
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts[name] = phone
    messagebox.showinfo("Success", "Contact added!")
    clear_entries()

def view_contacts():
    contact_list.delete(0, tk.END)
    for n, p in contacts.items():
        contact_list.insert(tk.END, n + " | " + p)

def search_contact():
    name = name_entry.get()
    contact_list.delete(0, tk.END)

    if name in contacts:
        contact_list.insert(tk.END, name + " | " + contacts[name])
    else:
        messagebox.showerror("Not Found", "Contact not found!")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", "Contact deleted!")
        view_contacts()
        clear_entries()
    else:
        messagebox.showerror("Error", "No such contact")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")
root.geometry("480x320")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=35)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=35)
phone_entry.pack()

tk.Button(root, text="Add", command=add_contact).pack(pady=4)
tk.Button(root, text="View", command=view_contacts).pack(pady=4)
tk.Button(root, text="Search", command=search_contact).pack(pady=4)
tk.Button(root, text="Delete", command=delete_contact).pack(pady=4)

contact_list = tk.Listbox(root, width=55)
contact_list.pack(pady=8)

root.mainloop()
