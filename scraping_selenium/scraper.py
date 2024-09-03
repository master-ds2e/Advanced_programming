import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from models import YouTubeVideo
from utils import parse_duration, clean_view_count, transform_ago_date

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Log all levels from DEBUG and above
    filename='project_logs.log',  # Log file path
    filemode='a',  # Append mode (use 'w' to overwrite each time)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Log format
)
# Create a logger object
logger = logging.getLogger(__name__)

URL = "https://www.youtube.com/@yesvousaime549/videos"
REJECT_BUTTON_XPATH = "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button/span"


def scrape_videos(driver, url):
    driver.get(url)

    reject_all = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, REJECT_BUTTON_XPATH))
    )
    reject_all.click()

    # Scroll to load all videos
    scroll_to_load_all_videos(driver)

    return extract_video_data(driver)


def scroll_to_load_all_videos(driver):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def extract_video_data(driver):
    lst_videos = []
    all_vignette = driver.find_elements(By.ID, 'dismissible')
    for vign in all_vignette:
        try:
            link = vign.find_element(By.TAG_NAME, "a").get_attribute("href")
            title = vign.find_element(By.ID, "video-title").text
            # type_video = transform_type_videos(title)
            duration_str = vign.find_element(By.TAG_NAME, "ytd-thumbnail-overlay-time-status-renderer").text
            duration = parse_duration(duration_str)
            view_time = vign.find_element(By.ID, 'metadata-line').text
            views, date_str = view_time.split("\n")
            nb_views = clean_view_count(views.split(" ")[0])
            date = transform_ago_date(date_str)

            # Log the values
            logger.info(f"LOGGING for vignette: {vign.text}")
            logger.info("---")
            logger.info(f"Link: {link}")
            logger.info(f"Title: {title}")
            # logger.info(f"Type Video: {type_video}")
            logger.info(f"Duration String: {duration_str}")
            logger.info(f"Duration: {duration}")
            logger.info(f"View Time: {view_time}")
            logger.info(f"Views: {nb_views}")
            logger.info(f"Date: {date}")

            lst_videos.append(YouTubeVideo(
                # type_video=type_video,
                title=title,
                link=link,
                views=nb_views,
                duration=duration,
                date=date
            ))
        except NoSuchElementException as e:
            logger.error(f"Error extracting video data: {str(e)}")

    return lst_videos