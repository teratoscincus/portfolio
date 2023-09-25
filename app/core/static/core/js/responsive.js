const navbar = document.querySelector(".navbar");
const navMenu = navbar.querySelector(".nav-menu");
const hamburger = navbar.querySelector(".hamburger");

hamburger.addEventListener("click", toggleNavMenu);

function toggleNavMenu() {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
}
