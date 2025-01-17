from flask import Flask, request, send_file
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

@app.route('/create_bar_chart', methods=['POST'])
def create_bar_chart():
    
    try:
        data = request.get_json()
        categorias = data.get("categorias", [])
        valores = data.get("valores", [])
        titulo = data.get("titulo", "Gráfica de Barras")
        xlabel = data.get("xlabel", "")
        ylabel = data.get("ylabel", "")
        
        #validar datos:
        if not categorias or not valores or len(categorias) != len(valores):
            return {"error": "Categorías y valores deben ser listas de igual longitud."}
        
        #crear gráfica:
        plt.bar(categorias,valores, color='skyblue', edgecolor='black', alpha=0.8)
        plt.title(titulo)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        #guardar gráfica en memoria:
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png', bbox_inches='tight')
        img_buffer.seek(0)
        plt.close()
        
        return send_file(img_buffer, mimetype='image/png')
    except Exception as e:
        return {"error" : f"Error al generar la gráfica: {e}"}, 500
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
    
        