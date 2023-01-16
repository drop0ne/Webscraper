import requests
import os
from pytube import YouTube

def progress_function(stream, chunk, file_handle, bytes_remaining):
    # Calculate the percentage of the file that has been downloaded
    percent = (100 * (file_size - bytes_remaining)) / file_size

    # Print the progress bar
    print('\r[{0}{1}] {2:.0f}%'.format('#' * int(percent), ' ' * (100 - int(percent)), percent), end='')
    
def download_youtube_video(url, download_path):
    try:
        # Create a YouTube object using the URL
        yt = YouTube(url)
    except:
        print("Invalid URL, please try again.")
        return

    try:
        # Get the highest quality video stream available with a resolution of 1440p or less
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().filter(lambda stream: stream.resolution in ['1440p', '1080p', '720p', '480p', '360p', '240p'])
    except:
        print("Video not available, please try another video.")
        return

    # Print available video qualities
    for i, stream in enumerate(streams):
        print(f'{i+1}. {stream.resolution}')

    # Ask the user to choose a video quality
    choice = int(input("Choose a video quality (1-6): "))

    # Get the selected stream
    stream = streams[choice - 1]

    # Get the size of the file in bytes
    file_size = stream.filesize

    # Set the progress function
    stream.on_progress(progress_function)
    # Download the video to the current working directory
    stream.download()

    print("\nVideo downloaded successfully!")

def download_pornhub_video(url, download_path):
    try:
        response = requests.get(url)
        open(download_path+"/video.mp4", "wb").write(response.content)
        print("\nVideo downloaded successfully!")
    except requests.exceptions.RequestException as e:
        print(f'Error occured: {e}')

try:
    while True:
        website = input("Which website do you want to download a video from? (Youtube/Pornhub) ")
        if website.lower() == "youtube":
            url = input("Please enter the URL of the Youtube video: ")
            download_path = input("Enter the download location (leave blank for current directory): ")
            try:
                if download_path:
                    os.makedirs(download_path, exist_ok=True)
                else:
                    download_path = os.getcwd()
                download_youtube_video(url, download_path)
            except Exception as e:
                print(f'An error occurred while creating the directory: {e}')
                continue
        elif website.lower() == "pornhub":
            url = input("Please enter the URL of the Pornhub video: ")
            download_path = input("Enter the download location (leave blank for current directory): ")
            try:
                if not download_path:
                    download_path = os.getcwd()
                os.makedirs(download_path, exist_ok=True)
                download_pornhub_video(url, download_path)
            except Exception as e:
                print(f'An error occurred while creating the directory: {e}')
                continue
        else:
            print("Invalid website, please try again.")
            choice = input("Do you want to download another video? (yes/no)")
            if choice.lower() == "no":
                break
except Exception as e:
    print(f'An unexpected error occurred: {e}')

print("Exiting program...")



