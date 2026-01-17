from flask import Flask, render_template

app = Flask(__name__)

# --- LISTAS DE CONTENIDO ---

# 1. FOTOS: Pega aquí los links que copiaste de Cloudinary
FOTOS_GALERIA = [
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627925/UMA_MI_FIESTA-204_yjqxkp.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627487/UMA_NOCHE-117_uu0els.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768628067/UMA_MI_FIESTA-447_pa1x3v.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627486/BOOK_UMA-186_ffcdkv.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627475/BOOK_UMA-156_tyafvw.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627463/BOOK_UMA-161_szlpz6.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627453/BOOK_UMA-64_rebmek.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627450/BOOK_UMA-27_qseah8.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627452/BOOK_UMA-93_lx3ane.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627450/BOOK_UMA-11_aooaaa.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627463/BOOK_UMA-161_szlpz6.jpg",
    "https://res.cloudinary.com/dfla3nr5b/image/upload/v1768627486/UMA_NOCHE-30_orsp2s.jpg"
    # ... agrega todas las que quieras, separadas por coma
]

# 2. SHORTS: Los IDs o Links Embed de tus videos de YouTube
VIDEOS_SHORTS = [
    "https://www.youtube.com/embed/OLV6Apw3yZ0",
    "https://www.youtube.com/embed/mPSoo_1ran0",
    "https://www.youtube.com/embed/nxjdUkbFv8g"
]

# --- RUTAS ---

@app.route("/")
def home():
    # Si quieres mostrar fotos en el inicio también, pásalas aquí
    # Por ahora solo renderizamos el home básico
    return render_template("index.html")

@app.route("/galeria")
def galeria():
    # AQUÍ ESTÁ LA MAGIA:
    # Enviamos las listas (FOTOS_GALERIA y VIDEOS_SHORTS) a la página web
    return render_template("galeria.html", fotos=FOTOS_GALERIA, videos=VIDEOS_SHORTS)

if __name__ == "__main__":
    app.run(debug=True)