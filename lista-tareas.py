import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"{task} (Completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Crear y ubicar widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, selectmode=tk.SINGLE)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10, padx=10)

button_add = tk.Button(root, text="Añadir Tarea", command=add_task)
button_add.pack(pady=5)

button_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
button_delete.pack(pady=5)

button_complete = tk.Button(root, text="Marcar como Completada", command=mark_completed)
button_complete.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
