from flask import Flask
from flask.templating import render_template
app= Flask(__name__)

""" creando una ruta para mi pagina principal(abajo)"""

@app.route('/') 
def home():
    return render_template('home.html')

""" creando segunda ruta aparte de la pagina principal(abajo)"""
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def Agregar():
    return render_template('index.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/recuperar')
def Olvidar():
    return render_template('olvide.html')

@app.route('/envio')
def Envio():
    return render_template('envio.html')

@app.route('/cambiocont')
def cambiocont():
    return render_template('cambiocont.html')

@app.route('/mensajefinal')
def mensaje():
    return render_template('mensajefinal.html')


"""validacion si esta en la pagina principa(abajo)

run nos permite arrancar uestra aplicacion"""
if __name__=='__main__':
    app.run(debug=True)