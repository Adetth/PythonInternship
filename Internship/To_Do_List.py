import tkinter as tk

root = tk.Tk()
root.configure(bg='darkgreen')

def add_entry(event):
    event = entry.get()
    if event:
        listbox.insert(tk.END,event)
        entry.delete(0,tk.END)

def del_entry():
    sel = listbox.curselection()
    if sel:
        listbox.delete(sel)

label = tk.Label(root,text="To-Do-List",pady=10,bg="darkgreen",font=("Helvetica", 16))
entry = tk.Entry(root,width=30)
add_button = tk.Button(root,text="Add",command=add_entry)
listbox = tk.Listbox(width=30)
del_button = tk.Button(root,text="Delete",command=del_entry)

label.pack()
entry.pack()
add_button.pack()
listbox.pack()
del_button.pack()

entry.bind("<Return>",func=add_entry)
listbox.bind("<Delete>",func=del_entry)

root.title("To-Do-List")
root.geometry("275x300")

root.mainloop()