import pytube

url = input("Enter the YouTube video URL: ")

# Create a YouTube object using the URL
yt = pytube.YouTube(url)

# Get the first video stream available
stream = yt.streams.first()

# Download the video to the current working directory
stream.download()

print("Video downloaded successfully!")

