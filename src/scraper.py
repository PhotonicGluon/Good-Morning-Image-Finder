"""
scraper.py

Created on 2021-01-18
Updated on 2021-01-18

Copyright © Ryan Kan

Description: Scraping utilities.
"""

# IMPORTS
import time

import selenium.common.exceptions as sel_ex
from retry import retry
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import trange, tqdm

# CONSTANTS
CSS_THUMBNAIL = "img.Q4LuWd"
CSS_LARGE_IMG = "img.n3VNCb"
CSS_LOAD_MORE = ".mye4qd"

SELENIUM_EXCEPTIONS = (sel_ex.ElementClickInterceptedException, sel_ex.ElementNotInteractableException,
                       sel_ex.StaleElementReferenceException)


# FUNCTIONS
@retry(exceptions=SELENIUM_EXCEPTIONS, tries=6, delay=0.1, backoff=2)
def retry_click(element):
    element.click()


@retry(exceptions=KeyError, tries=6, delay=0.1, backoff=2)
def get_image_src(driver):
    actual_images = driver.find_elements_by_css_selector(CSS_LARGE_IMG)
    sources = []

    for img in actual_images:
        src = img.get_attribute("src")
        if src.startswith("http") and not src.startswith("https://encrypted-tbn0.gstatic.com/"):
            sources.append(src)
    if not len(sources):
        raise KeyError("No large image")

    return sources


def search_images_on_google(search_term, num_images):
    """
    Finds images that are related to the `search_term`.

    Args:
        search_term (str):
            The thing to search Google.

        num_images (int):
            The number of images to obtain.

    Returns:
        list[str]:
            Links of images that are related to the `search_term`.
    """

    # Form the URL to be queried
    url = f"http://www.google.com/search?q={search_term.replace(' ', '%20')}&source=lnms&tbm=isch"

    # Define the options for the headless chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")  # Linux only

    # Start a headless browser
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # Calculate the number of scrolls needed to get the desired number of images
    num_scrolls = num_images // 400

    # Get the page source with all the images
    for _ in trange(num_scrolls + 1, desc="Scrolling"):
        for _ in range(10):  # Multiple scrolls are needed to show all 400 images
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(0.2)

        # Load next 400 images
        time.sleep(1)
        try:
            driver.execute_script(f"document.querySelector('{CSS_LOAD_MORE}').click();")
        except Exception as e:
            print("Less images found:", e)
            break

    # Get the thumbnails of all the images
    thumbnails = driver.find_elements_by_css_selector(CSS_THUMBNAIL)[:num_images]

    # For each thumbnail get its URL source
    sources = []
    for thumbnail in tqdm(thumbnails, desc="Getting image sources"):
        # Click on the thumbnail
        try:
            retry_click(thumbnail)
        except SELENIUM_EXCEPTIONS:
            print("Failed to click on main image.")
            continue

        # Get the image source
        try:
            temp_sources = get_image_src(driver)
        except KeyError:
            # If can't get the main image's source, then try finding the source for the thumbnail
            thumbnail_src = thumbnail.get_attribute("src")
            if not thumbnail_src.startswith("data"):
                print("No source found for main image; Using thumbnail's source instead.")
                temp_sources = [thumbnail_src]
            else:
                print("No source found for the main image and the thumbnail; skipping.")
                continue

        [(sources.append(temp_source) if temp_source not in sources else None) for temp_source in temp_sources]

    # Return those images' links
    return sources


# DEBUG CODE
if __name__ == "__main__":
    links = search_images_on_google("Mathematics", 20)
    print(links)
