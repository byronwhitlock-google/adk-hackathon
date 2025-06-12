import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool
from hack_agent.lyria_music import generate_lyria_music
#from .google_agent import google_agent
from .text_to_speech import text_to_speech

def gcs_uri_to_public_url(gcs_uri: str) -> str:
    """
    Converts a Google Cloud Storage (GCS) URI to its public HTTPS URL format.

    Args:
        gcs_uri: The GCS URI string (e.g., "gs://bucket_name/object_name").

    Returns:
        The corresponding public HTTPS URL string
        (e.g., "https://storage.googleapis.com/bucket_name/object_name").

    Raises:
        ValueError: If the input string is not a valid GCS URI format
                    starting with "gs://" and containing a bucket and object name.
    """
    if not gcs_uri or not gcs_uri.startswith("gs://"):
        raise ValueError("Invalid GCS URI: Must start with 'gs://'")

    # Remove the "gs://" prefix
    path_part = gcs_uri[5:]

    # Find the first slash separating bucket from object
    slash_index = path_part.find('/')

    # Check if the format is valid (must have bucket and object name)
    if slash_index == -1:
        raise ValueError("Invalid GCS URI: Format must be gs://BUCKET_NAME/OBJECT_NAME")
        # Could potentially handle gs://BUCKET_NAME separately if needed
    if slash_index == len(path_part) - 1:
         raise ValueError("Invalid GCS URI: Missing object name after bucket name /")


    # Extract bucket name and object name
    bucket_name = path_part[:slash_index]
    object_name = path_part[slash_index+1:] # Get everything after the first slash

    if not bucket_name:
        raise ValueError("Invalid GCS URI: Missing bucket name")
    # It's okay for object_name to be empty here if the URI was e.g. "gs://bucket//" but usually indicates an issue.
    # The earlier check for slash_index == len(path_part) - 1 already handles "gs://bucket/"

    # Construct the public URL using an f-string
    public_url = f"https://storage.googleapis.com/{bucket_name}/{object_name}"

    return public_url

ga= LlmAgent(
    name="swe_agent",
    model="gemini-2.0-flash",
    description=(
        "Amusing SWE agent "
    ),
    instruction=(
     """
You are a freindly software engineer agent.
You answer questions about current events, weather, and time in a haiku style.

You are amusing and answer in code haiku style.

you always answer with  reference to current events.

use google search to find current events, weather, and time.

You will use the text_to_speech tool to speak your answers in a haiku style. you will use the most amusing voice and speed and make it sound funny
     """
    ),
    tools=[google_search],
    #code_executor=[BuiltInCodeExecutor],

)
root_agent = Agent(
    name="swe_root_agent",
    model="gemini-2.0-flash",
    description=(
        "Amusing SWE Root Agent "
    ),
    instruction=(
     """
You communicate with the google agent to answer questions about current events, weather, and time in a haiku style.

Take the output from the google agent and speak it using the text_to_speech tool. you always show the output using the gcs_uri_to_public_url tool. you overlay a HOT edm soundtrtack from lyria over the output. show the output.
     """
    ),
    tools=[text_to_speech, agent_tool.AgentTool(agent=ga),gcs_uri_to_public_url,generate_lyria_music],
    #code_executor=[BuiltInCodeExecutor],

)
