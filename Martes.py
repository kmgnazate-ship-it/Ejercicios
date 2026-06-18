from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def obtener_conexion():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="2do_C Base de datos ON",
        user="postgres",
        password="12345"
    )

@app.route("/")
def inicio():

    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM actividades_becas")
        datos = cursor.fetchall()

        lista = []

        for d in datos:
            lista.append({
                "id": d[0],
                "mensaje": d[1],
                "actividad": d[2]
            })

        return jsonify(lista)

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

if __name__ == "__main__":
    app.run(debug=True)