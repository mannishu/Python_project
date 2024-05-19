import tkinter as tk
from tkinter import *


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        # Add a 'completed' attribute for each task (initially False)
        task_listbox.insert(tk.END, False)  # Index corresponds to task 



def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)


def mark_completed():
    selected_task_index = task_listbox.curselection()

    if not selected_task_index:
        message = tk.messagebox.showerror("Error", "Please select a task to mark complete.")
        return

    # Toggle the 'completed' attribute based on current state
    completed_status = task_listbox.get(selected_task_index[0] + 1)  # Get status from next index
    task_listbox.delete(selected_task_index[0] + 1)  # Remove status entry
    task_listbox.insert(selected_task_index[0] + 1, not completed_status)  # Insert negated status

    # Optionally, update listbox appearance based on completion status (e.g., strikethrough font)


root = tk.Tk()
root.title("To-Do List")
root.config(bg='#051622')
root.geometry("600x500")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

task_listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
task_listbox.pack(pady=10)
scrollbar.config(command=task_listbox.yview)

task_entry = tk.Entry(root)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, background="#DEB992")

remove_button = tk.Button(root, text="Remove Task", command=remove_task, background="#DEB992")
mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed, background="#DEB992")

add_button.pack()

task_update = tk.Entry(root)
task_update.pack(pady=5)
remove_button.pack()
mark_completed_button.pack(pady=5)

root.mainloop()
