import psycopg2


def obtener_conexion():
    return psycopg2.connect(
        host="localhost",
        database="clientes_db",
        user="postgres",
        password="123456",
        port="5432"
    )