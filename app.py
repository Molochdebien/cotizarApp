from flask import Flask, request, render_template, make_response
import pdfkit

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cotizador.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Captura los datos del formulario
    atencion = request.form['atencion']
    empresa = request.form['empresa']
    tipo = request.form['tipo']
    modelo = request.form['modelo']
    anio = request.form['anio']
    garantia = request.form['garantia']
    versiones = request.form['versiones']
    precio = request.form['precio']
    largo = request.form['largo']
    ancho = request.form['ancho']
    alto = request.form['alto']
    pbv = request.form['pbv']
    opcionesCarga = request.form['opcionesCarga']
    opcionSeleccionada = request.form['opcionSeleccionada']

    # Renderizar una plantilla HTML para el PDF
    rendered_html = render_template('pdf_template.html', atencion=atencion, empresa=empresa, tipo=tipo, 
                                    modelo=modelo, anio=anio, garantia=garantia, versiones=versiones, 
                                    precio=precio, largo=largo, ancho=ancho, alto=alto, pbv=pbv, 
                                    opcionesCarga=opcionesCarga, opcionSeleccionada=opcionSeleccionada)

    # Configurar opciones para pdfkit
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
    }

    # Generar el PDF
    pdf = pdfkit.from_string(rendered_html, False, options=options)

    # Retornar el PDF al cliente
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=cotizacion_{atencion}.pdf'
    
    return response

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
