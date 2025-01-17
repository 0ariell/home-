document.addEventListener('DOMContentLoaded', () => {
    const openBtn = document.getElementById('open-btn');
    const closeBtn = document.getElementById('close-btn');
    const sidebar = document.getElementById('sidebar');

    openBtn.addEventListener('click', () => {
        sidebar.classList.remove('hidden');
        sidebar.classList.add('translate-x-0');
    });

    closeBtn.addEventListener('click', () => {
        sidebar.classList.add('hidden');
        sidebar.classList.remove('translate-x-0');
    });
});