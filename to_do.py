import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40, font=("Helvetica", 14))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        add_button_style = {"bg": "#4CAF50", "fg": "white", "font": ("Helvetica", 12, "bold")}
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, **add_button_style)
        self.add_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        remove_button_style = {"bg": "#FF5733", "fg": "white", "font": ("Helvetica", 12, "bold")}
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, **remove_button_style)
        self.remove_button.grid(row=1, column=0, columnspan=2, pady=10)

        listbox_style = {"width": 50, "height": 10, "font": ("Helvetica", 12)}
        self.task_listbox = tk.Listbox(root, **listbox_style)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            removed_task = self.tasks.pop(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            messagebox.showinfo("Task Removed", f"'{removed_task}' task removed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
