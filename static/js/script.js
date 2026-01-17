/* --- static/js/script.js --- */

// 1. Función para enviar WhatsApp
function enviarWhatsApp() {
    var nombre = document.getElementById('nombre').value;
    var mensaje = document.getElementById('mensaje').value;
    var telefono = "5493425238973"; 

    if (nombre === "") {
        alert("Por favor, escribe tu nombre para saber quién eres 😊");
        return;
    }

    var textoFinal = "Hola Lys, soy " + nombre + ". " + mensaje;
    var link = "https://wa.me/" + telefono + "?text=" + encodeURIComponent(textoFinal);
    
    window.open(link, '_blank');
}

// 2. Función para agrandar tarjetas al hacer clic
function toggleZoom(card) {
    // Si la tarjeta ya está grande, la achicamos
    if (card.classList.contains('zoomed')) {
        card.classList.remove('zoomed');
        document.body.classList.remove('card-active');
    } else {
        // Primero achicamos cualquier otra que esté abierta
        var abiertas = document.querySelectorAll('.service-card.zoomed');
        abiertas.forEach(function(c) {
            c.classList.remove('zoomed');
        });

        // Agrandamos la que clickeaste
        card.classList.add('zoomed');
        document.body.classList.add('card-active');
    }
}