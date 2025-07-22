# ADK Hackathon Agent

This project is a demonstration of an amusing Software Engineering (SWE) agent built using the Google Agent Development Kit (ADK). The agent is designed to answer questions about current events, weather, and time in a haiku style, and it can convert text to speech, generate music, and mux audio and video.

## Features

* **Haiku Answers:** The agent provides answers in a 5-7-5 syllable haiku format.
* **Current Information:** It uses Google Search to get up-to-date information on current events, weather, and time.
* **Text-to-Speech:** The agent can convert text responses into speech using Google's Text-to-Speech API, with options for different voice categories and speaking rates.
* **Music Generation:** It can generate music using the Lyria model, with prompts for genre, style, mood, and instrumentation.
* **Audio/Video Muxing:** The agent can combine video, audio, and text streams into a single file using the Transcoder API.
* **GCS Integration:** The agent uses Google Cloud Storage (GCS) for storing and retrieving generated audio and video files.

## Prerequisites

* Python
* Google Cloud SDK
* Required Python packages (see `requirements.txt`)

## Installation

1.  Clone the repository.
2.  Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  Authenticate with Google Cloud:

    ```bash
    gcloud auth application-default login
    ```

## Configuration

* **Google Cloud Project:** Set the `GOOGLE_CLOUD_PROJECT` environment variable to your Google Cloud project ID.
* **Google Cloud Storage Bucket:** Set the `GOOGLE_CLOUD_BUCKET` environment variable to the name of your GCS bucket.
* **Agent Configuration:** The `hack_agent/agent.py` file contains the main agent configuration, including the model name, description, and tools used by the agent.
* **Text-to-Speech:** The `hack_agent/text_to_speech.py` file contains voice category definitions that can be customized.

## How to Run

After completing the installation and configuration steps, you can use the agent in your Python scripts by importing the `root_agent` instance from `hack_agent/agent.py`.
