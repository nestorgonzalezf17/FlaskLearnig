from flask import Flask, request, jsonify

app = Flask(__name__)

tareas = [
    {'id': 1,'titulo': "Comprar leche", 'completa': False},
    {"id": 2,"titulo": "Estudiar python","completa": True},
    {"id": 3,"titulo": "Hacer ejercicio","completa": False}
]

@app.route('/')
def bienvenida():
    return jsonify({"mensaje":"Bienvenido a mi api rest ocn flask"})

@app.route('/api/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify({"tareas":tareas})

@app.route('/api/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    tarea = next((t for t in tareas if t["id"] == id),None)
    if tarea:
        return jsonify({"tareas":tarea})
    return jsonify({"Error":"Tarea no encontrada"}), 404

@app.route('/api/tareas', methods=['POST'])
def crear_tarea():
    tarea_nueva = request.get_json()
    if not tarea_nueva or 'titulo' not in tarea_nueva:
        return jsonify({"error":'El titulo es requerido'}), 400
    
    tarea = {
        "id": id(tareas) + 1,
        "titulo": tarea_nueva["titulo"],
        "completa": tarea_nueva.get('completa',False)
    }
    tareas.append(tarea)
    return jsonify(tarea), 201

@app.route('/api/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    tarea = next((t for t in tareas if t["id"] == id),None)
    if not tarea:
        return jsonify({"error":"Tarea no encontrada"}),404

    datos = request.get_json()
    tarea['titulo'] = datos.get('titulo', tarea['titulo'])
    tarea['completa'] = datos.get("completa", tarea['completa'])
    return jsonify(tarea)

@app.route("/api/tareas/<int:id>", methods=['DELETE'])
def delete_tarea(id):
    global tareas
    tarea = next((t for t in tareas if t["id"] == id),None)
    if not tarea:
        return jsonify({"error":"Tarea no encontrada"}),404
    tareas = [t for t in tareas if t["id"] == id]
    return jsonify({"mensaje":"tarea eliminada correctamente"})

if __name__ == "__main__":
    app.run(debug=True)

