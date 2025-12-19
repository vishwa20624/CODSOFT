import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Todo List with Checkboxes")
root.geometry("400x400")

tasks_frame = tk.Frame(root)
tasks_frame.pack(pady=10, fill="both", expand=True)

tasks = []

def add_task():
    t = task_entry.get()
    if t != "":
        var = tk.IntVar()
        chk = tk.Checkbutton(tasks_frame, text=t, variable=var)
        chk.pack(anchor="w")
        tasks.append((t, var, chk))
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops", "Type something first!")

def delete_task():
    to_delete = []
    for t, v, chk in tasks:
        if v.get() == 1:
            chk.destroy()
            to_delete.append((t, v, chk))
    for item in to_delete:
        tasks.remove(item)

def clear_all():
    for t, v, chk in tasks:
        chk.destroy()
    tasks.clear()

bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", pady=10)

entry_frame = tk.Frame(bottom_frame)
entry_frame.pack(pady=5)

task_entry = tk.Entry(entry_frame, width=25)
task_entry.pack(side="left", padx=5)

add_button = tk.Button(entry_frame, text="Add", command=add_task)
add_button.pack(side="left")

action_frame = tk.Frame(bottom_frame)
action_frame.pack(pady=5)

delete_button = tk.Button(action_frame, text="Delete Checked", command=delete_task)
delete_button.pack(side="left", padx=5)

clear_button = tk.Button(action_frame, text="Clear All", command=clear_all)
clear_button.pack(side="left", padx=5)

root.mainloop()
