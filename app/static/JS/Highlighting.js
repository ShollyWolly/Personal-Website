const sections = document.querySelectorAll("section");
const navLi = document.querySelectorAll("nav .content ul li");
var timer = null;

//  console.log(navLi)
window.addEventListener("scroll", () => {
  let current = "";
  sections.forEach((section) => {
    const sectionTop = section.offsetTop;

    const sectionHeight = section.clientHeight;

    if (pageYOffset >= sectionTop - sectionHeight / 3) {
      current = section.getAttribute("id");
      //  console.log(current)
    }
  });

  navLi.forEach((li) => {
    li.classList.remove("active");
    //  console.log(li.classList)
    if (li.classList.contains(current)) {
      li.classList.add("active");
    }
    
  });

  if(timer !== null) {
    clearTimeout(timer);        
  }
  timer = setTimeout(function() {
    if(current==="") {
      history.pushState(null, null, ".");
    }  
    
    else if (history.pushState) {
      history.pushState(null, null, "#" + current);
    }
    else {
      location.hash = "#" + current;
    }
  }, 200);

});