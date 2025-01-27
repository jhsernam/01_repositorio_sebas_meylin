from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# Ruta para generar registros de sellos discográficos
@app.route('/generate_labels/', methods=['POST'])
def generate_labels():
    # Obtener la cantidad de registros a generar desde el cuerpo de la solicitud
    data = request.get_json()
    n = data.get('n', 10)  # Por defecto genera 10 registros si no se especifica

    # Generar registros ficticios
    records = []
    for i in range(1, n + 1):
        record = {
            "id": i,
            "label_name": f"Record Label {i}",
            "location": f"City {i}"
        }
        records.append(record)

    # Guardar registros en un archivo CSV
    file_path = 'record_labels.csv'
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "label_name", "location"])
        writer.writeheader()
        writer.writerows(records)

    return jsonify({"message": f"{n} labels generated", "file": file_path}), 201


# Ruta para obtener los sellos discográficos almacenados
@app.route('/record_labels/', methods=['GET'])
def get_record_labels():
    file_path = 'record_labels.csv'
    if not os.path.exists(file_path):
        return jsonify({"error": "No labels found. Please generate them first."}), 404

    # Leer registros desde el archivo CSV
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        records = [row for row in reader]

    return jsonify(records), 200


if __name__ == '__main__':
    app.run(debug=True)
