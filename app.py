from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import pymysql
from model import cargar_datos, detalle_cliente

app = Flask(__name__)

conexion = pymysql.connect(
    host='localhost',  # Cambia esto al nombre de host de tu base de datos
    user='afd',    # Cambia esto al nombre de usuario de tu base de datos
    password='afd',  # Cambia esto a la contraseña de tu base de datos
    database='clientes'  # Cambia esto al nombre de la base de datos
)

@app.route('/')
def index():
    vista = cargar_datos()
    print(vista)  # Agrega esta línea para imprimir los resultados
    return render_template('clientes.html', vista=vista)

@app.route('/clientes/<int:id>', methods=["GET"])
def ver_cliente(id):
    cliente = detalle_cliente(id)  # Obtén los detalles de un cliente
    return render_template('detalle_cliente.html', cliente=cliente)




