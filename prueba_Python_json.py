import json
from urllib.request import urlopen
from urllib.error import URLError

url = "https://jsonplaceholder.typicode.com/todos?userId=1"

try:
    with urlopen(url, timeout=10) as respuesta:
        tareas = json.load(respuesta)

    for tarea in tareas[:5]:
        print("ID:", tarea["id"])
        print("Título:", tarea["title"])
        print("Completada:", tarea["completed"])
        print("---")

except (URLError, json.JSONDecodeError):
    print("No fue posible obtener datos válidos.")