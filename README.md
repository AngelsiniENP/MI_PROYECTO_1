# 📌 Primer Proyecto de la Clase de Git y GitHub

## 📖 Descripción

En este proyecto de la clase de Git y GitHub, queremos hacer funcionar una página web utilizando un sistema **CRUD** con **MySQL y Python**.

![MySQL CRUD usando Python](https://cdn.hashnode.com/res/hashnode/image/upload/v1670187083067/yb0KwknQD.png)

## 🎯 Objetivo

Aprender a utilizar las herramientas de **Git** y **GitHub**, creando una página web sencilla para ingresar datos y almacenarlos, con la finalidad de gestionar una biblioteca digital.

## 🏗️ Estructura y características del programa

### 📌 Diagrama de caso de uso
Se crea con el fin de tener una idea clara de la estructura del programa y establecer objetivos definidos para su funcionamiento.

### 📂 Templates
Esta carpeta almacena los archivos **HTML** para mantener el orden del programa. Si es necesario agregar nuevas plantillas, se mantendrá la estructura organizada.

- En los archivos **HTML** se encuentran los formularios de la página.
- Actualmente, el **formulario de USUARIOS** permite:
  - Ingresar usuarios.
  - Actualizar usuarios.
  - Eliminar usuarios.

### 🎨 Static
Esta carpeta almacena los archivos **CSS y otros estilos**, mejorando la experiencia visual del usuario y haciendo el entorno más interactivo.

### 📜 Base de datos en MySQL
Este sistema ahora usa **MySQL** en lugar de **MongoDB**.

### 📂 BASE_DE_DATOS_BIBLIOTECA.sql
Este archivo define la estructura de la base de datos y los documentos que se podrán gestionar en la página:

- **EJEMPLARES**
- **HISTORIAL_PRESTAMOS**
- **LIBROS**
- **PRÉSTAMOS**
- **RESERVAS**
- **USUARIOS**

### 🖥️ app.py
Este archivo de **Python** contiene toda la lógica del **CRUD**, con sus funcionalidades actuales:

- ✅ Leer usuarios en **MySQL**.
- ✅ Agregar usuarios en **MySQL**.
- ✅ Actualizar usuarios en **MySQL**.
- ✅ Eliminar usuarios en **MySQL**.
### 🖥️ app.py  
Este archivo de **Python** contiene toda la lógica del **CRUD**, con sus funcionalidades actuales:  

- ✅ Leer usuarios **MySQL**.  
- ✅ Agregar usuarios  **MySQL**.  
- ✅ Actualizar usuarios **MySQL**.  
- ✅ Eliminar usuarios **MySQL**.  

## 🛠️ Instalación  

Sigue estos pasos para instalar el proyecto en tu máquina local:  

1. **Clona el repositorio**:  
   ```sh
   git clone https://github.com/AngelsiniENP/MI_PROYECTO_1.git
   ```

2. **Entra en la carpeta del proyecto**:
   ```sh
   cd MI_PROYECTO_1
   ```

3. **Instala las dependencias necesarias**:
   ```sh
   pip install flask mysql-conector-python 
   ```

## ✒️ Autor

 - Angel Manuel Gaviria Ramírez.  
