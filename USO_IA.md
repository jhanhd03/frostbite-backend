## Uso de inteligencia artificial

## Detalle de uso por archivo

* `config/settings.py` — 50%:** Apoyo en la configuración inicial de Django REST Framework, habilitación de CORS y parámetros de paginación global.
* `config/urls.py` — 70%:** Consulta de sintaxis para enlazar las rutas principales de la aplicación `catalogo` bajo el prefijo `/api/`.
* `catalogo/models.py` — 55%:** Apoyo para estructurar las relaciones `ForeignKey` entre `Categoria`, `Producto` y `Pedido`, y orientación en los métodos `clean()` y `save()` para validar precios, controlar el stock y calcular totales automáticamente.
* `catalogo/serializers.py` — 35%:** Sugerencias para definir los serializadores basados en `ModelSerializer` y configurar los campos de solo lectura (`precio_unitario`, `total`, `fecha_pedido`).
* `catalogo/views.py` — 45%:** Generación inicial de los `ModelViewSet` para las operaciones CRUD y posterior modificación para agregar filtros de búsqueda (`SearchFilter`), ordenamiento (`OrderingFilter`) y optimización con `select_related`.
* `catalogo/urls.py` — 45%:** Consulta de sintaxis para configurar el enrutador automático (`DefaultRouter`) y registrar los endpoints de categorías, productos y pedidos.
* `catalogo/admin.py` — 40%:** Apoyo en la sintaxis de `@admin.register` para personalizar las columnas visibles, filtros laterales y barras de búsqueda en el panel de administración.
* `README.md` y `USO_IA.md` — 65%:** Apoyo en la redacción, estructura y formato de la documentación técnica del repositorio.



### 1. ¿En qué aspectos del proyecto utilizaron inteligencia artificial?
La IA Gemini la utilize como una guia tecnica paso a paso para configurar Django REST Framework y CORS, estructurar los serializadores y `ViewSet`, diagnosticar errores en la terminal de PowerShell (como problemas con `pip` en el entorno virtual y comandos de migración), y redactar la documentación base del repositorio.

### 2. ¿Qué partes del código fueron desarrolladas principalmente por ustedes?
la partes principales desarrolladas por nosotros fue el dominio del negocio (`FrostBite`), la estructura y atributos específicos de los tres modelos (`Categoria`, `Producto` y `Pedido`), las reglas de negocio (validación de stock disponible antes de vender, descuento automático de inventario y respaldo de precios unitarios en pesos chilenos), la creación de datos reales en la base de datos SQLite y la gestión del historial de commits en GitHub.

### 3. ¿Qué errores o problemas encontraron en las respuestas generadas por IA?
En ocasiones las sugerencias incluían configuraciones genéricas o nombres de campos que no coincidían con nuestro modelo de negocio, por lo que debimos adaptarlos manualmente. Además, en `models.py` fue necesario reordenar la ubicación de la clase `Meta` para respetar las convenciones de Django (campos primero, luego `Meta` y finalmente los métodos), y ajustar comandos de terminal como `pip freeze` reemplazándolo por `python -m pip freeze` debido a un error de rutas en el entorno virtual de Windows.

### 4. ¿Cómo verificaron que el código sugerido funcionaba correctamente?
Cada funcionalidad se probó de forma práctica tras integrarla: verificando la creación de tablas mediante `makemigrations` y `migrate`, registrando categorías y productos reales desde el panel `/admin/`, enviando peticiones `GET` y `POST` en la interfaz web de Django REST Framework (`/api/productos/` y `/api/pedidos/`) y comprobando en la base de datos SQLite3 que el stock se descontara y los totales se calcularan sin errores.

### 5. ¿Qué conocimientos adquirieron durante el desarrollo?
Se adquirió dominio práctico sobre el flujo completo de una API REST en Django: cómo relacionar modelos con `ForeignKey`, cómo encapsular reglas de negocio dentro de `clean()` y `save()`, asimismo tambien serializar datos a JSON con validaciones, cómo implementar filtros de búsqueda y paginación en `ViewSet`, y cómo mantener un flujo de trabajo ordenado en Git mediante commits