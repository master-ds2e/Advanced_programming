import logging
import re
from datetime import datetime, timedelta
import pandas as pd
from models import YouTubeVideo

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Log all levels from DEBUG and above
    filename='project_logs.log',  # Log file path
    filemode='a',  # Append mode (use 'w' to overwrite each time)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Log format
)

# Create a logger object
logger = logging.getLogger(__name__)

def clean_view_count(view: str) -> int:
    pattern = r"(?P<number>\d+(?:\.\d+)?)(?P<unit>[KMB]?)"
    dic_unit = {"B": 1_000_000_000, "M": 1_000_000, "K": 1_000, "": 1}

    match = re.match(pattern, view)
    if not match:
        return -1

    num = float(match.group('number'))
    unit = match.group('unit')

    return int(num * dic_unit[unit])


def transform_ago_date(ago_str: str) -> datetime:
    pattern = r"(?P<quantity>\d+)\s(?P<unit>minute|minutes|hour|hours|day|days|month|months|year|years) ago"
    match = re.match(pattern, ago_str)

    if not match:
        raise ValueError(f"Invalid format: {ago_str}")

    quantity = int(match.group('quantity'))
    unit = match.group('unit')

    if unit in ["minute", "minutes"]:
        delta = timedelta(minutes=quantity)
    elif unit in ["hour", "hours"]:
        delta = timedelta(hours=quantity)
    elif unit in ["day", "days"]:
        delta = timedelta(days=quantity)
    elif unit in ["month", "months"]:
        delta = timedelta(days=quantity * 30)  # Approximate
    elif unit in ["year", "years"]:
        delta = timedelta(days=quantity * 365)  # Approximate
    else:
        raise ValueError(f"Unsupported unit: {unit}")

    return datetime.now() - delta


def parse_duration(duration_str: str) -> timedelta:
    try:
        parts = [int(part) for part in duration_str.split(":")]
    except ValueError:
        logger.error(f"Invalid duration format {duration_str}. Expected MM:SS, HH:MM:SS, or DD:HH:MM:SS.")
        return timedelta(0)
    if len(parts) == 2:
        return timedelta(minutes=parts[0], seconds=parts[1])
    elif len(parts) == 3:
        return timedelta(hours=parts[0], minutes=parts[1], seconds=parts[2])
    elif len(parts) == 4:
        return timedelta(days=parts[0], hours=parts[1], minutes=parts[2], seconds=parts[3])
    else:
        logger.error(f"Invalid duration format {duration_str}. Expected MM:SS, HH:MM:SS, or DD:HH:MM:SS.")
        return timedelta(0)



def create_dataframe(videos: list[YouTubeVideo]) -> pd.DataFrame:
    return pd.DataFrame([
        {
            # 'type_video': video.type_video.value,
            'title': video.title,
            'link': video.link,
            'views': video.views,
            'duration': video.duration.total_seconds(),
            'date': video.date.strftime('%Y-%m-%d %H:%M:%S')  # Format the date here
        }
        for video in videos
    ])