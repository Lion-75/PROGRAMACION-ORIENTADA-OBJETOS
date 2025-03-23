import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


# Función para agregar un evento
def agregar_evento():
    fecha = date_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        date_entry.set_date("")
        hora_entry.delete(0, tk.END)
        descripcion_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos")


# Función para eliminar un evento seleccionado
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirmar = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?")
        if confirmar:
            tree.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")


# Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame para entrada de datos
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
hora_entry = tk.Entry(frame_entrada)
hora_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
descripcion_entry = tk.Entry(frame_entrada)
descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack()

tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).grid(row=0, column=0, padx=10, pady=10)
tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento).grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=10, pady=10)

# TreeView para mostrar eventos
frame_lista = tk.Frame(root)
frame_lista.pack()

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

tree.pack()

# Ejecutar aplicación
root.mainloop()
