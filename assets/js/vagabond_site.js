<script>
    document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.querySelector("[data-mobile-menu-toggle]");
    const mobileMenu = document.getElementById("mobile-menu");

    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener("click", function () {
            const isOpen = mobileMenu.classList.contains("block");
            if (isOpen) {
                mobileMenu.classList.remove("block");
                mobileMenu.classList.add("hidden");
                menuToggle.setAttribute("aria-expanded", "false");
            } else {
                mobileMenu.classList.remove("hidden");
                mobileMenu.classList.add("block");
                menuToggle.setAttribute("aria-expanded", "true");
            }
        });
    }
});
</script>
