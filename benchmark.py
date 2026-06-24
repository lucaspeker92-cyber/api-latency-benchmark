import time
import requests
import csv

ITERACIONES = 10

# Comparamos la velocidad de dos APIs públicas muy usadas por desarrolladores
def test_api(nombre, url):
    start_time = time.time()
    try:
        response = requests.get(url)
        response.raise_for_status()
        latency = round((time.time() - start_time) * 1000, 2)
        # Verificamos si devuelven un JSON limpio
        is_clean_json = "{" in response.text or "[" in response.text
        return {"api": nombre, "latency_ms": latency, "clean_json": is_clean_json, "error": None}
    except Exception as e:
        return {"api": nombre, "latency_ms": None, "clean_json": False, "error": str(e)}

def run_benchmark():
    results = []
    print(f"Iniciando benchmark de latencia: {ITERACIONES} iteraciones...")
    
    for i in range(ITERACIONES):
        print(f"Iteración {i+1}/{ITERACIONES}...")
        results.append(test_api("JSONPlaceholder", "https://jsonplaceholder.typicode.com/todos/1"))
        time.sleep(0.5)
        results.append(test_api("DummyJSON", "https://dummyjson.com/products/1"))
        time.sleep(0.5)
        
    with open('resultados_benchmark.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["api", "latency_ms", "clean_json", "error"])
        writer.writeheader()
        writer.writerows(results)
        
    print("Benchmark finalizado. Resultados guardados con éxito.")

if __name__ == "__main__":
    run_benchmark()