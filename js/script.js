// Obtén los elementos
const openBtn = document.getElementById('open-btn');
const closeBtn = document.getElementById('close-btn');
const sidebar = document.getElementById('sidebar');

// Muestra el sidebar
openBtn.addEventListener('click', () => {
    // Asegúrate de quitar la clase de ocultar y agregar la de mostrar con transición
    sidebar.classList.remove('translate-x-full');
    sidebar.classList.add('translate-x-0');
});

// Cierra el sidebar
closeBtn.addEventListener('click', () => {
    // Asegúrate de ocultar el sidebar con la transición
    sidebar.classList.add('translate-x-full');
    sidebar.classList.remove('translate-x-0');
});

document.addEventListener('DOMContentLoaded', function () {
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const sliderWrapper = document.getElementById('slider-wrapper');
    const slides = document.querySelectorAll('.testimonial-slide');
    const slidesToShow = 3; // Número de testimonios por página
    let currentSlide = 0;

    // Función para mover el slider
    function moveToSlide(index) {
        // Si el índice es mayor que el número total de slides, volvemos al principio
        if (index >= slides.length) {
            currentSlide = 0;
        }
        // Si el índice es menor que 0, vamos al último slide
        else if (index < 0) {
            currentSlide = slides.length - slidesToShow;
        } else {
            currentSlide = index;
        }

        // Movemos el contenedor para mostrar los 3 testimonios actuales
        sliderWrapper.style.transform = `translateX(-${currentSlide * (100 / slidesToShow)}%)`;
    }

    // Eventos para las flechas
    nextBtn.addEventListener('click', function () {
        moveToSlide(currentSlide + slidesToShow);
    });

    prevBtn.addEventListener('click', function () {
        moveToSlide(currentSlide - slidesToShow);
    });

    // Inicializar el slider
    moveToSlide(currentSlide);
});
