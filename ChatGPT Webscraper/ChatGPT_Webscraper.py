import pytube3

def progress_function(stream, chunk, file_handle, bytes_remaining):
    # Calculate the percentage of the file that has been downloaded
    percent = (100 * (file_size - bytes_remaining)) / file_size

    # Print the progress bar
    print('\r[{0}{1}] {2:.0f}%'.format('#' * int(percent), ' ' * (100 - int(percent)), percent), end='')

url = input("Enter the YouTube video URL: ")

# Create a YouTube object using the URL
yt = pytube3.YouTube(url)

# Get the highest quality video stream available with a resolution of 1080p or less
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Get the size of the file in bytes
file_size = stream.filesize

# Set the progress function
stream.on_progress(progress_function)

# Download the video to the current working directory
stream.download()

print("\nVideo downloaded successfully!")
