let currentIndex = 0;
const slides = document.querySelectorAll('.slide');
const captionText = document.getElementById('caption-text');
document.getElementById('next').addEventListener('click', () => {
    slides[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % slides.length;
    slides[currentIndex].classList.add('active');
    updateCaption();
});
document.getElementById('prev').addEventListener('click', () => {
    slides[currentIndex].classList.remove('active');
    currentIndex = (currentIndex - 1 + slides.length) %
        slides.length;
    slides[currentIndex].classList.add('active');
    updateCaption();
});
function updateCaption() {
    captionText.textContent = `Image ${currentIndex + 1} of
${slides.length}`;
}
// Инициализация первого слайда
slides[currentIndex].classList.add('active');
updateCaption();