import os
import yt_dlp
from constants import DOWNLOAD_DIRECTORY_NAME


def download_youtube_video(url, format="best"):
    output_path = os.path.join("./", DOWNLOAD_DIRECTORY_NAME)
    ydl_opts = {
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",  # Save with the video title
        "format": format,  # Video format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"An error occurred: {e}")
