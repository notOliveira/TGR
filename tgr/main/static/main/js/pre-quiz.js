document.addEventListener('DOMContentLoaded', function() {
    const imageElement = document.getElementById('play-hover-img');
    if (imageElement) {
      const originalSrc = imageElement.src;
      const newSrc = '/static/main/media/play-hover.png';
      imageElement.addEventListener('mouseover', function() {
        imageElement.src = newSrc;
      });
      imageElement.addEventListener('mouseout', function() {
        imageElement.src = originalSrc;
      });
    }
  });