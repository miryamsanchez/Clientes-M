import pymysql
connection = pymysql.connect(
    host='localhost',  # Cambia esto al nombre de host de tu base de datos
    user='afd',    # Cambia esto al nombre de usuario de tu base de datos
    password='afd',  # Cambia esto a la contraseña de tu base de datos
    database='clientes'  # Cambia esto al nombre de la base de datos
)
def cargar_datos():
    vista = "SELECT * FROM clientes;"
    cursor = connection.cursor()
    cursor.execute(vista)
    resultados = cursor.fetchall()  # Recuperar los resultados de la consulta
    return resultados

def detalle_cliente(id):
    vista = "SELECT * FROM clientes WHERE id = %s ;"
    cursor = connection.cursor()
    cursor.execute(vista, (id,))
    resultado = cursor.fetchone()  # Obtén el primer registro de la consulta
    return resultado


