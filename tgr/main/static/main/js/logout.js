document.addEventListener('DOMContentLoaded', function() {
    const imageElement = document.getElementById('replay-hover-img');

    if (imageElement) {
        const originalSrc = imageElement.src;
        const newSrc = '/static/main/media/replay-hover.png';

        imageElement.addEventListener('mouseover', function() {
            imageElement.src = newSrc;
        });

        imageElement.addEventListener('mouseout', function() {
            imageElement.src = originalSrc;
        });
    }
});