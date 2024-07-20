import yt_dlp

# Define the save path for the downloaded video
SAVE_PATH = "D:\\Python Projects\\Youtube video downloader"  # Adjust this path as needed

# YouTube video link
link = "https://www.youtube.com/watch?v=_iktURk0X-A"

# yt-dlp options
ydl_opts = {
    'outtmpl': SAVE_PATH + '\\%(title)s.%(ext)s',  # Path to save the video with backslashes for Windows
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Downloads the best video and audio or the best combined MP4 format
    'merge_output_format': 'mp4',  # Merge video and audio into a single MP4 file
    'noplaylist': True,  # Download only the video, not the entire playlist
    'retries': 10,  # Retry the download in case of failure
    'retry_sleep': 5,  # Time to wait between retries
    'max_sleep': 30,  # Maximum time to wait before retrying on failure
    'progress_hooks': [  # Track download progress
        lambda d: print(f"Progress: {d['_percent_str']} ({d['_eta_str']})") if d['status'] == 'downloading' else None
    ],
    'quiet': False,  # Print status messages and errors
    # 'writethumbnail': True,  # Download video thumbnail
    'postprocessors': [{  # Convert video to .mp4 format if it's not already
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Video downloaded successfully!')
except Exception as e:
    print(f"Some Error: {e}")
