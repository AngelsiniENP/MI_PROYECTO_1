USE prueba;

CREATE TABLE IF NOT EXISTS autor (
	_id int AUTO_INCREMENT PRIMARY KEY,
	NOMBRE VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS libro (
	_id INT AUTO_INCREMENT PRIMARY KEY,
	PAGINAS INT NOT NULL,
	ISBN INT NOT NULL,
	EDITORIAL VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS libro_autor (
	autor_id INT,
	libro_id INT,
	PRIMARY KEY (autor_id, libro_id),
	FOREIGN KEY (autor_id) REFERENCES autor(_id),
	FOREIGN KEY (libro_id) REFERENCES libro(_id)
);

CREATE TABLE IF NOT EXISTS ejemplar (
	_id INT PRIMARY KEY AUTO_INCREMENT,
	localizcaion VARCHAR(30) NOT NULL,
	libro_id INT,
	FOREIGN KEY (libro_id) REFERENCES libro(_id)	
);

CREATE TABLE IF NOT EXISTS usuario (
	_id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(30) NOT NULL,
	telefono INT NOT NULL,
	direccion VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS prestamos (
	Fecha_prestamo DATE NOT NULL,
	Fecha_devolucion DATE NOT NULL,
	ejemplar_id INT,
	usuario_id INT,
	PRIMARY KEY(ejemplar_id, usuario_id) AUTO_INCREMENT,
	FOREIGN KEY (ejemplar_id) REFERENCES ejemplar(_id),
	FOREIGN KEY (usuario_id) REFERENCES usuario(_id)
);