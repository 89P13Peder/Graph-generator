import requests

def main():
    
    server_url = "http://server:5000/create_bar_chart"
    
    categorias = input("Ingresa las categorías separadas por comas: ").split(",")
    valores = list(map(float, input("Ingresa los valores correspondientes separados por comas: ").split(",")))
    titulo = input("Ingresa el título de la gráfica: ")
    xlabel = input("Ingresa la etiqueta para el eje X: ")
    ylabel = input("Ingresa la etiqueta para el eje Y: ")
    
    payload = {
        "categorias": categorias,
        "valores": valores,
        "titulo": titulo,
        "xlabel": xlabel,
        "ylabel": ylabel
    }
    
    try: 
        
        response = requests.post(server_url, json=payload)
        response.raise_for_status()
        
        with open("generated_chart.png", "wb") as f:
            f.write(response.content)
        print("Gráfica generada y guardada como 'generated_chart.png'.")
    except requests.exceptions.RequestException as e:
        print(f"Error al comunicarse con el servidor {e}")
        
if __name__ == "__main__":
    main()