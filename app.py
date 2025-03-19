from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# 🔹 Conexión a MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="caragors1",
    database="biblioteca"
)
cursor = db.cursor(dictionary=True)  # Permite obtener los resultados como diccionarios

@app.route('/')
def home():
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()

    cursor.execute("SELECT * FROM libro")
    libros = cursor.fetchall()
    
    return render_template('index.html', usuarios=usuarios, libros=libros)

# 📌 Agregar un nuevo usuario
@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']

    cursor.execute("INSERT INTO usuario (nombre, email, telefono) VALUES (%s, %s, %s)",
                    (nombre, email, telefono))
    db.commit()
    
    return redirect('/')

# 📌 Agregar un nuevo libro
@app.route('/agregar_libro', methods=['POST'])
def agregar_libro():
    nombre = request.form['nombre']
    autor = request.form['autor']
    fecha_publicacion = request.form['fecha_publicacion']

    cursor.execute("INSERT INTO libro (nombre, autor, fecha_publicacion) VALUES (%s, %s, %s)",
                    (nombre, autor, fecha_publicacion))
    db.commit()
    
    return redirect('/')

# 📌 Eliminar usuario
@app.route('/eliminar_usuario/<int:_id>', methods=['POST'])
def eliminar_usuario(_id):
    cursor.execute("DELETE FROM usuario WHERE _id = %s", (_id,))
    db.commit()
    
    return redirect('/')


# 📌 Eliminar libro
@app.route('/eliminar_libro/<int:libro_id>', methods=['POST'])
def eliminar_libro(libro_id):
    cursor.execute("DELETE FROM libros WHERE id = %s", (libro_id,))
    db.commit()
    
    return redirect('/')

# 📌 Ruta para cargar los datos en el formulario de edición
@app.route('/editar_usuario/<int:_id>')
def editar_usuario(_id):
    cursor.execute("SELECT * FROM usuario WHERE _id = %s", (_id,))
    usuario = cursor.fetchone()
    return render_template('editar_usuario.html', usuario=usuario)

# 📌 Ruta para actualizar los datos en la base de datos
@app.route('/actualizar_usuario/<int:_id>', methods=['POST'])
def actualizar_usuario(_id):
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']

    cursor.execute("UPDATE usuario SET nombre = %s, email = %s, telefono = %s WHERE _id = %s",
                    (nombre, email, telefono, _id))
    db.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

