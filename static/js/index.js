const modal = document.querySelectorAll(".modal-container");
const deleteBtns = document.querySelectorAll(".delete-btn");

const closeModalBtns = document.querySelectorAll(".close-modal")

deleteBtns.forEach((btn, idx) => {
  btn.addEventListener("click", () => {
    modal[idx].style.display = "flex";
  });
});

closeModalBtns.forEach((btn, idx) => {
  btn.addEventListener("click", () => {
    modal[idx].style.display = "none";
  })
})
