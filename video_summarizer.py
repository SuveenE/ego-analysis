import vertexai
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credential.json"

vertexai.init(project="458181737688", location="us-central1")



def analyse_video(video_file):
    model = GenerativeModel("gemini-1.5-flash-001")

    prompt = """
    Provide a description of the video.
    The description should also contain anything important which people say in the video.
    """

    contents = [video_file, prompt]

    response = model.generate_content(contents)
    return response.text