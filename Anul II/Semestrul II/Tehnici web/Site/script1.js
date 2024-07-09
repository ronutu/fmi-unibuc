const images = document.querySelectorAll(".img-column img");

        images.forEach((image) => {
        image.addEventListener("click", function() {
        const name = this.nextElementSibling.textContent.trim();

        const elementList = document.getElementById("elementList");
        const listItem = document.createElement("li");
        listItem.textContent = name;

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.classList.add("delete-button");
        deleteButton.addEventListener("click", function() {
        listItem.parentNode.removeChild(listItem);
        });

    listItem.appendChild(deleteButton);
    elementList.appendChild(listItem);
  });
});