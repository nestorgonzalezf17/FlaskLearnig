from flask import Flask, request, jsonify, blueprints

tareas = [
    {'id': 1,'titulo': "Comprar leche", 'completa': False},
    {"id": 2,"titulo": "Estudiar python","completa": True},
    {"id": 3,"titulo": "Hacer ejercicio","completa": False}
]

def bienvenida():
    return jsonify({"mensaje":"Bienvenido a mi api rest ocn flask"})

def obtener_tareas():
    return jsonify({"tareas":tareas})

def obtener_tarea(id):
    tarea = next((t for t in tareas if t["id"] == id),None)
    if tarea:
        return jsonify({"tareas":tarea})
    return jsonify({"Error":"Tarea no encontrada"}), 404

def crear_tarea(request):
    tarea_nueva = request
    if not tarea_nueva or 'titulo' not in tarea_nueva:
        return jsonify({"error":'El titulo es requerido'}), 400
    
    tarea = {
        "id": len(tareas) + 1,
        "titulo": tarea_nueva["titulo"],
        "completa": tarea_nueva.get('completa',False)
    }
    tareas.append(tarea)
    return jsonify(tarea), 201

def actualizar_tarea(id, request):
    tarea = next((t for t in tareas if t["id"] == id),None)
    if not tarea:
        return jsonify({"error":"Tarea no encontrada"}),404

    datos = request
    tarea['titulo'] = datos.get('titulo', tarea['titulo'])
    tarea['completa'] = datos.get("completa", tarea['completa'])
    return jsonify(tarea)

def delete_tarea(id):
    global tareas
    tarea = next((t for t in tareas if t["id"] == id),None)
    if not tarea:
        return jsonify({"error":"Tarea no encontrada"}),404
    tareas = [t for t in tareas if t["id"] != id]
    return jsonify({"mensaje":"tarea eliminada correctamente"})