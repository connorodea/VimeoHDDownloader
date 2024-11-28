import os
from yt_dlp import YoutubeDL
from tqdm import tqdm
from colorama import Fore, Style, init

# Initialize colorama for better terminal colors
init(autoreset=True)

def download_vimeo_video():
    print(f"{Fore.CYAN}Welcome to the Vimeo HD Video Downloader!")
    print(f"{Fore.GREEN}This program will help you download Vimeo videos in HD format.\n")
    
    # Prompt the user for the Vimeo video URL
    video_url = input(f"{Fore.YELLOW}Enter the Vimeo video URL: {Style.RESET_ALL}").strip()
    
    if not video_url:
        print(f"{Fore.RED}Error: No URL provided. Exiting.{Style.RESET_ALL}")
        return

    # Prompt the user for the output directory (default is './outputs')
    output_dir = input(f"{Fore.YELLOW}Enter the output directory (leave blank for './outputs'): {Style.RESET_ALL}").strip()
    output_dir = output_dir if output_dir else './outputs'

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define download options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio available
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Save with title as filename
        'merge_output_format': 'mp4',  # Merge video and audio into MP4
        'progress_hooks': [tqdm_hook]  # Add a progress hook for progress bar
    }

    # Download the video
    try:
        print(f"\n{Fore.CYAN}Starting download...")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"{Fore.GREEN}Download completed successfully!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Check your video in the directory: {Fore.YELLOW}{output_dir}")
    except Exception as e:
        print(f"{Fore.RED}Error during download: {e}{Style.RESET_ALL}")


# Custom progress hook for yt-dlp using tqdm
def tqdm_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', 0) or d.get('total_bytes_estimate', 0)
        downloaded_bytes = d.get('downloaded_bytes', 0)
        if total_bytes > 0:
            progress = (downloaded_bytes / total_bytes) * 100
            bar = tqdm(total=total_bytes, unit='B', unit_scale=True, desc="Downloading", leave=True)
            bar.update(downloaded_bytes)
            bar.close()
        else:
            print(f"{Fore.YELLOW}[INFO] Unable to calculate total size.{Style.RESET_ALL}")
    elif d['status'] == 'finished':
        print(f"{Fore.GREEN}Download complete! Merging files...{Style.RESET_ALL}")


if __name__ == "__main__":
    download_vimeo_video()
