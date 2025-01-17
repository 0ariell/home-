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

document.addEventListener('DOMContentLoaded', function () {
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const sliderWrapper = document.getElementById('slider-wrapper');
    const slides = document.querySelectorAll('.testimonial-slide');
    let currentSlide = 0;
    let slidesToShow = 5; // Por defecto, mostramos 5 por página

    // Función para actualizar la cantidad de testimonios por página según el tamaño de la pantalla
    function updateSlidesToShow() {
        if (window.innerWidth >= 1024) {
            slidesToShow = 5; // Desktop
        } else if (window.innerWidth >= 768) {
            slidesToShow = 2; // Tablet
        } else {
            slidesToShow = 1; // Mobile
        }
    }

    // Función para mover el slider
    function moveToSlide(index) {
        updateSlidesToShow(); // Actualiza el número de slides a mostrar
        // Si el índice es mayor que el número total de slides, volvemos al principio
        if (index >= slides.length - slidesToShow + 1) {
            currentSlide = 0;
        }
        // Si el índice es menor que 0, vamos al último bloque de slides
        else if (index < 0) {
            currentSlide = Math.floor((slides.length - 1) / slidesToShow) * slidesToShow;
        } else {
            currentSlide = index;
        }

        // Movemos el contenedor para mostrar los testimonios actuales
        sliderWrapper.style.transform = `translateX(-${currentSlide * (100 / slidesToShow)}%)`;
    }

    // Eventos para las flechas
    nextBtn.addEventListener('click', function() {
        moveToSlide(currentSlide + 1);
    });

    prevBtn.addEventListener('click', function() {
        moveToSlide(currentSlide - 1);
    });

    // Iniciar en el primer slide
    moveToSlide(currentSlide);

    // Cambiar el número de slides mostrados cuando se redimensiona la ventana
    window.addEventListener('resize', function() {
        moveToSlide(currentSlide);
    });
});
