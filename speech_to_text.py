from groq import Groq

# Initialize the Groq client
client = Groq()

def transcribe_audio(filename):
    """
    Transcribes the given audio file using a specified model.

    Args:
    filename (str): The path to the audio file to be transcribed.

    Returns:
    str: The transcribed text.
    """
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(filename, file.read()),  # Required audio file
            model="distil-whisper-large-v3-en",  # Required model to use for transcription
            response_format="json",  # Optional
            language="en",  # Optional
        )
        return transcription.text