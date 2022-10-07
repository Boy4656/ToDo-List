from tkinter import *
from tkinter import messagebox

if __name__ == '__main__':
    root = Tk()
    root.title("To-Do List")

    def add_task():
        task = entry_task.get()
        if task != "":
            listbox_tasks.insert(END, task)
            entry_task.delete(0, END)
        else:
            messagebox.showwarning(
                title="Warning!", message="You must enter a task!")

    frame_tasks = Frame(root)
    frame_tasks.pack()

    listbox_tasks = Listbox(frame_tasks, height=8, width=50)
    listbox_tasks.pack(side=LEFT)

    scrollbar_task = Scrollbar(frame_tasks)
    scrollbar_task.pack(side=LEFT, fill=Y)
    listbox_tasks.config(yscrollcommand=scrollbar_task.set)
    scrollbar_task.config(command=listbox_tasks.yview)

    entry_task = Entry(frame_tasks, width=50)
    entry_task.pack(side=BOTTOM)

    button_add_task = Button(root, text="Add task", width=48, command=add_task)
    button_add_task.pack(side=RIGHT)

    root.mainloop()
