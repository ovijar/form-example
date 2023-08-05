"""modulo"""
from flask import Flask, request, render_template

app = Flask(__name__)

# Ruta para mostrar el formulario HTML


@app.route('/')
def show_form():
    return render_template('index.html')

# Ruta para manejar los datos del formulario


@app.route('/submit', methods=['POST'])
def submit_form():
    """form"""
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        email = request.form['correo']

        # Hacer lo que necesites con los datos (en este ejemplo, imprimirlos)
        print(f'Nombre: {nombre}')
        print(f'Email: {email}')

        # Puedes redirigir a una página de agradecimiento u otra acción aquí
        return 'Formulario enviado correctamente'


if __name__ == '__main__':
    app.run(debug=True)
