from moviepy.video.io.VideoFileClip import VideoFileClip
import os


def separate_audio_video(input_file, output_video_file, output_audio_file):
    # Load the video file
    video = VideoFileClip(input_file)

    # Extract and save the audio
    audio = video.audio
    if audio:
        audio.write_audiofile(output_audio_file)

    # Save the video without audio
    video_without_audio = video.without_audio()
    video_without_audio.write_videofile(output_video_file, codec="libx264")

    # Close the video clip
    video.close()


def chunk_video(file_path, chunk_length=60):
    # Load the video file
    video = VideoFileClip(file_path)

    # Get the total duration of the video in seconds
    video_duration = int(video.duration)

    # Create output directory
    output_dir = "video_chunks"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate video chunks
    for start_time in range(0, video_duration, chunk_length):
        # Define the end time for the current chunk
        end_time = min(start_time + chunk_length, video_duration)

        # Extract the chunk
        chunk = video.subclip(start_time, end_time)

        # Define the output file name
        output_file = os.path.join(
            output_dir, f"chunk_{start_time // chunk_length + 1}.mp4"
        )

        # Write the chunk to the file
        chunk.write_videofile(output_file, codec="libx264")

        output_video_file = os.path.join(
            output_dir, f"chunk_{start_time // chunk_length + 1}_video.mp4"
        )

        output_audio_file = os.path.join(
            output_dir, f"chunk_{start_time // chunk_length + 1}_audio.mp3"
        )
        separate_audio_video(output_file, output_video_file, output_audio_file)

        ### THIS IS WHERE WE WILL CALL Hume AI for emotion analysis, Gemini 1.5 for activity analysis, and Groq for transcript ###

    # Close the video file
    video.close()


# Usage example
file_path = "/Users/minsukkang/Downloads/Ego video.mov"
separate_audio_video(file_path, "video.mp4", "audio.mp3")
chunk_video(file_path)
