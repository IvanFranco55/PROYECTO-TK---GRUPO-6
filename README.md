# 🛍️ Proyecto: Supermercado Virtual MARIANTECH

Este proyecto es un **Sistema de Gestión de Supermercado** desarrollado en Python, utilizando la librería estándar **Tkinter** para la interfaz gráfica de usuario (GUI). Se enfoca en aplicar los principios de la **Programación Orientada a Objetos (POO)** y la separación clara de responsabilidades entre la lógica del negocio (Backend) y la presentación (Frontend).

## 📝 Descripción del Sistema y Funcionalidades

El sistema permite gestionar un inventario de productos, registrar clientes y procesar transacciones de compra. Toda la lógica del negocio se encuentra encapsulada en la clase `Supermercado` y sus componentes relacionados (`Producto`, `Cliente`).

La aplicación se estructura en tres pestañas principales:

| Pestaña | Propósito Principal | Lógica (Backend) Aplicada |
| :--- | :--- | :--- |
| **📦 Gestión de Productos** | Permite registrar nuevos productos, especificando nombre, precio, categoría y stock. | Utiliza la clase `Producto` para crear y almacenar objetos con sus atributos. |
| **👥 Registro de Clientes** | Permite añadir nuevos clientes al sistema del supermercado. | Utiliza la clase `Cliente` y la añade a una lista gestionada por la clase `Supermercado`. |
| **💳 Realizar Compra** | Procesa la venta, gestionando el carrito y validando el stock. | **1. Lógica Iterativa:** Recorre el carrito de compras (diccionario) del cliente. **2. Lógica Condicional:** En cada paso, valida si hay suficiente `stock` (`if producto.stock < cantidad`) antes de procesar la venta. **3. Actualiza Datos:** Llama a `Producto.actualizar_stock()` para decrementar el inventario de la clase `Producto`. |

---

## 🚀 Cómo Correr el Proyecto (Instrucciones de Ejecución)

El proyecto requiere únicamente la instalación estándar de Python, ya que utiliza la librería Tkinter, que viene incluida por defecto.

### 1. Requisitos

Asegúrate de tener **Python 3.x** instalado en tu sistema.

### 2. Estructura de Archivos

Los dos archivos principales deben estar ubicados en la **misma carpeta**:

| Archivo | Contenido |
| :--- | :--- |
| `logica_supermercado.py` | **Lógica del Negocio (POO / Backend):** Clases `Producto`, `Cliente`, `Supermercado`. |
| `app_tkinter.py` | **Interfaz Gráfica (Tkinter / Frontend):** Clase `AppSupermercado`. |

### 3. Pasos de Ejecución

1.  Abre tu terminal (o Símbolo del Sistema / PowerShell).
2.  Navega al directorio donde guardaste los archivos:

    ```bash
    cd /ruta/al/directorio/del/proyecto
    ```

3.  Ejecuta el archivo de la interfaz gráfica usando el intérprete de Python:

    ```bash
    python app_tkinter.py
    ```

La aplicación se iniciará inmediatamente en una ventana de escritorio.