function search_filter() {
    // Declare variables
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('search-bar');
    filter = input.value.toUpperCase();
    ul = document.getElementById("filter-list");
    li = ul.getElementsByTagName('li');
  
    // Loop through all list items, and hide those who don't match the search query
    
    for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      txtValue = a.textContent || a.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        li[i].style.display = "";
      } else {
        li[i].style.display = "none";
      }
    }
  }

  document.addEventListener('DOMContentLoaded', function() {
    const imageElement = document.getElementById('hover-img');

    if (imageElement) {
        const originalSrc = imageElement.src;
        const newSrc = '/static/main/media/start-hover.png';

        imageElement.addEventListener('mouseover', function() {
            imageElement.src = newSrc;
        });

        imageElement.addEventListener('mouseout', function() {
            imageElement.src = originalSrc;
        });
    }
});