from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
    Hola, Bienvenidos<br>
    A la Carrera de Desarrollo de Software<br>
    Curso C<br>
    Estudiante Kevin Nazate<br>
    Práctica Flask<br>
    """

@app.route('/bienvenida')
def bienvenida():
    return "Hola, Bienvenidos"

@app.route('/carrera')
def carrera():
    return "A la Carrera de Desarrollo de Software"

@app.route('/curso')
def curso():
    return "Curso C"

@app.route('/estudiante')
def estudiante():
    return "Estudiante Kevin Nazate"

@app.route('/practica')
def practica():
    return "Práctica Flask"

if __name__ == '__main__':
    app.run(debug=True)