class Producto:
    def __init__(self, nombre, precio, categoria, stock):
        self.nombre = nombre
        self.precio = float(precio)
        self.categoria = categoria
        self.stock = int(stock)

    def mostrar_info(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Categoría: {self.categoria} | Stock: {self.stock}"
    def actualizar_stock(self, cantidad):
        self.stock += int(cantidad)
    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje <= 100:
            self.precio *= (1 - porcentaje / 100)

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = {} 

    def agregar_producto(self, producto, cantidad):
        if cantidad <= 0:
            return
        nombre_prod = producto.nombre
        if nombre_prod in self.carrito:
            self.carrito[nombre_prod] += cantidad
        else:
            self.carrito[nombre_prod] = cantidad

    def ver_carrito(self):
        pass 

    def vaciar_carrito(self):
        self.carrito.clear()

class Supermercado:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {} 
        self.clientes = []

    def mostrar_productos(self):
        pass

    def buscar_producto(self, nombre):
        return self.productos.get(nombre)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def realizar_compra(self, cliente):

        
        if not cliente.carrito:
            return False 

        stock_suficiente = True
        for nombre_prod, cantidad_deseada in cliente.carrito.items():
            producto = self.buscar_producto(nombre_prod)
            
            if not producto:
                print(f"ERROR: Producto '{nombre_prod}' no existe en el inventario.")
                return False
            
            if producto.stock < cantidad_deseada:
                print(f"ERROR: Stock insuficiente para '{nombre_prod}'. Solicitados: {cantidad_deseada}, Disponibles: {producto.stock}")
                return False

        total_compra = 0
        for nombre_prod, cantidad_comprada in cliente.carrito.items():
            producto = self.buscar_producto(nombre_prod)
            
            producto.actualizar_stock(-cantidad_comprada)
            
            subtotal = producto.precio * cantidad_comprada
            total_compra += subtotal
                
        cliente.vaciar_carrito()
        return total_compra 


def crear_supermercado():
    """Inicializa el supermercado con algunos productos."""
    super_vecino = Supermercado("El Vecino")
    
    p1 = Producto("Manzana", 150.50, "Frutas", 100)
    p2 = Producto("Leche Entera", 220.00, "Lácteos", 50)
    p3 = Producto("Pan Integral", 180.75, "Panadería", 30)
    p4 = Producto("Queso Duro", 800.00, "Lácteos", 20)
    p5 = Producto("Gaseosa Cola 2L", 300.00, "Bebidas", 40)
    
    productos_iniciales = [p1, p2, p3, p4, p5]
    for p in productos_iniciales:
        super_vecino.productos[p.nombre] = p
        
    return super_vecino

def mostrar_resumen(supermercado):
    """Muestra un resumen del inventario (función de requisito)."""
    pass