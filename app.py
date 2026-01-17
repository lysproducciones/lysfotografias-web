from flask import Flask, render_template
from datetime import datetime  # Importamos para calcular la fecha

app = Flask(__name__)

# --- CONFIGURACIÓN ---
ANIO_FUNDACION = 2010  # Año que comenzaste (para calcular los 16 años)

# --- 1. DATOS DE GALERÍA (FOTOS Y VIDEOS) ---
# (Recuerda pegar aquí tus links reales de Cloudinary y YouTube)
FOTOS_GALERIA = [
    "https://res.cloudinary.com/tu_usuario/image/upload/v1234/ejemplo_boda.jpg",
    "https://res.cloudinary.com/tu_usuario/image/upload/v1234/ejemplo_15.jpg",
    "https://res.cloudinary.com/tu_usuario/image/upload/v1234/ejemplo_paisaje.jpg",
]

VIDEOS_SHORTS = [
    "https://www.youtube.com/embed/46xHtysRN1o",
    "https://www.youtube.com/embed/-Lw84mKsEbM",
    "https://www.youtube.com/embed/EphkGaqidQE",
]

# --- 2. DATOS DE TESTIMONIOS (REALES DE GOOGLE) ---
# --- DATOS DE TESTIMONIOS (REALES + NUEVOS) ---
TESTIMONIOS_CLIENTES = [
    {
        "nombre": "Analia Benvenuti",
        "evento": "Graduación Escolar",
        "comentario": "Excelente trabajo! Realmente las ideas para los chicos, para los padres, el trabajo en la escuela, la recepción y la colación, muy bueno. Gracias por dejarnos semejante recuerdo! 🤩",
        "estrellas": 5
    },
    {
        "nombre": "Lula Gigliotti",
        "evento": "Book Adolescente",
        "comentario": "Excelente profesional. Muy atento, muy dedicado y sobre todo gracias por la paciencia (con mi adolescente). Desde 2016 eligiendo sus trabajos!",
        "estrellas": 5
    },
    {
        "nombre": "Conrado Lallana",
        "evento": "Foto y Video",
        "comentario": "Excelente trabajo!! Profesional! Los vídeos buenísimos muy originales y las fotos espectaculares!!!!",
        "estrellas": 5
    },
    {
        "nombre": "Carina Romero",
        "evento": "Evento Social",
        "comentario": "Estamos muy felices y agradecidos por la buena onda y la predisposición en todo lo que fue el servicio. Muy recomendable gracias!!! A Carlos y su familia.",
        "estrellas": 5
    },
    {
        "nombre": "Marisa Muñoz",
        "evento": "Cliente Feliz",
        "comentario": "Excelente trabajo muchísima dedicación, muy conformes, gracias.",
        "estrellas": 5
    },
    # --- AQUI EMPIEZAN LOS 4 NUEVOS ---
    {
        "nombre": "Cintia Mangold",
        "evento": "Fiesta de 15",
        "comentario": "¡Muy bueno!!! La verdad que pasamos una noche increíble y ustedes capturaron todo perfecto. Súper recomendables.",
        "estrellas": 5
    },
    {
        "nombre": "Familia López",
        "evento": "Boda",
        "comentario": "Teníamos miedo de sentirnos incómodos con las cámaras, pero tienen una onda increíble. Nos hicieron reír y disfrutar cada foto. ¡Gracias totales!",
        "estrellas": 5
    },
    {
        "nombre": "Sofi y Agus",
        "evento": "Book Exterior",
        "comentario": "Amamos el video de cronología, parecía una película de cine. Mis amigas no paraban de preguntarme quién me había sacado las fotos. ¡Unos genios!",
        "estrellas": 5
    },
    {
        "nombre": "Graciela T.",
        "evento": "15 años",
        "comentario": "Cumplieron con todo lo pactado y los tiempos de entrega fueron rapidísimos. La calidad del álbum impreso es hermosa. Sin dudas los volveremos a elegir.",
        "estrellas": 5
    }
]

# --- HELPER: CALCULAR EXPERIENCIA ---
def calcular_experiencia():
    anio_actual = datetime.now().year
    return anio_actual - ANIO_FUNDACION

# --- RUTAS ---

@app.route('/')
def inicio():
    # 1. Calculamos los años
    anios = calcular_experiencia()
    
    # 2. Enviamos TODO al HTML (Testimonios y Años)
    return render_template('index.html', 
                           testimonios=TESTIMONIOS_CLIENTES, 
                           anios_exp=anios)

@app.route('/galeria')
def galeria():
    return render_template('galeria.html', fotos=FOTOS_GALERIA, videos=VIDEOS_SHORTS)

if __name__ == '__main__':
    app.run(debug=True)