
  document.addEventListener("DOMContentLoaded", function() {
    const hamburger = document.querySelector(".navbar-toggler");
    const menu = document.querySelector(".navbar-collapse");
    
    hamburger.addEventListener("click", function() {
      menu.classList.toggle("collapse"); // Toggle collapse class to show/hide the menu
    });
  });

