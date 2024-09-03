from dataclasses import dataclass
from datetime import timedelta, datetime


@dataclass
class YouTubeVideo:
    # type_video: TypeVideo
    title: str
    link: str
    views: int
    duration: timedelta
    date: datetime