from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def obtener_conexion():
    return psycopg2.connect(
        host="localhost",
        database="curso_flask",
        user="postgres",
        password="123456",
        port="5432"
    )

print("Conexión exitosa")


# =========================
# HOME
# =========================
@app.route('/')
def inicio():
    return jsonify({"mensaje": "API de productos funcionando"})


# =========================
# GET TODOS LOS PRODUCTOS
# =========================
@app.route('/productos', methods=['GET'])
def obtener_productos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, precio, stock, categoria FROM productos")
    datos = cursor.fetchall()

    productos = []

    for p in datos:
        productos.append({
            "id": p[0],
            "nombre": p[1],
            "precio": float(p[2]),
            "stock": p[3],
            "categoria": p[4]
        })

    cursor.close()
    conexion.close()

    return jsonify(productos)


# =========================
# GET PRODUCTO POR ID
# =========================
@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, nombre, precio, stock, categoria FROM productos WHERE id=%s",
        (id,)
    )

    p = cursor.fetchone()

    cursor.close()
    conexion.close()

    if p:
        return jsonify({
            "id": p[0],
            "nombre": p[1],
            "precio": float(p[2]),
            "stock": p[3],
            "categoria": p[4]
        })

    return jsonify({"error": "Producto no encontrado"}), 404


# =========================
# POST - CREAR PRODUCTO
# =========================
@app.route('/productos', methods=['POST'])
def crear_producto():

    datos = request.get_json()

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO productos(nombre, precio, stock, categoria) VALUES(%s, %s, %s, %s) RETURNING id",
        (datos['nombre'], datos['precio'], datos['stock'], datos['categoria'])
    )

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()
    cursor.close()
    conexion.close()

    return jsonify({
        "id": nuevo_id,
        "nombre": datos['nombre']
    }), 201


# =========================
# PUT - ACTUALIZAR PRODUCTO
# =========================
@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):

    datos = request.get_json()

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE productos SET nombre=%s, precio=%s, stock=%s, categoria=%s WHERE id=%s",
        (datos['nombre'], datos['precio'], datos['stock'], datos['categoria'], id)
    )

    conexion.commit()
    cursor.close()
    conexion.close()

    return jsonify({"mensaje": "Producto actualizado correctamente"})


# =========================
# DELETE - ELIMINAR PRODUCTO
# =========================
@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM productos WHERE id=%s",
        (id,)
    )

    conexion.commit()
    cursor.close()
    conexion.close()

    return jsonify({"mensaje": "Producto eliminado correctamente"})


# =========================
# RUN SERVER
# =========================
if __name__ == '__main__':
    app.run(debug=True)