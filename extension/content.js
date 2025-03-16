const catImageURL = "https://media.tenor.com/wPmWF1RWD6cAAAAe/sus-cat-cat-sus.png";

function replaceThumbnails() {
  const thumbnails = document.querySelectorAll("img");

  thumbnails.forEach(img => {
    if (img.src.includes("ytimg")) {
      img.src = catImageURL;
    }
  });
}

setInterval(replaceThumbnails, 1000); // Runs every second to catch new thumbnails
