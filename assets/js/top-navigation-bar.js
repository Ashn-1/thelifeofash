
/* Toggle between adding and removing the responsive class to topnavbar when the user clicks on the icon */
function toggleResponsiveNavbar() {
    var navbar = document.getElementById("topnavbar");

    if (navbar.className === "topnavbar") {
        navbar.className += " responsive";
    } else {
        navbar.className = "topnavbar";
    }
}
