const navbar = document.querySelector(".navbar");
const navMenu = navbar.querySelector(".nav-menu");
const navLinks = navMenu.querySelectorAll(".nav-link");
const hamburger = navbar.querySelector(".hamburger");
const mainContent = document.querySelector("main");
const footer = document.querySelector(".footer");

function toggleMenu(menuToggle, menu) {
    menuToggle.classList.toggle("active");
    menu.classList.toggle("active");
}

// Drop-down navbar menu

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

hamburger.addEventListener("click", toggleNavMenu);

function toggleNavMenu() {
    toggleMenu(hamburger, navMenu);
    fadeMainContent();
}

async function fadeMainContent() {
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
    navbar.classList.toggle("fixed");
}

// Highlight current page in navbar

function isVisible(element) {
    const elementRect = element.getBoundingClientRect();

    return (
        elementRect.top >= 0 &&
        elementRect.left >= 0 &&
        elementRect.bottom <=
        (window.innerHeight || document.documentElement.clientHeight) &&
        elementRect.right <=
        (window.innerWidth || document.documentElement.clientWidth)
    );
}

function getLastUrlPathPart(url) {
    const urlParts = url.split("/");

    // Trailing slash in URL cause empty string as last element
    let urlLastPart = urlParts[urlParts.length - 1];
    if (!urlLastPart) {
        urlLastPart = urlParts[urlParts.length - 2];
    }

    return urlLastPart;
}

function highlightCurrentPageNavLink() {
    const url = location.href;
    const currentPage = getLastUrlPathPart(url);

    for (i = 0; i < navLinks.length; i++) {
        const navLinkUrl = navLinks[i].href;
        const navLinkDestination = getLastUrlPathPart(navLinkUrl);

        if (navLinkDestination === currentPage) {
            navLinks[i].classList.add("current");
        }
    }
}

if (isVisible(navMenu)) {
    highlightCurrentPageNavLink();
}
