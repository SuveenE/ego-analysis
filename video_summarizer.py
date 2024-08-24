import vertexai
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv

load_dotenv()

vertexai.init(project=os.getenv("PROJECT_ID"), location="joingobi.com")

def analyse_video(video_file):
    model = GenerativeModel("gemini-1.5-flash-001")

    prompt = """
    Provide a description of the video.
    The description should also contain anything important which people say in the video.
    """

    contents = [video_file, prompt]

    response = model.generate_content(contents)
    return response.text