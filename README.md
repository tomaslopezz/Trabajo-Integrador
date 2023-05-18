
# StockControl

El sistema presentado permite llevar un control de stock de productos como tambien de una lista con sus proveedores. El mismo esta desarollado a traves del framework Django.
 


## Conocimientos aplicados

- Python/Django
- POO
- Base de datos
## Tecnologias usadas

**Frameworks:** Django, Bootstrap5

**Base de datos:** SQLite3

**Templates:** Jinja2



## Funcionalidades

- Ingresar un producto
- Consultar lista de los productos
- Ingresar un proveedor
- Consultar lista de los proveedores
- Panel de administrador




## Requisitos
- Python 3.x
## Instalacion y uso

**1.** Clonar el repositorio.

**2.** Navegar hasta el directorio donde se encuentra.

**3.(opcional)** Crear un entorno virtual y activarlo.

**4.** Instalar las dependencias de la aplicacion (Django y Jinja).
Puede hacerlo a traves del comando `pip install` de la siguiente manera:
```bash
 pip install Django 
```
```bash
 pip install Jinja2 
```

**5.** Una vez instalado Django realize las migraciones de la base de datos con el comando:
```bash
 python manage.py migrate
```

**6.** Inicie el serivdor con el comando:
```bash
 python manage.py runserver
```


## Vistas DIsponibles
- **Acceder al panel de administrador**: http://localhost:8000/admin

    >*Nota:* Es neceseario antes crear un super usuario, esto se puede hacer con el comando `python manage.py createsuperuser`

- **Ingresar un producto**: http://localhost:8000/compra/productos/crear_producto

- **Ver lista de productos**: http://localhost:8000/compra/productos/lista_productos

- **Ingresar un proveedor**: http://localhost:8000/compra/proveedores/crear_proveedor

- **Ver lista de proveedores**: http://localhost:8000/compra/proveedores/lista_proveedores
