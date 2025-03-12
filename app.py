from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["base_de_datos"]  # Asegúrate de usar el nombre correcto de tu base de datos

# Colecciones
usuarios_col = db["usuarios"]
libros_col = db["libros"]
ejemplares_col = db["ejemplares"]
prestamos_col = db["prestamos"]
reservas_col = db["reservas"]
historial_col = db["historial_prestamos"]

@app.route('/')
def home():
    usuarios = list(usuarios_col.find())  # Obtener la lista de usuarios
    libros = list(libros_col.find())
    ejemplares = list(ejemplares_col.find())
    return render_template('index.html', usuarios=usuarios, libros=libros, ejemplares=ejemplares)

# 📌 Agregar un nuevo usuario

@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']

    usuarios_col.insert_one({
        "nombre": nombre,
        "email": email,
        "telefono": telefono
    })
    return redirect('/')

# 📌 Agregar un nuevo libro
@app.route('/agregar_libro', methods=['POST'])
def agregar_libro():
    nombre = request.form['nombre']
    autor = request.form['autor']
    fecha_publicacion = request.form['fecha_publicacion']

    libros_col.insert_one({
        "nombre": nombre,
        "autor": autor,
        "fecha_publicacion": int(fecha_publicacion)
    })
    return redirect('/')

# 📌 Registrar un préstamo
@app.route('/registrar_prestamo', methods=['POST'])
def registrar_prestamo():
    usuario_id = request.form['usuario_id']
    ejemplar_id = request.form['ejemplar_id']
    fecha_prestamo = request.form['fecha_prestamo']
    fecha_devolucion = request.form['fecha_devolucion']

    prestamos_col.insert_one({
        "usuario_id": ObjectId(usuario_id),
        "ejemplar_id": ObjectId(ejemplar_id),
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion,
        "estado": "activo",
        "devolucion": [{"fecha_real_devolucion": "", "estado_libro": "", "estado": "Pendiente"}]
    })
    return redirect('/')

# 📌 Registrar una reserva
@app.route('/registrar_reserva', methods=['POST'])
def registrar_reserva():
    usuario_id = request.form['usuario_id']
    ejemplar_id = request.form['ejemplar_id']
    fecha_recibir = request.form['fecha_recibir']
    fecha_limite_recibir = request.form['fecha_limite_recibir']
    puesto_reserva = int(request.form['puesto_reserva'])

    reservas_col.insert_one({
        "usuario_id": ObjectId(usuario_id),
        "ejemplar_id": ObjectId(ejemplar_id),
        "fecha_recibir": fecha_recibir,
        "fecha_limite_recibir": fecha_limite_recibir,
        "puesto_reserva": puesto_reserva
    })
    return redirect('/')

# 📌 Registrar historial de préstamos
@app.route('/registrar_historial', methods=['POST'])
def registrar_historial():
    usuario_id = request.form['usuario_id']
    ejemplar_id = request.form['ejemplar_id']
    fecha_prestamo = request.form['fecha_prestamo']
    fecha_devolucion = request.form['fecha_devolucion']
    fecha_real_devolucion = request.form['fecha_real_devolucion']
    estado_libro = request.form['estado_libro']
    estado_prestamo = request.form['estado_prestamo']

    historial_col.insert_one({
        "usuario_id": ObjectId(usuario_id),
        "ejemplar_id": ObjectId(ejemplar_id),
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion,
        "estado": estado_prestamo,
        "devolucion": {
            "fecha_real_devolucion": fecha_real_devolucion,
            "estado_libro": estado_libro,
            "estado": "Completado" if estado_prestamo == "finalizado" else "Pendiente"
        }
    })
    return redirect('/')

# 📌 Eliminar usuario
@app.route('/eliminar_usuario/<usuario_id>', methods=['POST'])
def eliminar_usuario(usuario_id):
    usuarios_col.delete_one({"_id": ObjectId(usuario_id)})
    return redirect('/')

@app.route('/eliminar_libro/<libro_id>', methods=['POST'])
def elimina_libro(libro_id):
    libros_col.delete_one({"_id": ObjectId(libro_id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
