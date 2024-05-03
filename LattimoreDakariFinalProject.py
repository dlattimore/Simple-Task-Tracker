import tkinter as tk
from tkinter import messagebox

class SimpleTaskTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Task Tracker")
        
        self.tasks = []
        
        self.create_menu()
        self.create_task_list_display_area()
        self.create_task_management_buttons()
        self.create_sorting_and_filtering_options()
        self.create_status_bar()
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Task", command=self.add_task)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about_dialog)
        help_menu.add_command(label="Help")
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def create_task_list_display_area(self):
        self.task_listbox = tk.Listbox(self.root, height=10, width=50)
        self.task_listbox.pack(pady=10)
    
    def create_task_management_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()
        
        add_btn = tk.Button(btn_frame, text="Add Task", command=self.add_task)
        add_btn.grid(row=0, column=0, padx=5)
        
        edit_btn = tk.Button(btn_frame, text="Edit Task", command=self.edit_task)
        edit_btn.grid(row=0, column=1, padx=5)
        
        del_btn = tk.Button(btn_frame, text="Delete Task", command=self.delete_task)
        del_btn.grid(row=0, column=2, padx=5)
        
        mark_btn = tk.Button(btn_frame, text="Mark as Completed", command=self.mark_task_completed)
        mark_btn.grid(row=0, column=3, padx=5)
    
    def create_sorting_and_filtering_options(self):
        options_frame = tk.Frame(self.root)
        options_frame.pack()
        
        sort_label = tk.Label(options_frame, text="Sort by:")
        sort_label.grid(row=0, column=0, padx=5)
        
        filter_label = tk.Label(options_frame, text="Filter:")
        filter_label.grid(row=0, column=1, padx=5)
    
    def create_status_bar(self):
        self.status_bar = tk.Label(self.root, text="Total Tasks: 0")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def add_task(self):
        add_dialog = tk.Toplevel()
        add_dialog.title("Add New Task")
        
        title_label = tk.Label(add_dialog, text="Task Title:")
        title_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.title_entry = tk.Entry(add_dialog)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        
        desc_label = tk.Label(add_dialog, text="Task Description:")
        desc_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.desc_entry = tk.Entry(add_dialog)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)
        
        add_btn = tk.Button(add_dialog, text="Add", command=self.save_task)
        add_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        cancel_btn = tk.Button(add_dialog, text="Cancel", command=add_dialog.destroy)
        cancel_btn.grid(row=2, column=1, columnspan=2, pady=10, padx=5)
    
    def save_task(self):
        title = self.title_entry.get()
        desc = self.desc_entry.get()
        self.tasks.append((title, desc))
        self.task_listbox.insert(tk.END, title)
        self.update_status_bar()
        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
    
    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            selected_task_title = self.task_listbox.get(selected_task_index)
            edit_dialog = tk.Toplevel()
            edit_dialog.title("Edit Task")
            title_label = tk.Label(edit_dialog, text="Task Title:")
            title_label.grid(row=0, column=0, padx=5, pady=5)
            self.edit_title_entry = tk.Entry(edit_dialog)
            self.edit_title_entry.insert(tk.END, selected_task_title)
            self.edit_title_entry.grid(row=0, column=1, padx=5, pady=5)
            desc_label = tk.Label(edit_dialog, text="Task Description:")
            desc_label.grid(row=1, column=0, padx=5, pady=5)
            self.edit_desc_entry = tk.Entry(edit_dialog)
            self.edit_desc_entry.grid(row=1, column=1, padx=5, pady=5)
            save_btn = tk.Button(edit_dialog, text="Save Changes", command=lambda: self.update_task(selected_task_index))
            save_btn.grid(row=2, column=0, columnspan=2, pady=10)
            cancel_btn = tk.Button(edit_dialog, text="Cancel", command=edit_dialog.destroy)
            cancel_btn.grid(row=2, column=1, columnspan=2, pady=10, padx=5)
    
    def update_task(self, index):
        new_title = self.edit_title_entry.get()
        new_desc = self.edit_desc_entry.get()
        self.tasks[index] = (new_title, new_desc)
        self.task_listbox.delete(index)
        self.task_listbox.insert(index, new_title)
        self.update_status_bar()
        self.edit_title_entry.delete(0, tk.END)
        self.edit_desc_entry.delete(0, tk.END)
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this task?")
            if confirmation:
                index = selected_task_index[0]
                self.task_listbox.delete(index)
                del self.tasks[index]
                self.update_status_bar()
    
    def mark_task_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            task_title = self.task_listbox.get(index)
            self.task_listbox.itemconfig(index, {'bg': 'light gray', 'fg': 'gray'})
            self.task_listbox.selection_clear(index)
    
    def update_status_bar(self):
        total_tasks = len(self.tasks)
        self.status_bar.config(text=f"Total Tasks: {total_tasks}")
    
    def show_about_dialog(self):
        about_dialog = tk.Toplevel()
        about_dialog.title("About Simple Task Tracker")
        about_text = "Simple Task Tracker\nVersion 1.0\n\nThis application was created to help users manage their daily tasks efficiently."
        about_label = tk.Label(about_dialog, text=about_text)
        about_label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTaskTracker(root)
    root.mainloop()
