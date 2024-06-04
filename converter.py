import moviepy.editor as mp
import os

# Define the directory containing the MP4 files
directory = '/Volumes/Multimedia/英文字母歌'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.mp4'):
        # Construct the full file path
        video_path = os.path.join(directory, filename)
        
        # Load the video file
        video = mp.VideoFileClip(video_path)
        
        # Extract the audio
        audio = video.audio
        
        # Construct the output file path
        audio_filename = os.path.splitext(filename)[0] + '.mp3'
        audio_path = os.path.join(directory, audio_filename)
        
        # Save the audio to an MP3 file
        audio.write_audiofile(audio_path)
        
        # Close the video and audio clips to free up resources
        video.close()
        audio.close()

print("Conversion complete!")
