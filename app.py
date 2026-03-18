from flask import Flask, request, jsonify
from funciones import consultas
app = Flask(__name__)



@app.route('/')
def bienvenida():
    return consultas.bienvenida()

@app.route('/api/tareas', methods=['GET'])
def obtener_tareas():
    return consultas.obtener_tareas()

@app.route('/api/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    return consultas.obtener_tarea(id)

@app.route('/api/tareas', methods=['POST'])
def crear_tarea():
    return consultas.crear_tarea(request=request.get_json())

@app.route('/api/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    return consultas.actualizar_tarea(id,request=request.get_json())

@app.route("/api/tareas/<int:id>", methods=['DELETE'])
def delete_tarea(id):
    return consultas.delete_tarea(id)

if __name__ == "__main__":
    app.run(debug=True)

