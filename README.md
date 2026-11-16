# FrostBite - Backend 🧊

Sistema backend desarrollado en **Python**, **Django** y **Django REST Framework** para la gestión de inventario, catálogo mayorista y toma de pedidos de hielo, utilizando **SQLite3** como base de datos relacional


## Modelos y Relaciones

El sistema cuenta con tres modelos principales conectados mediante claves foráneas (`ForeignKey`):

*   `Categoria`**: Agrupa los productos del catálogo.
   `nombre` (texto único): Nombre de la categoría (ej. *Hielo Mayorista*).
   `descripcion` (texto opcional): Detalle general de la categoría.

*   `Producto`**: Representa cada formato de hielo disponible para la venta.
 `categoria` (`ForeignKey` hacia `Categoria`): Categoría a la que pertenece.
 `nombre` (texto): Nombre comercial del producto (ej. *Hielo Cilindro Premium*).
 `descripcion` (texto opcional): Características del producto.
 `precio` (numérico): Precio unitario en pesos chilenos (validado para no ser negativo).
 `formato` (texto): Presentación del envase (ej. *Bolsa 5 kg*).
 `stock` (entero positivo): Cantidad disponible en inventario.
 `disponible` (booleano): Indica si el producto está activo en catálogo.
 `fecha_creacion` (fecha/hora): Registro automático de creación.

*   `Pedido`**: Registra las órdenes de compra y ejecuta la lógica de negocio.
 `producto` (`ForeignKey` hacia `Producto`): Producto solicitado.
 `cantidad` (entero positivo): Unidades solicitadas (valida que no supere el `stock` disponible).
 `precio_unitario` (numérico): Se guarda automáticamente con el precio vigente del producto al momento de la compra.
 `total` (numérico): Se calcula automáticamente (`precio_unitario * cantidad`).
 `fecha_pedido` (fecha/hora): Registro automático de la venta.


## Endpoints de la API REST

Todos los recursos soportan operaciones CRUD completas mediante métodos HTTP estándar:

### 1. Categorías
  `GET /api/categorias/` — Lista todas las categorías.
  `POST /api/categorias/` — Crea una nueva categoría.
  `GET /api/categorias/{id}/` — Consulta el detalle de una categoría.
  `PUT /api/categorias/{id}/` — Actualiza una categoría existente.
  `DELETE /api/categorias/{id}/` — Elimina una categoría.

### 2. Productos
  `GET /api/productos/` — Lista los productos (paginado de 10 en 10). Permite búsqueda con `?search=cilindro` y ordenamiento con `?ordering=precio`.
  `POST /api/productos/` — Crea un nuevo producto.
  `GET /api/productos/{id}/` — Consulta un producto específico.
  `PUT /api/productos/{id}/` — Actualiza los datos o el stock de un producto.
  `DELETE /api/productos/{id}/` — Elimina un producto.

  **Ejemplo de solicitud (`POST /api/productos/`):**
```json
{
  "categoria": 1,
  "nombre": "Hielo Escama",
  "descripcion": "Ideal para conservación de productos frescos.",
  "precio": "2200",
  "formato": "Bolsa 5 kg",
  "stock": 40,
  "disponible": true
}


## Instalacion y ejecucion en tu computador

```powershell
# 1. Crear y activar entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Instalar dependencias
python -m pip install -r requirements.txt

# 3. Aplicar migraciones
python manage.py migrate

# 4. Cargar datos iniciales de prueba (opcional)
python manage.py loaddata catalogo_inicial.json

# 5. Iniciar servidor local
python manage.py runserver