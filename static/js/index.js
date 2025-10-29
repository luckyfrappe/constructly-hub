const banner = document.querySelector(".banner");
const closeButton = banner.querySelector("button");

closeButton.addEventListener("click", () => {
  banner.style.display = "none";
});

module.exports = { banner, closeButton };
