import requests
import concurrent.futures
import time


import requests
import concurrent.futures

# URL del endpoint
endpoints = 'http://localhost:8000/api/genres'

def realizar_solicitudes(peticion):
    try:
        respuesta = requests.get(endpoints)
        if respuesta.status_code == 200:
            print(f"Solicitud #{peticion} exitosa")
        else:
            print(f"Error en solicitud #{peticion}: {respuesta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error en solicitud #{peticion}: {e}")

# Número de solicitudes concurrentes (número de hilos)
num_peticiones = 5

# Crear hilos para realizar solicitudes concurrentes
with concurrent.futures.ThreadPoolExecutor(max_workers=num_peticiones) as executor:
    tareas_pendientes = []
    for i in range(num_peticiones):
        # Enviar la solicitud de manera asíncrona utilizando el método submit
        tarea_pendiente = executor.submit(realizar_solicitudes, i)
        # Guardar la tarea pendiente en la lista de tareas pendientes
        tareas_pendientes.append(tarea_pendiente)

    for tarea_pendiente in tareas_pendientes:
        # Esperar a que la tarea pendiente se complete
        tarea_pendiente.result()

print("Todas las solicitudes han finalizado")

""" 
# Configuración de los endpoints y sus métodos
ENDPOINTS = {
    "get_all_bands": {"url": "http://localhost:8000/api/bands", "method": "GET"},
    "get_band_by_id": {"url": "http://localhost:8000/api/bands/1", "method": "GET"},
    "get_genre_by_id": {"url": "http://localhost:8000/api/genres/1", "method": "GET"},
    "get_all_genres": {"url": "http://localhost:8000/api/genres", "method": "GET"},
}

# Función para realizar una solicitud y recolectar métricas
def realizar_solicitud(endpoint_name, peticion, tiempos, exitos):
    config = ENDPOINTS[endpoint_name]
    url = config["url"]
    method = config["method"]
    inicio = time.time()

    try:
        if method == "GET":
            respuesta = requests.get(url)
        else:
            # Soporte para otros métodos (POST, PUT, DELETE)
            respuesta = requests.request(method, url)

        duracion = (time.time() - inicio) * 1000  # Tiempo en milisegundos
        tiempos.append(duracion)

        if respuesta.status_code == 200:
            exitos.append(1)
            print(f"[{endpoint_name}] Solicitud #{peticion} exitosa - {duracion:.2f} ms")
        else:
            exitos.append(0)
            print(f"[{endpoint_name}] Error #{peticion}: {respuesta.status_code} - {duracion:.2f} ms")
    except requests.exceptions.RequestException as e:
        exitos.append(0)
        print(f"[{endpoint_name}] Error #{peticion}: {e}")

# Ejecutar pruebas de carga para un endpoint
def probar_endpoint(endpoint_name, num_peticiones):
    print(f"\nIniciando pruebas para {endpoint_name}...")
    tiempos = []  # Lista para almacenar los tiempos de respuesta
    exitos = []  # Lista para almacenar el estado de éxito (1 para éxito, 0 para fallo)

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_peticiones) as executor:
        tareas = [executor.submit(realizar_solicitud, endpoint_name, i, tiempos, exitos) for i in range(num_peticiones)]
        for tarea in concurrent.futures.as_completed(tareas):
            tarea.result()

    # Cálculos de métricas
    tiempo_promedio = sum(tiempos) / len(tiempos) if tiempos else 0
    tiempo_maximo = max(tiempos) if tiempos else 0
    tasa_exito = (sum(exitos) / len(exitos)) * 100 if exitos else 0

    print(f"Pruebas para {endpoint_name} finalizadas.")
    print(f"Métricas para {endpoint_name}:")
    print(f"- Número de usuarios concurrentes: {num_peticiones}")
    print(f"- Tiempo de respuesta promedio: {tiempo_promedio:.2f} ms")
    print(f"- Tiempo de respuesta máximo: {tiempo_maximo:.2f} ms")
    print(f"- Tasa de éxito: {tasa_exito:.2f} %\n")

# Ejecutar pruebas para todos los endpoints
if __name__ == "__main__":
    num_peticiones = 40  # Configura cuántas solicitudes concurrentes deseas realizar
    for endpoint_name in ENDPOINTS.keys():
        probar_endpoint(endpoint_name, num_peticiones)


 """