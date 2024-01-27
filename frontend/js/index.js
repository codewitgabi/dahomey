const modal = document.querySelector(".modal-container");
const deleteBtns = document.querySelectorAll(".delete-btn");

document.querySelector("#close-id").addEventListener("click", () => {
  modal.style.display = "none";
});

deleteBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    modal.style.display = "flex";
    // console.log(btn?.dataset?.itemid)
  });
});
