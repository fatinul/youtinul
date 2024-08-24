import subprocess
import os
from threading import Thread


def extract_video(youtube_link, name):
    """Extract best video mp4"""
    print("--------> Extracting best video mp4...")
    video_cmd = f"yt-dlp -f 'bestvideo[height<=1440][ext=mp4]' {youtube_link} --output '{name}-video.mp4'"
    subprocess.run(video_cmd, shell=True)


def extract_audio(youtube_link, name):
    """Extract mp3 audio"""
    print("--------> Extracting mp3 audio...")
    audio_cmd = f"yt-dlp -x --audio-format mp3 {youtube_link} --output '{name}.mp3'"
    subprocess.run(audio_cmd, shell=True)


def merge_video_audio(name):
    """Merge video and audio"""
    print("--------> Merging video and audio...")
    merge_cmd = (
        f"ffmpeg -i '{name}-video.mp4' -i '{name}.mp3' -c:v copy -c:a aac {name}.mp4"
    )
    subprocess.run(merge_cmd, shell=True)


def remove_video_audio(name):
    """Remove extracted files"""
    print("--------> Remove video and audio...")
    remove_cmd = f"rm {name}-video.mp4 && rm {name}.mp3"
    subprocess.run(remove_cmd, shell=True)


def check_file_exists(file_path):
    return os.path.isfile(file_path)


class VideoExtractor(Thread):
    def __init__(self, youtube_link, name):
        super().__init__()
        self.youtube_link = youtube_link
        self.name = name

    def run(self):
        extract_video(self.youtube_link, self.name)
        print("--------> Video extracted successfully")


class AudioExtractor(Thread):
    def __init__(self, youtube_link, name):
        super().__init__()
        self.youtube_link = youtube_link
        self.name = name

    def run(self):
        extract_audio(self.youtube_link, self.name)
        print("--------> Audio extracted successfully")


def main():
    youtube_link = input("Enter the YouTube link: ")
    name = input("Enter the output file name: ")

    video_extractor = VideoExtractor(youtube_link, name)
    audio_extractor = AudioExtractor(youtube_link, name)

    video_extractor.start()
    audio_extractor.start()

    video_extractor.join()
    audio_extractor.join()

    merge_video_audio(name)
    remove_video_audio(name)

    if check_file_exists(f"{name}.mp4"):
        print(f"Video and audio merged successfully and saved as {name}.mp4")
    else:
        print(f"Video and audio of {name}.mp4 cannot be detected. Something is wrong")


if __name__ == "__main__":
    main()
