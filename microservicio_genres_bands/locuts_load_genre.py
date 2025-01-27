from locust import HttpUser, task   

#Definir una clase de usuario que simula las interacciones de los usuarios en la API
class ApiUser(HttpUser):
    #Definir una tarea a realizar
    @task
    def get_home(self): #Self es una referencia a una instancia de la clase
        self.client.get("api/genres")
    
    @task
    def post_date(self):
        self.client.post("api/genres", json={"name"})