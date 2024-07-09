const images = ["1.jpg", "2.jpg", "3.jpg"]; 
const slideshowDuration = 3000;

let currentIndex = 0;
const imageElement = document.getElementById("image");

function startSlideshow() {
  setInterval(changeImage, slideshowDuration);
}

function changeImage() {
  currentIndex = (currentIndex + 1) % images.length;
  const imageUrl = images[currentIndex];
  imageElement.src = imageUrl;
}

startSlideshow();