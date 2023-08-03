import pymysql
import tkinter as tk
from tkinter import ttk
from win10toast import ToastNotifier
from tkinter import messagebox

# PEQUEÑA INTERFAZ
root1 = tk.Tk()
root1.geometry("200x200+600+300")
root1.title("Conexión")
# PIDE LOS DATOS
host = tk.Label(root1, text="host")
host.pack(fill=tk.BOTH, expand=True)
host_entry = tk.Entry()
host_entry.pack()
port = tk.Label(root1, text="puerto")
port.pack(fill=tk.BOTH, expand=True)
port_entry = tk.Entry()
port_entry.pack()
user = tk.Label(root1, text="usuario")
user.pack(fill=tk.BOTH, expand=True)
user_entry = tk.Entry()
user_entry.pack()
password = tk.Label(root1, text="constraseña")
password.pack(fill=tk.BOTH, expand=True)
password_entry = tk.Entry()
password_entry.pack()
db = tk.Label(root1, text="base de datos")
db.pack(fill=tk.BOTH, expand=True)
db_entry = tk.Entry()
db_entry.pack()


def destroy():
    try:
        # Intentar establecer la conexión
        connection = pymysql.connect(
            host=host_entry.get(),
            port=int(port_entry.get()),
            user=user_entry.get(),
            passwd=password_entry.get(),
            db=db_entry.get(),
        )
        toaster = ToastNotifier()
        toaster.show_toast(
            "Conexión exitosa",
            f"Base de datos: '{db_entry.get()}'",
            duration=10,
            threaded=True,
            icon_path=None,
        )
        connection.close()
        root1.destroy()
    except pymysql.Error as error:
        # Mostrar un mensaje de error
        messagebox.showerror(
            "Error", f"No se pudo conectar a la base de datos: {error}"
        )


button = tk.Button(root1, text="ok", command=destroy, activebackground="#fdbce1")
button.place(x=175, y=18)
root1.mainloop()
