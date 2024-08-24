import subprocess

def extract_video_audio(youtube_link, name):
    # Extract best video mp4
    print("--------> Extracting best video mp4...")
    video_cmd = f"yt-dlp -f 'bestvideo[height<=1440][ext=mp4]' {youtube_link} --output '{name}-video.mp4'"
    subprocess.run(video_cmd, shell=True)

    # Extract mp3 audio
    print("--------> Extracting mp3 audio...")
    audio_cmd = f"yt-dlp -x --audio-format mp3 {youtube_link} --output '{name}.mp3'"
    subprocess.run(audio_cmd, shell=True)

def merge_video_audio(name):
    # Merge video and audio
    print("--------> Merging video and audio...")
    merge_cmd = f"ffmpeg -i '{name}-video.mp4' -i '{name}.mp3' -c:v copy -c:a aac {name}.mp4"
    subprocess.run(merge_cmd, shell=True)

def remove_video_audio(name):
    print("--------> Remove video and audio...")
    remove_cmd = f"rm {name}-video.mp4 && rm {name}.mp3"
    subprocess.run(remove_cmd, shell=True)

def main():
    youtube_link = input("Enter the YouTube link: ")
    name = input("Enter the output file name: ")

    extract_video_audio(youtube_link, name)
    merge_video_audio(name)
    remove_video_audio(name)
    print(f"Video and audio merged successfully and saved as {name}.mp4")

if __name__ == "__main__":
    main()
