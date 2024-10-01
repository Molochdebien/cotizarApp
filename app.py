from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Cargar la hoja de Excel
excel_file = "Cotizador 2025 Danny Foton.xlsm"  # Asegúrate de que el archivo esté en la misma carpeta que app.py
df = pd.read_excel(excel_file, sheet_name='Cotizador')

@app.route('/')
def home():
    return render_template('cotizador.html')

@app.route('/cotizacion', methods=['POST'])
def cotizacion():
    # Obtener datos del formulario
    cliente = request.form['cliente']
    modelo = request.form['modelo']
    # Procesar la cotización (puedes personalizar este proceso)
    cotizacion = f"Cotización para {cliente} con el modelo {modelo}"
    return cotizacion

if __name__ == "__main__":
    app.run(debug=True)
