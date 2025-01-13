# Transaction Merchant API

## Descripción
Transaction Merchant es una API diseñada para manejar transacciones, palabras clave, comercios y categorías. Proporciona endpoints para crear, listar y gestionar estos recursos, con un enfoque en enriquecer las transacciones basadas en palabras clave.

---

## Requisitos

- Docker
- Docker Compose

---

## Instalación y Ejecución

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/adcc662/transaction_merchant.git
   cd transaction_merchant
   ```

2. **Levantar los servicios**:
   ```bash
   docker compose up
   ```

3. **Aplicar las migraciones**:
   Una vez que los contenedores estén corriendo, aplica las migraciones:
   ```bash
   docker exec -it <container_id> python manage.py makemigrations
   docker exec -it <container_id> python manage.py migrate
   ```

   > Reemplaza `<container_id>` con el ID o nombre del contenedor correspondiente al servicio `web`.
   
---

## Endpoints

### Categorías
- **GET** `/catalog/categories/`: Lista todas las categorías.
- **POST** `/catalog/categories/`: Crea una nueva categoría.

### Comercios
- **GET** `/catalog/commerce/`: Lista todos los comercios.
- **POST** `/catalog/commerce/`: Crea un nuevo comercio.

### Palabras Clave
- **GET** `/transaction/keywords/`: Lista todas las palabras clave.
- **POST** `/transaction/keywords/`: Crea una nueva palabra clave.

### Transacciones
- **POST** `/transaction/enrichment/`: Enriquecer transacciones basadas en palabras clave.

---

## Postman Collection

Para facilitar el uso de la API, se incluye una colección de Postman exportada que contiene ejemplos de todas las solicitudes.

1. Importa la colección de Postman en tu cliente.
2. La colección se encuentra en la raíz del proyecto con el nombre `getxerpa-transactions.postman_collection.json`.

---

## Pruebas

1. **Ejecutar pruebas unitarias**:
   ```bash
   docker exec -it <container_id> python manage.py test
   ```

