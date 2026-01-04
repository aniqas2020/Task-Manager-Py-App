import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return [line.strip().split("|") for line in f.readlines()]

def save_tasks():
    with open(FILE_NAME, "w") as f:
        for task, done in tasks:
            f.write(f"{task}|{done}\n")

def refresh_listbox():
    listbox.delete(0, tk.END)
    for task, done in tasks:
        status = "✓" if done == "True" else " "
        listbox.insert(tk.END, f"[{status}] {task}")

def add_task():
    task = entry.get().strip()
    if not task:
        messagebox.showwarning("Warning", "Task cannot be empty")
        return
    tasks.append([task, "False"])
    entry.delete(0, tk.END)
    save_tasks()
    refresh_listbox()

def complete_task():
    try:
        index = listbox.curselection()[0]
        tasks[index][1] = "True"
        save_tasks()
        refresh_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first")

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        save_tasks()
        refresh_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first")

# --- GUI Setup ---
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

tasks = load_tasks()

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack()

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

complete_button = tk.Button(root, text="Mark as Completed", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

refresh_listbox()
root.mainloop()
