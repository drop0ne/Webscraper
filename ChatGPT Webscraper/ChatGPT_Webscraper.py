import pytube3
import os

def progress_function(stream, chunk, file_handle, bytes_remaining):
    # Calculate the percentage of the file that has been downloaded
    percent = (100 * (file_size - bytes_remaining)) / file_size

    # Print the progress bar
    print('\r[{0}{1}] {2:.0f}%'.format('#' * int(percent), ' ' * (100 - int(percent)), percent), end='')

url = input("Enter the YouTube video URL: ")

# Create a YouTube object using the URL
yt = pytube3.YouTube(url)

# Get the highest quality video stream available with a resolution of 1440p or less
streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().filter(lambda stream: stream.resolution in ['1440p', '1080p', '720p', '480p', '360p', '240p'])


# Print available video qualities
for i, stream in enumerate(streams):
    print(f'{i+1}. {stream.resolution}')

# Ask the user to choose a video quality
choice = int(input("Choose a video quality (1-6): "))

# Get the selected stream
stream = streams[choice - 1]

# Get the size of the file in bytes
file_size = stream.filesize

# Ask the user for the download location
download_path = input("Enter the download location (leave blank for current directory): ")

if download_path:
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    else:
        download_path = os.getcwd()

# Set the progress function
stream.on_progress(progress_function)

# Download the video to the current working directory
stream.download()

print("\nVideo downloaded successfully!")