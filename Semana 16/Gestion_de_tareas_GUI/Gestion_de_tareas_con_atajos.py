import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        self.task_list = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack()

        self.add_btn = tk.Button(self.btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(self.btn_frame, text="Marcar como Completada", command=self.mark_completed)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(self.btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Bind de atajos de teclado
        self.entry.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.mark_completed())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_list.append({"text": task, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingresa una tarea.")

    def mark_completed(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.task_list[index]["completed"] = not self.task_list[index]["completed"]
            self.update_listbox()

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.task_list[index]
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.task_list:
            display_text = f"[✔] {task['text']}" if task["completed"] else f"[ ] {task['text']}"
            self.listbox.insert(tk.END, display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
