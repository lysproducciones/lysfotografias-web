from flask import Flask, render_template
from datetime import datetime

import cloudinary
import cloudinary.api

# --- CONFIGURACIÓN CLOUDINARY ---
cloudinary.config(
    cloud_name="dfla3nr5b",
    api_key="299958621738739",          # luego lo pasamos a variables de entorno
    api_secret="s31XLO5xi2L4r2s1AXVb2xlbz5c",
    secure=True
)

app = Flask(__name__)

# --- CONFIGURACIÓN ---
ANIO_FUNDACION = 2010

# --- HELPERS ---
def calcular_experiencia():
    anio_actual = datetime.now().year
    return anio_actual - ANIO_FUNDACION


def obtener_fotos_cloudinary():
    resultado = cloudinary.api.resources(
        type="upload",
        max_results=100
    )
    return [img["secure_url"] for img in resultado["resources"]]


# --- DATOS ---
VIDEOS_SHORTS = [
    "https://www.youtube.com/embed/46xHtysRN1o",
    "https://www.youtube.com/embed/-Lw84mKsEbM",
    "https://www.youtube.com/embed/EphkGaqidQE",
]

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

# --- RUTAS ---
@app.route('/')
def inicio():
    anios = calcular_experiencia()
    return render_template(
        'index.html',
        testimonios=TESTIMONIOS_CLIENTES,
        anios_exp=anios
    )


@app.route('/galeria')
def galeria():
    fotos = obtener_fotos_cloudinary()
    return render_template(
        'galeria.html',
        fotos=fotos,
        videos=VIDEOS_SHORTS
    )


if __name__ == '__main__':
    app.run(debug=True)
