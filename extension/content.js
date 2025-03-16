const images = Array.from({ length: 15 }, (_, i) => chrome.runtime.getURL(`images/image_${i}.jpg`));

function replaceImages() {
  document.querySelectorAll('img').forEach(img => {
    const randomImage = images[Math.floor(Math.random() * images.length)];
    img.src = randomImage;
  });
}

replaceImages(); // Run on initial page load

// Mutation Observer to detect new images
const observer = new MutationObserver(replaceImages);
observer.observe(document.body, { childList: true, subtree: true });
