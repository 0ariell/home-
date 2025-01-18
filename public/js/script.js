// Obtén los elementos
const openBtn = document.getElementById('open-btn');
const closeBtn = document.getElementById('close-btn');
const sidebar = document.getElementById('sidebar');

// Muestra el sidebar
openBtn.addEventListener('click', () => {
    // Asegúrate de quitar la clase de ocultar y agregar la de mostrar con transición
    sidebar.classList.add('open');  // Añadimos la clase 'open' para mostrarlo
});

// Cierra el sidebar
closeBtn.addEventListener('click', () => {
    // Asegúrate de ocultar el sidebar con la transición
    sidebar.classList.remove('open');  // Removemos la clase 'open' para ocultarlo
});

const prevButton = document.getElementById('prev-btn');
const nextButton = document.getElementById('next-btn');
const sliderWrapper = document.getElementById('slider-wrapper');
let slideIndex = 0;

const slides = document.querySelectorAll('.testimonial-slide');
const totalSlides = slides.length;

function moveToSlide(index) {
    // Aseguramos que el índice esté dentro del rango de las diapositivas
    if (index < 0) {
        slideIndex = totalSlides - 1; // Si el índice es menor que 0, ir al último
    } else if (index >= totalSlides) {
        slideIndex = totalSlides - 1; // Si el índice es mayor o igual al total, ir al primero
    } else {
        slideIndex = index;
    }

    // Mover el slider con la transición
    sliderWrapper.style.transform = `translateX(-${slideIndex * 100}%)`;
}

prevButton.addEventListener('click', () => {
    moveToSlide(slideIndex - 1);
});

nextButton.addEventListener('click', () => {
    moveToSlide(slideIndex + 1);
});

    


// Obtener elementos
const modalLogin = document.getElementById("login-modal");
const btnUneteAhora = document.getElementById("btn-unete-ahora");
const btnRegistrarse = document.getElementById("btn-registrate");
const btnUnirse = document.getElementById("btn-unete");
const btnCerrarModal = document.getElementById("login-close");

// Función para abrir el modal
function abrirModal() {
    modalLogin.style.display = "flex"; // Mostrar el modal
}

// Función para cerrar el modal
function cerrarModal() {
    modalLogin.style.display = "none"; // Ocultar el modal
}

// Agregar evento para abrir el modal cuando se hace clic en los botones
btnRegistrarse.addEventListener("click", abrirModal);
btnUnirse.addEventListener("click", abrirModal);
btnUneteAhora.addEventListener("click", abrirModal);

// Agregar evento para cerrar el modal cuando se hace clic en el botón de cerrar
btnCerrarModal.addEventListener("click", cerrarModal);

// También cerrar el modal si se hace clic fuera del cuadro modal
window.addEventListener("click", function(event) {
    if (event.target === modalLogin) {
        cerrarModal();
    }
});
