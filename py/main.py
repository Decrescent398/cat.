from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os
import requests


def fetch_pinterest_images(query, num_images=10, output_dir="extension/images/"):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    search_url = f"https://www.pinterest.com/search/pins/?q={query.replace(' ', '%20')}"
    driver.get(search_url)

    # Scroll to load images
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Get image elements
    image_elements = driver.find_elements(By.TAG_NAME, "img")
    image_urls = [img.get_attribute("src") for img in image_elements if img.get_attribute("src")]

    driver.quit()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    count = 0
    for url in image_urls[:num_images]:
        try:
            img_data = requests.get(url).content
            with open(os.path.join(output_dir, f"image_{count}.jpg"), "wb") as f:
                f.write(img_data)
            print(f"Downloaded: image_{count}.jpg")
            count += 1
        except Exception as e:
            print(f"Failed to download {url}: {e}")


if __name__ == "__main__":
    search_query = "funny cat images"
    fetch_pinterest_images(search_query, num_images=15)