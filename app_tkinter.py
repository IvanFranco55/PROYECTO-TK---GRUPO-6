import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from logica_supermercado import Producto, Cliente, Supermercado, crear_supermercado 


class AppSupermercado:
    
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Supermercado MARIANTECH - Gestión Estética ✨") 
        self.root.geometry("980x680") 
        self.root.config(bg="#EBEBEB") 
        self.root.resizable(False, False)

        self.mi_super = crear_supermercado()
        
        
        style = ttk.Style()
        style.theme_use('clam') 

        style.configure('Accent.TButton', font=('Arial', 12, 'bold'), foreground='white', background='#28A745', borderwidth=0)
        style.map('Accent.TButton', background=[('active', '#1E7E34')])
        
        style.configure('TLabelFrame', bordercolor='#CCCCCC', background='#F8F8F8') 
        style.configure('TLabelframe.Label', font=('Arial', 12, 'bold'), foreground='#333333') 
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=15, padx=15, fill="both", expand=True)

        self.crear_pestana_productos()
        self.crear_pestana_clientes()
        self.crear_pestana_ventas()

        self.mi_super.registrar_cliente(Cliente("Ivan Franco"))
        self.mi_super.registrar_cliente(Cliente("Roberto Fernandez"))
        self.mi_super.registrar_cliente(Cliente("Mariano Insaurralde"))
        self.mi_super.registrar_cliente(Cliente("Francisco Sosa"))
        self.mi_super.registrar_cliente(Cliente("Maximiliano Castañon"))
        self.mi_super.registrar_cliente(Cliente("Gonzalo Vallejos"))
        self.mi_super.registrar_cliente(Cliente("Elio Segura"))
        self.actualizar_combobox_clientes()


    def crear_pestana_productos(self):
        self.frame_productos = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(self.frame_productos, text="📦 Gestión de Productos")
        
        frame_agregar = ttk.LabelFrame(self.frame_productos, text="✍️ Nuevo Producto", padding="20")
        frame_agregar.pack(fill=tk.X, pady=15)

        ttk.Label(frame_agregar, text="Nombre:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_nombre = ttk.Entry(frame_agregar, width=30)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_agregar, text="Precio:", font=('Arial', 10, 'bold')).grid(row=0, column=2, sticky=tk.W, padx=20, pady=5)
        self.entry_precio = ttk.Entry(frame_agregar, width=15)
        self.entry_precio.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_agregar, text="Categoría:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_categoria = ttk.Entry(frame_agregar, width=30)
        self.entry_categoria.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_agregar, text="Stock:", font=('Arial', 10, 'bold')).grid(row=1, column=2, sticky=tk.W, padx=20, pady=5)
        self.entry_stock = ttk.Entry(frame_agregar, width=15)
        self.entry_stock.grid(row=1, column=3, padx=5, pady=5)

        btn_agregar = ttk.Button(frame_agregar, text="➕ Agregar Producto", command=self.agregar_producto_tk)
        btn_agregar.grid(row=2, column=0, columnspan=4, pady=20)

        frame_lista = ttk.LabelFrame(self.frame_productos, text="📋 Inventario Actual", padding="15")
        frame_lista.pack(fill=tk.BOTH, expand=True, pady=15)

        scrollbar = ttk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.lista_productos_widget = tk.Text(frame_lista, height=15, yscrollcommand=scrollbar.set, font=("Consolas", 10), bg="#FFFFFF") 
        self.lista_productos_widget.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lista_productos_widget.yview)

        self.actualizar_lista_productos()

    def crear_pestana_clientes(self):
        self.frame_clientes = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(self.frame_clientes, text="👥 Registro de Clientes")

        frame_registro = ttk.LabelFrame(self.frame_clientes, text="📝 Registrar Nuevo Cliente", padding="20")
        frame_registro.pack(pady=40, padx=120)

        ttk.Label(frame_registro, text="Nombre del Cliente:", font=('Arial', 11, 'bold')).grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.entry_cliente_nombre = ttk.Entry(frame_registro, width=40)
        self.entry_cliente_nombre.grid(row=0, column=1, padx=10, pady=10)

        btn_registrar = ttk.Button(frame_registro, text="✅ Registrar Cliente", command=self.registrar_cliente_tk)
        btn_registrar.grid(row=1, column=0, columnspan=2, pady=20)
        
        ttk.Label(self.frame_clientes, text="Clientes Registrados:", font=('Arial', 11, 'bold', 'underline')).pack(pady=(30, 10))
        self.lista_clientes_widget = tk.Listbox(self.frame_clientes, height=10, width=50, font=("Arial", 10), bg="#FFFFFF")
        self.lista_clientes_widget.pack(pady=5)
        self.actualizar_lista_clientes()


    def crear_pestana_ventas(self):
        self.frame_ventas = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(self.frame_ventas, text="💳 Realizar Compra")

        frame_cliente = ttk.LabelFrame(self.frame_ventas, text="👤 1. Seleccionar Cliente", padding="15")
        frame_cliente.pack(fill=tk.X, pady=10)
        ttk.Label(frame_cliente, text="Cliente:", font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=10)
        self.cliente_seleccionado = tk.StringVar()
        self.combo_clientes = ttk.Combobox(frame_cliente, textvariable=self.cliente_seleccionado, state="readonly", width=30)
        self.combo_clientes.pack(side=tk.LEFT, padx=15)
        self.combo_clientes.bind("<<ComboboxSelected>>", self.mostrar_carrito_actual)

        frame_carrito = ttk.LabelFrame(self.frame_ventas, text="🛒 2. Añadir al Carrito", padding="15")
        frame_carrito.pack(fill=tk.X, pady=10)
        
        ttk.Label(frame_carrito, text="Producto:", font=('Arial', 10, 'bold')).grid(row=0, column=0, padx=10)
        self.prod_carrito_seleccionado = tk.StringVar()
        self.combo_productos_carrito = ttk.Combobox(frame_carrito, textvariable=self.prod_carrito_seleccionado, state="readonly", width=30)
        self.combo_productos_carrito.grid(row=0, column=1, padx=5)
        self.actualizar_combobox_productos()
        
        ttk.Label(frame_carrito, text="Cantidad:", font=('Arial', 10, 'bold')).grid(row=0, column=2, padx=20)
        self.entry_cantidad_carrito = ttk.Entry(frame_carrito, width=10)
        self.entry_cantidad_carrito.grid(row=0, column=3, padx=5)
        self.entry_cantidad_carrito.insert(0, "1")
        
        btn_agregar_carrito = ttk.Button(frame_carrito, text="➕ Agregar al Carrito", command=self.agregar_a_carrito_tk)
        btn_agregar_carrito.grid(row=0, column=4, padx=20)

        frame_resumen = ttk.LabelFrame(self.frame_ventas, text="💰 3. Resumen y Pago", padding="15")
        frame_resumen.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.carrito_widget = tk.Listbox(frame_resumen, height=8, font=("Arial", 10), bg="#FFFFFF")
        self.carrito_widget.pack(fill=tk.X, padx=10)
        
        frame_controles = ttk.Frame(frame_resumen)
        frame_controles.pack(pady=20)

        btn_vaciar_carrito = ttk.Button(frame_controles, text="Vaciar Carrito", command=self.vaciar_carrito_tk)
        btn_vaciar_carrito.pack(side=tk.LEFT, padx=15)
        
        self.label_total = ttk.Label(frame_controles, text="TOTAL: $0.00", font=('Helvetica', 16, 'bold'), foreground='#D9534F') 
        self.label_total.pack(side=tk.LEFT, padx=30)
        
        btn_pagar = ttk.Button(frame_controles, text="💵 REALIZAR COMPRA (Pagar)", command=self.realizar_compra_tk, style='Accent.TButton')
        btn_pagar.pack(side=tk.LEFT, padx=15)


    def actualizar_lista_productos(self):
        self.lista_productos_widget.config(state=tk.NORMAL)
        self.lista_productos_widget.delete('1.0', tk.END)
        
        header = f"{'Nombre':<25} | {'Precio':>10} | {'Categoría':<15} | {'Stock':>5}\n"
        self.lista_productos_widget.insert(tk.END, header)
        self.lista_productos_widget.insert(tk.END, "="*60 + "\n")
        
        for producto in self.mi_super.productos.values():
            info = f"{producto.nombre:<25} | ${producto.precio:>9.2f} | {producto.categoria:<15} | {producto.stock:>5}\n"
            self.lista_productos_widget.insert(tk.END, info)
        
        self.lista_productos_widget.config(state=tk.DISABLED)

    def agregar_producto_tk(self):
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        categoria = self.entry_categoria.get()
        stock = self.entry_stock.get()
        
        if not all([nombre, precio, categoria, stock]):
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return
        try:
            precio_val = float(precio)
            stock_val = int(stock)
            if precio_val <= 0 or stock_val < 0: raise ValueError
        except ValueError:
            messagebox.showerror("Datos inválidos", "Precio y Stock deben ser números válidos y positivos.")
            return

        if self.mi_super.buscar_producto(nombre):
            messagebox.showwarning("Producto existente", f"El producto '{nombre}' ya existe.")
            return

        nuevo_prod = Producto(nombre, precio_val, categoria, stock_val)
        self.mi_super.productos[nuevo_prod.nombre] = nuevo_prod
        
        messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente.")
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)
        
        self.actualizar_lista_productos()
        self.actualizar_combobox_productos()

    def registrar_cliente_tk(self):
        nombre = self.entry_cliente_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "El nombre del cliente no puede estar vacío.")
            return
            
        nombres_existentes = [c.nombre for c in self.mi_super.clientes]
        if nombre in nombres_existentes:
            messagebox.showwarning("Error", f"El cliente '{nombre}' ya está registrado.")
            return

        nuevo_cliente = Cliente(nombre)
        self.mi_super.registrar_cliente(nuevo_cliente)
        
        messagebox.showinfo("Éxito", f"Cliente '{nombre}' registrado.")
        self.entry_cliente_nombre.delete(0, tk.END)
        
        self.actualizar_lista_clientes()
        self.actualizar_combobox_clientes()

    def actualizar_lista_clientes(self):
        self.lista_clientes_widget.delete(0, tk.END)
        for cliente in self.mi_super.clientes:
            self.lista_clientes_widget.insert(tk.END, cliente.nombre)

    def actualizar_combobox_clientes(self):
        nombres_clientes = [c.nombre for c in self.mi_super.clientes]
        self.combo_clientes['values'] = nombres_clientes
        if nombres_clientes and not self.cliente_seleccionado.get():
            self.cliente_seleccionado.set(nombres_clientes[0])
        self.mostrar_carrito_actual()

    def actualizar_combobox_productos(self):
        nombres_productos = list(self.mi_super.productos.keys())
        self.combo_productos_carrito['values'] = nombres_productos
        if nombres_productos and not self.prod_carrito_seleccionado.get():
             self.prod_carrito_seleccionado.set(nombres_productos[0])

    def obtener_cliente_actual(self):
        nombre_cliente = self.cliente_seleccionado.get()
        if not nombre_cliente: return None
        for cliente in self.mi_super.clientes:
            if cliente.nombre == nombre_cliente:
                return cliente
        return None

    def mostrar_carrito_actual(self, event=None):
        cliente = self.obtener_cliente_actual()
        self.carrito_widget.delete(0, tk.END)
        self.label_total.config(text="TOTAL: $0.00")
        
        if not cliente:
            self.carrito_widget.insert(tk.END, "Seleccione un cliente para ver su carrito.")
            return

        if not cliente.carrito:
            self.carrito_widget.insert(tk.END, "(Carrito vacío)")
            return

        total_estimado = 0
        for nombre_prod, cantidad in cliente.carrito.items():
            producto = self.mi_super.buscar_producto(nombre_prod)
            
            if producto:
                subtotal = producto.precio * cantidad
                total_estimado += subtotal
                linea = f"{nombre_prod:<20} (x{cantidad}) -> ${subtotal:.2f}"
            else:
                linea = f"{nombre_prod} (x{cantidad}) -> ¡No disponible!"
                
            self.carrito_widget.insert(tk.END, linea)
        
        self.label_total.config(text=f"TOTAL: ${total_estimado:.2f}")

    def agregar_a_carrito_tk(self):
        cliente = self.obtener_cliente_actual()
        nombre_prod = self.prod_carrito_seleccionado.get()
        cantidad_str = self.entry_cantidad_carrito.get()

        if not cliente or not nombre_prod:
            messagebox.showwarning("Advertencia", "Debe seleccionar un cliente y un producto.")
            return
            
        try:
            cantidad = int(cantidad_str)
            if cantidad <= 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida.")
            return

        producto = self.mi_super.buscar_producto(nombre_prod)
        if not producto:
             messagebox.showerror("Error", "Producto no encontrado.")
             return

        cliente.agregar_producto(producto, cantidad) 
        self.mostrar_carrito_actual()
        self.entry_cantidad_carrito.delete(0, tk.END)
        self.entry_cantidad_carrito.insert(0, "1")

    def vaciar_carrito_tk(self):
        cliente = self.obtener_cliente_actual()
        if not cliente or not cliente.carrito:
            messagebox.showinfo("Información", "El carrito ya está vacío o no hay cliente seleccionado.")
            return
            
        if messagebox.askyesno("Confirmar", f"¿Desea vaciar el carrito de {cliente.nombre}?"):
            cliente.vaciar_carrito()
            self.mostrar_carrito_actual()
            messagebox.showinfo("Éxito", "Carrito vaciado.")

    def realizar_compra_tk(self):
        cliente = self.obtener_cliente_actual()
        if not cliente or not cliente.carrito:
            messagebox.showwarning("Advertencia", "El carrito está vacío. No se puede realizar la compra.")
            return

        resultado_compra = self.mi_super.realizar_compra(cliente) 
        
        if isinstance(resultado_compra, (float, int)):
            messagebox.showinfo("¡COMPRA EXITOSA!", 
                                f"La compra de {cliente.nombre} se ha completado.\n"
                                f"Total final: ${resultado_compra:.2f}\n"
                                "Stock actualizado.")
            self.actualizar_lista_productos()
            self.mostrar_carrito_actual()
        else:
            messagebox.showerror("Error de Compra", "Hubo un problema al procesar la compra. Verifique el stock o el producto.")
            self.mostrar_carrito_actual()

if __name__ == "__main__": 
    try:
        root = tk.Tk()
        app = AppSupermercado(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error Fatal", f"Ocurrió un error al iniciar la aplicación:\n{e}\n\nAsegúrese de que el archivo 'logica_supermercado.py' esté en la misma carpeta.")