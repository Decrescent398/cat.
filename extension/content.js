const imageFolder = "images/";

// Fetch all images from the folder
async function getImageList() {
  const response = await fetch(imageFolder);
  const text = await response.text();
  const files = [...text.matchAll(/href="(.*?\.jpg)"/g)].map(match => match[1]);
  return files.map(file => imageFolder + file);
}

async function replaceImages() {
  const images = document.querySelectorAll("img");
  const imageList = await getImageList();

  images.forEach(img => {
    const randomIndex = Math.floor(Math.random() * imageList.length);
    img.src = imageList[randomIndex];
  });
}

setInterval(replaceImages, 1000); // Runs every second to catch new images