import argparse
import os
from openai import OpenAI
from dotenv import load_dotenv


def transcribe_audio(client, file_path):
    try:
        with open(file_path, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1", file=audio_file
            )
        return response.text
    except Exception as e:
        print(f"Error transcribing file {file_path}: {e}")
        return None


def main():
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    parser = argparse.ArgumentParser(
        description="Transcribe audio files using OpenAI Whisper API."
    )
    parser.add_argument(
        "audio_files", nargs="+", help="Paths to audio files for transcription."
    )
    args = parser.parse_args()

    for file_path in args.audio_files:
        print(f"Transcribing file: {file_path}")
        transcription = transcribe_audio(client, file_path)
        if transcription:
            print(f"Transcription for {file_path}:\n{transcription}")
        else:
            print(f"Failed to transcribe file: {file_path}")


if __name__ == "__main__":
    main()
