from pytube import YouTube

def download_video(url, output_path):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Get the highest resolution available
        stream = video.streams.get_highest_resolution()

        # Download the video to the specified output path
        stream.download(output_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
video_url = "Enter url"
output_directory = "Set path"
download_video(video_url, output_directory)
