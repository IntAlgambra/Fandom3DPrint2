import Glide, {
  Controls,
  Breakpoints
} from "@glidejs/glide/dist/glide.modular.esm";

console.log(Controls, Breakpoints);

let photoGlider;
let textGlider;

document.addEventListener("DOMContentLoaded", () => {
  photoGlider = new Glide(".glide").mount({ Controls, Breakpoints });
  textGlider = new Glide(".text-glide").mount();
  console.log(photoGlider, textGlider);
  let nextBtn = document.querySelector(".gallery-next");
  let prevBtn = document.querySelector(".gallery-prev");
  nextBtn.addEventListener("click", function() {
    textGlider.go(">");
  });
  prevBtn.addEventListener("click", function() {
    textGlider.go("<");
  });
});
