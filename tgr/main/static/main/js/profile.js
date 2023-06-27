document.addEventListener('DOMContentLoaded', function() {
    var textContainer = document.getElementById('upload-pic');
    textContainer.innerHTML = textContainer.innerHTML.replace('Currently: ', '');
    textContainer.innerHTML = textContainer.innerHTML.replace('Change:', '');    
});