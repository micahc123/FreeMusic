import os
from pytube import Search, YouTube

choice = input("Enter '1' to input a music title or '2' to use a text file: ")

if choice == '1':
    # Input the music title
    title = input("Enter the music title: ")
    music_titles = [title]
elif choice == '2':
    # Read music titles from a text file
    file_path = os.path.join(os.getcwd(), "music_titles.txt")
    with open(file_path, 'r') as file:
        music_titles = file.read().splitlines()
else:
    print("Invalid choice. Please try again.")
    exit()

project_folder = os.getcwd()
folder_name = os.path.join(project_folder, "audio_files")
os.makedirs(folder_name, exist_ok=True)

for title in music_titles:
    # Search for the video and get the top result
    search_results = Search(title)
    video_url = search_results.results[0].watch_url

    # Download the video
    video = YouTube(video_url)
    video.streams.filter(only_audio=True).first().download(output_path=folder_name)

    file_path = os.path.join(folder_name, video.title + ".mp4")

    mp3_file_path = os.path.join(folder_name, video.title + ".mp3")
    os.rename(file_path, mp3_file_path)

print("Music videos downloaded and converted to MP3 successfully!")