from tkinter import *
from tkinter import ttk

class InventarioApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Inventario")
        self.usuario_actual = None
        self.inventario = []
        self.status_text = "Usuario no registrado."

        self.status_label = Label(self.master, text=self.status_text, bd=1, relief=SUNKEN, anchor=W)
        self.status_label.pack(side=BOTTOM, fill=X)

        self.login_frame = Frame(self.master)
        self.login_frame.pack()

        self.registrar_usuario_btn = Button(self.login_frame, text="Registrar Usuario", command=self.registrar_usuario)
        self.registrar_usuario_btn.pack(fill=X)

        self.iniciar_sesion_btn = Button(self.login_frame, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.iniciar_sesion_btn.pack(fill=X)

    def registrar_usuario(self):
        self.login_frame.destroy()

        registro_frame = Frame(self.master)
        registro_frame.pack()

        usuario_label = Label(registro_frame, text="Nombre de Usuario:")
        usuario_label.grid(row=0, column=0, padx=5, pady=5)
        usuario_entry = Entry(registro_frame)
        usuario_entry.grid(row=0, column=1, padx=5, pady=5)

        registrar_btn = Button(registro_frame, text="Registrar", command=lambda: self.registrar_confirmado(usuario_entry.get(), registro_frame))
        registrar_btn.grid(row=1, columnspan=2, padx=5, pady=5)

    def registrar_confirmado(self, nombre_usuario, registro_frame):
        if nombre_usuario:
            self.usuario_actual = nombre_usuario
            self.status_text = f"Usuario registrado: {self.usuario_actual}"
            self.actualizar_status_label()
            print("Usuario registrado con éxito.")
            registro_frame.destroy()
        else:
            print("Error: Por favor ingrese un nombre de usuario válido.")

    def iniciar_sesion(self):
        self.login_frame.destroy()

        inicio_sesion_frame = Frame(self.master)
        inicio_sesion_frame.pack()

        usuario_label = Label(inicio_sesion_frame, text="Nombre de Usuario:")
        usuario_label.grid(row=0, column=0, padx=5, pady=5)
        usuario_entry = Entry(inicio_sesion_frame)
        usuario_entry.grid(row=0, column=1, padx=5, pady=5)

        iniciar_btn = Button(inicio_sesion_frame, text="Iniciar", command=lambda: self.iniciar_sesion_confirmado(usuario_entry.get(), inicio_sesion_frame))
        iniciar_btn.grid(row=1, columnspan=2, padx=5, pady=5)

    def iniciar_sesion_confirmado(self, nombre_usuario, inicio_sesion_frame):
        if nombre_usuario == self.usuario_actual:
            self.status_text = f"Usuario registrado: {self.usuario_actual}"
            self.actualizar_status_label()
            print("Sesión iniciada con éxito.")
            inicio_sesion_frame.destroy()
        else:
            print("Error: Nombre de usuario incorrecto.")

    def mostrar_menu_principal(self):
        self.inventario_frame = Frame(self.master)
        self.inventario_frame.pack()

        agregar_producto_btn = Button(self.inventario_frame, text="Agregar Producto", command=self.mostrar_ventana_agregar_producto)
        agregar_producto_btn.pack(fill=X)

        actualizar_cantidad_btn = Button(self.inventario_frame, text="Actualizar Cantidad", command=self.mostrar_ventana_actualizar_cantidad)
        actualizar_cantidad_btn.pack(fill=X)

        eliminar_producto_btn = Button(self.inventario_frame, text="Eliminar Producto", command=self.mostrar_ventana_eliminar_producto)
        eliminar_producto_btn.pack(fill=X)

        ver_inventario_btn = Button(self.inventario_frame, text="Ver Inventario", command=self.mostrar_inventario)
        ver_inventario_btn.pack(fill=X)

        cerrar_sesion_btn = Button(self.inventario_frame, text="Cerrar Sesión", command=self.cerrar_sesion)
        cerrar_sesion_btn.pack(fill=X)

    def mostrar_ventana_agregar_producto(self):
        if self.usuario_actual:
            ventana_agregar = Toplevel(self.master)
            ventana_agregar.title("Agregar Producto")

            id_producto_label = Label(ventana_agregar, text="ID del Producto:")
            id_producto_label.grid(row=0, column=0, padx=5, pady=5)
            id_producto_entry = Entry(ventana_agregar)
            id_producto_entry.grid(row=0, column=1, padx=5, pady=5)

            nombre_producto_label = Label(ventana_agregar, text="Nombre del Producto:")
            nombre_producto_label.grid(row=1, column=0, padx=5, pady=5)
            nombre_producto_entry = Entry(ventana_agregar)
            nombre_producto_entry.grid(row=1, column=1, padx=5, pady=5)

            categoria_producto_label = Label(ventana_agregar, text="Categoría del Producto:")
            categoria_producto_label.grid(row=2, column=0, padx=5, pady=5)
            categoria_producto_entry = Entry(ventana_agregar)
            categoria_producto_entry.grid(row=2, column=1, padx=5, pady=5)

            cantidad_producto_label = Label(ventana_agregar, text="Cantidad del Producto:")
            cantidad_producto_label.grid(row=3, column=0, padx=5, pady=5)
            cantidad_producto_entry = Entry(ventana_agregar)
            cantidad_producto_entry.grid(row=3, column=1, padx=5, pady=5)

            agregar_btn = Button(ventana_agregar, text="Agregar", command=lambda: self.agregar_producto_confirmado(id_producto_entry.get(),
                                                                                                                nombre_producto_entry.get(),
                                                                                                                categoria_producto_entry.get(),
                                                                                                                cantidad_producto_entry.get(),
                                                                                                                ventana_agregar))
            agregar_btn.grid(row=4, columnspan=2, padx=5, pady=5)

        else:
            print("Error: Debe iniciar sesión o registrar un usuario antes de agregar productos.")

    def agregar_producto_confirmado(self, id_producto, nombre_producto, categoria_producto, cantidad_producto, ventana_agregar):
        if id_producto and nombre_producto and categoria_producto and cantidad_producto:
            producto = {"ID": id_producto, "Nombre": nombre_producto, "Categoría": categoria_producto, "Cantidad": cantidad_producto}
            self.inventario.append(producto)
            self.actualizar_status_label()
            print("Producto agregado con éxito.")
            ventana_agregar.destroy()
        else:
            print("Error: Por favor complete todos los campos antes de agregar el producto.")

    def mostrar_ventana_actualizar_cantidad(self):
        if self.usuario_actual:
            ventana_actualizar = Toplevel(self.master)
            ventana_actualizar.title("Actualizar Cantidad")

            id_producto_label = Label(ventana_actualizar, text="Seleccione el ID del Producto:")
            id_producto_label.grid(row=0, column=0, padx=5, pady=5)

            id_producto_combobox = ttk.Combobox(ventana_actualizar, values=[producto["ID"] for producto in self.inventario])
            id_producto_combobox.grid(row=0, column=1, padx=5, pady=5)

            cantidad_actual_label = Label(ventana_actualizar, text="Cantidad Actual:")
            cantidad_actual_label.grid(row=1, column=0, padx=5, pady=5)

            cantidad_actual_entry = Entry(ventana_actualizar, state="readonly")
            cantidad_actual_entry.grid(row=1, column=1, padx=5, pady=5)

            def seleccionar_producto(event):
                selected_id = id_producto_combobox.get()
                selected_product = next((p for p in self.inventario if p["ID"] == selected_id), None)
                if selected_product:
                    cantidad_actual_entry.config(state="normal")
                    cantidad_actual_entry.delete(0, END)
                    cantidad_actual_entry.insert(0, selected_product["Cantidad"])
                    cantidad_actual_entry.config(state="readonly")

            id_producto_combobox.bind("<<ComboboxSelected>>", seleccionar_producto)

            cantidad_nueva_label = Label(ventana_actualizar, text="Cantidad Nueva:")
            cantidad_nueva_label.grid(row=2, column=0, padx=5, pady=5)

            cantidad_nueva_entry = Entry(ventana_actualizar)
            cantidad_nueva_entry.grid(row=2, column=1, padx=5, pady=5)

            actualizar_btn = Button(ventana_actualizar, text="Actualizar",
                                    command=lambda: self.actualizar_cantidad_confirmado(id_producto_combobox.get(),
                                                                                         cantidad_nueva_entry.get(),
                                                                                         ventana_actualizar))
            actualizar_btn.grid(row=3, columnspan=2, padx=5, pady=5)

        else:
            print("Error: Debe iniciar sesión o registrar un usuario antes de actualizar la cantidad.")

    def actualizar_cantidad_confirmado(self, id_producto, cantidad_nueva, ventana_actualizar):
        if id_producto and cantidad_nueva:
            for producto in self.inventario:
                if producto["ID"] == id_producto:
                    producto["Cantidad"] = cantidad_nueva
                    self.actualizar_status_label()
                    print("Cantidad actualizada con éxito.")
                    ventana_actualizar.destroy()
                    return
            print("Error: El ID del producto no existe.")
        else:
            print("Error: Por favor seleccione un ID de producto y complete la cantidad nueva.")

    def mostrar_ventana_eliminar_producto(self):
        if self.usuario_actual:
            ventana_eliminar = Toplevel(self.master)
            ventana_eliminar.title("Eliminar Producto")

            id_producto_label = Label(ventana_eliminar, text="Seleccione el ID del Producto:")
            id_producto_label.grid(row=0, column=0, padx=5, pady=5)

            id_producto_combobox = ttk.Combobox(ventana_eliminar, values=[producto["ID"] for producto in self.inventario])
            id_producto_combobox.grid(row=0, column=1, padx=5, pady=5)

            eliminar_btn = Button(ventana_eliminar, text="Eliminar",
                                  command=lambda: self.eliminar_producto_confirmado(id_producto_combobox.get(),
                                                                                      ventana_eliminar))
            eliminar_btn.grid(row=1, columnspan=2, padx=5, pady=5)

        else:
            print("Error: Debe iniciar sesión o registrar un usuario antes de eliminar productos.")

    def eliminar_producto_confirmado(self, id_producto, ventana_eliminar):
        if id_producto:
            for producto in self.inventario:
                if producto["ID"] == id_producto:
                    self.inventario.remove(producto)
                    self.actualizar_status_label()
                    print("Producto eliminado con éxito.")
                    ventana_eliminar.destroy()
                    return
            print("Error: El ID del producto no existe.")
        else:
            print("Error: Por favor seleccione un ID de producto.")

    def mostrar_inventario(self):
        if self.usuario_actual:
            inventario_window = Toplevel(self.master)
            inventario_window.title("Inventario")

            scrollbar = Scrollbar(inventario_window)
            scrollbar.pack(side=RIGHT, fill=Y)

            tree = ttk.Treeview(inventario_window, yscrollcommand=scrollbar.set)
            tree.pack()

            scrollbar.config(command=tree.yview)

            tree["columns"] = ("ID", "Nombre", "Categoría", "Cantidad")
            tree.column("#0", width=0, stretch=NO)
            tree.column("ID", anchor=CENTER, width=80)
            tree.column("Nombre", anchor=W, width=150)
            tree.column("Categoría", anchor=W, width=100)
            tree.column("Cantidad", anchor=CENTER, width=80)

            tree.heading("#0", text="", anchor=CENTER)
            tree.heading("ID", text="ID", anchor=CENTER)
            tree.heading("Nombre", text="Nombre", anchor=W)
            tree.heading("Categoría", text="Categoría", anchor=W)
            tree.heading("Cantidad", text="Cantidad", anchor=CENTER)

            for producto in self.inventario:
                tree.insert(parent='', index='end', values=(producto["ID"], producto["Nombre"], producto["Categoría"], producto["Cantidad"]))

        else:
            print("Error: Debe iniciar sesión o registrar un usuario antes de ver el inventario.")

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.status_text = "Usuario no registrado."
        self.actualizar_status_label()

        self.inventario_frame.destroy()
        self.mostrar_menu_principal()

    def actualizar_status_label(self):
        self.status_label.config(text=self.status_text)

if __name__ == "__main__":
    root = Tk()
    app = InventarioApp(root)
    app.actualizar_status_label()
    app.mostrar_menu_principal()
    root.mainloop()
