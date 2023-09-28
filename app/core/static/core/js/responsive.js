const navbar = document.querySelector(".navbar");
const navMenu = navbar.querySelector(".nav-menu");
const hamburger = navbar.querySelector(".hamburger");
const mainContent = document.querySelector("main");
const footer = document.querySelector(".footer");

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

hamburger.addEventListener("click", toggleNavMenu);

async function toggleNavMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");

    let sleepDurationMs = 350;
    if (!mainContent.classList.contains("hidden")) {
        mainContent.classList.toggle("fade-visibility");
        footer.classList.toggle("fade-visibility");
        await sleep(sleepDurationMs);
        mainContent.classList.toggle("hidden");
        footer.classList.toggle("hidden");
    } else {
        mainContent.classList.toggle("hidden");
        footer.classList.toggle("hidden");
        await sleep(sleepDurationMs);
        mainContent.classList.toggle("fade-visibility");
        footer.classList.toggle("fade-visibility");
    }
    navbar.classList.toggle("sticky");
}
