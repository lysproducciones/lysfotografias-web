from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def inicio():
    # Aquí podrías cargar datos de una base de datos más adelante
    titulo = "Lys Fotografía y Video"
    return render_template('index.html', titulo=titulo)

# Ruta para la galería (ejemplo futuro)
@app.route('/galeria')
def galeria():
    # Tus fotos existentes
    mis_fotos = ['foto1.jpg', 'foto2.jpg', 'foto3.jpg']
    
    # NUEVO: Lista con los IDs de tus videos de YouTube (Reemplaza con los tuyos reales)
    mis_videos = ['46xHtysRN1o', '-Lw84mKsEbM', 'EphkGaqidQE'] 
    
    # Pasamos ambas listas al HTML
    return render_template('galeria.html', fotos=mis_fotos, videos=mis_videos)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Aquí Python "atrapa" lo que el usuario escribió
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        
        # POR AHORA: Lo imprimimos en tu terminal (la pantalla negra de VS Code)
        # En el futuro, aquí pondremos el código para enviar el email real.
        print(f"NUEVO CLIENTE: {nombre} ({email}) dice: {mensaje}")
        
        # Redireccionamos al inicio o a una página de "Gracias"
        return redirect(url_for('inicio'))
        
    return render_template('contacto.html')

if __name__ == '__main__':
    # debug=True permite que los cambios se vean al guardar sin reiniciar
    app.run(debug=True)