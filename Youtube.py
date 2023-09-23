from pytube import YouTube

def download_video(url, output_path):
    try:
        
        video = YouTube(url)

        
        stream = video.streams.get_highest_resolution()

        
        stream.download(output_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

video_url = "Enter url"
output_directory = "Set path"
download_video(video_url, output_directory)
