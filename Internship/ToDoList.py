import tkinter as tk

# Function to add a new task to the list
def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

# Function to remove a selected task from the list
def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget for entering tasks
entry = tk.Entry(root, width=30)
entry.pack()

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create a listbox to display the tasks
task_list = tk.Listbox(root, width=40)
task_list.pack()

# Create a button to remove selected tasks
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

root.mainloop()
