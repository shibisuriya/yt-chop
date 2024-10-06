import argparse
import subprocess


def download_video(url):
    # Command to download the video using yt-dlp
    command = ["yt-dlp", url]
    subprocess.run(command)


def main():
    parser = argparse.ArgumentParser(
        description="A simple CLI tool to download and cut YouTube videos."
    )
    parser.add_argument("url", type=str, help="URL of the YouTube video")
    parser.add_argument(
        "-s",
        "--start",
        type=str,
        required=False,
        help="Start time in hh:mm:ss format",
    )
    parser.add_argument(
        "-e",
        "--end",
        type=str,
        required=False,
        help="End time in hh:mm:ss format",
    )

    args = parser.parse_args()

    print(args)

    # Step 1: Download the video
    print(f"Downloading video from {args.url}...")
    # download_video(args.url)


if __name__ == "__main__":
    main()
