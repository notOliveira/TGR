document.addEventListener('DOMContentLoaded', function() {
  const sections = document.querySelectorAll('.section');
  let currentSectionIndex = 0;
  const btnPrevious = document.getElementById('btnPrevious');
  const btnNext = document.getElementById('btnNext');

  function showCurrentSection() {
    sections.forEach((section, index) => {
      if (index === currentSectionIndex) {
        section.classList.add('active');
      } else {
        section.classList.remove('active');
      }
    });

    // Verifica se a seção atual é a primeira e oculta o botão 'btnPrevious'
    if (currentSectionIndex === 0) {
      btnPrevious.style.display = 'none';
    } else {
      btnPrevious.style.display = 'inline';
    }

    // Verifica se a seção atual é a última e oculta o botão 'btnNext'
    if (currentSectionIndex === sections.length - 1) {
      btnNext.style.display = 'none';
    } else {
      btnNext.style.display = 'inline';
    }
  }

  function nextSection() {
    currentSectionIndex++;
    if (currentSectionIndex >= sections.length) {
      currentSectionIndex = 0;
    }
    showCurrentSection();
  }

  function previousSection() {
    if (currentSectionIndex === 0) {
      return;
    }
    currentSectionIndex--;
    showCurrentSection();
  }

  btnPrevious.addEventListener('click', previousSection);
  btnNext.addEventListener('click', nextSection);

  showCurrentSection();
});