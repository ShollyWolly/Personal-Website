const about = document.querySelectorAll(".navbar .content .menu-list .about a");
const contact = document.querySelectorAll(".navbar .content .menu-list .contact a");
const skills = document.querySelectorAll(".navbar .content .menu-list .skills a");

about[0].addEventListener("click", clickHandler);
contact[0].addEventListener("click", clickHandler);
skills[0].addEventListener("click", clickHandler);

function clickHandler(e) {
  e.preventDefault();
  const href = this.getAttribute("href");
  const offsetTop = document.querySelector(href).offsetTop;

  scroll({
    top: offsetTop,
    behavior: "smooth"
  });
}