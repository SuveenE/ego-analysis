import requests
import json
import os
from base64 import b64encode
import asyncio


from authenticator import Authenticator
from connection import Connection
from devices import AudioDevices
from dotenv import load_dotenv
from pyaudio import PyAudio, paInt16

# Replace with your actual API key
HUME_API_KEY = os.getenv("HUME_API_KEY")
HUME_SECRET_KEY = os.getenv("HUME_SECRET_KEY")

# API endpoint
URL = "https://api.hume.ai/v0/batch/jobs"

def encode_audio(file_path):
    with open(file_path, "rb") as audio_file:
        return b64encode(audio_file.read()).decode('utf-8')

def analyze_audio(file_path):
    encoded_audio = encode_audio(file_path)

    payload = {
        "json": {
            "models": {
                "language": {},
                "prosody": {}
            },
            "data": encoded_audio
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-Hume-Api-Key": HUME_API_KEY
    }

    response = requests.post(URL, json=payload, headers=headers)
    
    if response.status_code == 202:
        job_id = response.json()["job_id"]
        print(f"Job submitted successfully. Job ID: {job_id}")
        return job_id
    else:
        print(f"Error submitting job: {response.status_code}")
        print(response.text)
        return None

def get_job_result(job_id):
    headers = {
        "X-Hume-Api-Key": API_KEY
    }

    while True:
        response = requests.get(f"{URL}/{job_id}", headers=headers)
        
        if response.status_code == 200:
            job_status = response.json()["status"]
            
            if job_status == "COMPLETED":
                return response.json()["results"]
            elif job_status == "FAILED":
                print("Job failed")
                return None
            else:
                print(f"Job status: {job_status}. Waiting...")
        else:
            print(f"Error checking job status: {response.status_code}")
            print(response.text)
            return None

        time.sleep(5)  # Wait for 5 seconds before checking again

def main():
    audio_file_path = "path/to/your/audio/file.mp3"
    
    if not os.path.exists(audio_file_path):
        print(f"Audio file not found: {audio_file_path}")
        return

    job_id = analyze_audio(audio_file_path)
    
    if job_id:
        results = get_job_result(job_id)
        
        if results:
            print(json.dumps(results, indent=2))
        else:
            print("Failed to get results")
    else:
        print("Failed to submit job")

if __name__ == "__main__":
    main()