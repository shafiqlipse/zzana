document.addEventListener("DOMContentLoaded", () => {
  const menuItems = document.querySelectorAll(".drop");

  menuItems.forEach((menuItem) => {
    const dropdown = menuItem.querySelector(".drop-menu");

    if (window.innerWidth <= 1024) {
      menuItem.addEventListener("click", (e) => {
        e.stopPropagation(); // Prevent bubbling to avoid unwanted behaviors
        dropdown.classList.toggle("droplet");
      });
    } else {
      menuItem.addEventListener("mouseover", () => {
        dropdown.classList.add("droplet");
      });

      menuItem.addEventListener("mouseout", () => {
        dropdown.classList.remove("droplet");
      });
    }
  });
});

const ToggleMenu = () => {
  const Bun = document.querySelector(".bun");

  if (Bun.classList.contains("menubar")) {
    Bun.classList.remove("menubar");
    Bun.classList.add("thuglife");
  } else {
    Bun.classList.add("menubar");
    Bun.classList.remove("thuglife");
  }
};
