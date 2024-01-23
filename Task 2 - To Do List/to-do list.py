import tkinter as tk
from tkinter import messagebox

def add_new_task():
    new_task = entry_new_task.get()
    if new_task:
        task_listbox.insert(tk.END, new_task)
        entry_new_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning!", "No task is entered")

def modify_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        previous_task_name = task_listbox.get(selected_task_index)
        new_task = entry_new_task.get()
        if new_task and previous_task_name != new_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            entry_new_task.delete(0, tk.END)
        elif previous_task_name == new_task:
            entry_new_task.delete(0, tk.END)
            messagebox.showwarning("Same Task", "Previous and present names are the same")
        else:
            messagebox.showwarning("Warning!", "The task name can't be empty")
    except IndexError:
        messagebox.showwarning("Warning!", "Nothing is selected to modify")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning!", "No task is selected")
main_window = tk.Tk()
main_window.title("# To-Do List App #")

main_window.geometry("400x400")
main_window.configure(bg="#E0E0E0")

frame_tasks = tk.Frame(main_window, bg="#E0E0E0")
frame_tasks.pack(pady=10)

task_listbox = tk.Listbox(frame_tasks, height=10, width=30, selectbackground="#FFD700", selectforeground="black", font=("Verdana", 12))
task_listbox.pack(side=tk.LEFT, ipady=10)

scrollbar = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)

entry_new_task = tk.Entry(main_window, width=30, font=("Verdana", 12))
entry_new_task.pack(pady=10)

buttons = [
    ("Add New Task", add_new_task, "#90EE90"),
    ("Remove Task", remove_task, "#FFA07A"),
    ("Modify Task", modify_task, "#DA70D6")
]

for btn_text, btn_command, btn_bg in buttons:
    button = tk.Button(main_window, text=btn_text, width=30, command=btn_command, bg=btn_bg, fg="black", font=("Verdana", 12))
    button.pack()

main_window.mainloop()
