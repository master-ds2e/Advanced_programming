import logging
import sys

from selenium import webdriver
from scraper import scrape_videos
from utils import create_dataframe

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,  # Log all levels from DEBUG and above
    filename='project_logs.log',  # Log file path
    filemode='a',  # Append mode (use 'w' to overwrite each time)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Log format
)
# Create a logger object
logger = logging.getLogger(__name__)

def main(youtube_channel):
    logger.info(f"Scraping videos from {youtube_channel}")
    driver = webdriver.Firefox()
    url = f"https://www.youtube.com/{youtube_channel}/videos"
    try:
        logger.info("Scraping videos")
        videos = scrape_videos(driver, url=url)
        df = create_dataframe(videos)
        df.to_excel("results/info_youtuber.xlsx")
        logger.info(f"Scraped {len(videos)} videos")
        # You can add code here to save the DataFrame to a file if needed
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <youtube_channel>, must start by @youtube_channel")
        sys.exit(1)
    youtube_channel = sys.argv[1]
    main(youtube_channel)