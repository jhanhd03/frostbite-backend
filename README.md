# FrostBite Backend API

Sistema backend desarrollada con Django y Django REST fRAMEWORK para la gestión de inventario, catálogo de productos y toma de pedidos mayoristas de hielo.

## Características Técnicas
- Arquitectura: Django REST Framework con `ModelViewSet` y enrutadores automáticos.
- Base de Datos: SQLite3 con relaciones `ForeignKey` (`Categoria` -> `Producto` -> `Pedido`)
- Lógica de Negocio:
  - Validación de stock disponible antes de confirmar órdenes de compra
  - Descuento automático de inventario al registrar un pedido
  - Cálculo autónomo del total y respaldo del precio unitario histórico
  - Validación de valores positivos en precios y cantidades
- Optimizaciones: Paginación global (10 registros por página), búsqueda por texto, ordenamiento dinámico y optimización de consultas mediante `select_related`

## Endpoints Principales
- `/api/categorias/` — Ver, crear o editar categorías.
- `/api/productos/` — Ver, crear o buscar productos del catálogo.
- `/api/pedidos/` — Registrar nuevas ventas y revisar el historial de pedidos.
- `/admin/` - Panel de administración Django

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