const navbar = document.querySelector(".navbar");
const navMenu = navbar.querySelector(".nav-menu");
const hamburger = navbar.querySelector(".hamburger");

hamburger.addEventListener("click", toggleNavMenu);

const mainContent = document.querySelector("main");

function toggleNavMenu() {
    mainContent.classList.toggle("hidden");
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}
