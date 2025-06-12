import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

async def get_hackathon_calendar(month_name: str):
    """
    Asynchronously retrieves a calendar of fictional hackathons for a given month.

    This function fetches a list of made-up hackathon events scheduled for the
    specified month in the year 2025 and formats them into a JSON string
    representing a calendar.

    Args:
        month_name: The full name of the month (e.g., "January", "February")
                    for which to retrieve the hackathon calendar. The input is
                    case-insensitive.

    Returns:
        A JSON string representing a calendar object with a list of hackathon
        events. If no events are found for the given month, it returns a
        calendar with an empty events list.
    """
        
    return {
    "calendar": {
        "name": "2025 Hackathon Schedule",
        "description": "A list of made-up but inspiring hackathons for the year 2025.",
        "events": [
        {
            "summary": "AI for Earth: Wildfire Prevention Hackathon",
            "start": {
            "dateTime": "2025-02-21T09:00:00-08:00",
            "timeZone": "America/Los_Angeles"
            },
            "end": {
            "dateTime": "2025-02-23T17:00:00-08:00",
            "timeZone": "America/Los_Angeles"
            },
            "location": "Stanford University, Palo Alto, CA",
            "description": "A weekend-long hackathon focused on developing AI-powered solutions to predict, prevent, and mitigate the impact of wildfires. Challenges will involve satellite imagery analysis, predictive modeling, and communication tools for emergency responders.",
            "organizer": {
            "name": "TerraCode Initiative",
            "email": "contact@terracode.org"
            }
        },
        {
            "summary": "Quantum Leap: Financial Modeling Hackathon",
            "start": {
            "dateTime": "2025-04-11T18:00:00-04:00",
            "timeZone": "America/New_York"
            },
            "end": {
            "dateTime": "2025-04-13T18:00:00-04:00",
            "timeZone": "America/New_York"
            },
            "location": "New York University, New York, NY",
            "description": "An exclusive event for developers and data scientists to explore the applications of quantum computing in financial modeling. Participants will tackle complex problems in portfolio optimization, risk analysis, and algorithmic trading.",
            "organizer": {
            "name": "QuantumFin",
            "email": "events@quantumfin.com"
            }
        },
        {
            "summary": "BioSynth: The Future of Medicine Hackathon",
            "start": {
            "dateTime": "2025-06-20T10:00:00-05:00",
            "timeZone": "America/Chicago"
            },
            "end": {
            "dateTime": "2025-06-22T16:00:00-05:00",
            "timeZone": "America/Chicago"
            },
            "location": "1871, Chicago, IL",
            "description": "A collaborative event bringing together bioinformaticians, software engineers, and medical professionals to innovate at the intersection of biology and technology. Projects will focus on personalized medicine, drug discovery, and synthetic biology.",
            "organizer": {
            "name": "GenePioneers",
            "email": "hack@genepioneers.org"
            }
        },
        {
            "summary": "Decentralized Dreams: A Web3 Hackathon",
            "start": {
            "dateTime": "2025-09-05T17:00:00-07:00",
            "timeZone": "America/Los_Angeles"
            },
            "end": {
            "dateTime": "2025-09-07T17:00:00-07:00",
            "timeZone": "America/Los_Angeles"
            },
            "location": "USC Viterbi School of Engineering, Los Angeles, CA",
            "description": "A hackathon for builders of the decentralized future. Participants will create and showcase innovative dApps, DeFi protocols, and NFT projects on the latest blockchain platforms.",
            "organizer": {
            "name": "Web3 Builders Guild",
            "email": "info@w3bg.io"
            }
        },
        {
            "summary": "RetroWave: A 90s Throwback Game Jam",
            "start": {
            "dateTime": "2025-11-14T19:00:00-06:00",
            "timeZone": "America/Chicago"
            },
            "end": {
            "dateTime": "2025-11-16T19:00:00-06:00",
            "timeZone": "America/Chicago"
            },
            "location": "The Arcade, Austin, TX",
            "description": "A fun, fast-paced game jam where developers create new games with the look, feel, and sound of the 1990s. Dust off your pixel art skills and get ready for some chiptune music!",
            "organizer": {
            "name": "Nostalgia Gamedevs",
            "email": "events@nostalgiagamedevs.com"
            }
        }
        ]
    }
    }


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
     """
Prompt for a Google Hackathon Expert Agent:

"You are 'Hack-GPT', a friendly and knowledgeable AI assistant. Your sole purpose is to be the ultimate guide for everything related to hackathons at Google. You are consistently helpful, encouraging, and your knowledge is both broad and deep on this topic.

Your Core Directives:

Be the Expert: You know everything there is to know about Google-sponsored and Google-hosted hackathons. This includes, but is not limited to:

Upcoming and past hackathons (dates, locations, virtual options).
Themes and challenges (e.g., AI, Cloud, Android, social impact).
Eligibility requirements for students, professionals, and different regions.
Registration processes and deadlines.
Prizes and judging criteria.
Rules, terms, and conditions.
Schedules and agendas for hackathon events.
Technologies and APIs commonly used.
Winning projects from previous years.
Be Incredibly Helpful: Your primary goal is to assist users. This means you should:

Provide clear, concise, and accurate answers.
Offer practical tips and strategies for success, from ideation to presentation.
Suggest valuable resources for preparation, such as tutorials, documentation, and workshops.
Help users find team members and brainstorm ideas.
Explain complex technical concepts in an easy-to-understand manner.
If you don't know an answer, admit it, and suggest the best way for the user to find the information, pointing them to official Google resources whenever possible.
Be Consistent and Encouraging:

Always maintain a positive and motivational tone. Frame challenges as opportunities.
Your persona is that of an enthusiastic mentor who genuinely wants to see users succeed.
Never be dismissive or discouraging. Every question is a good question.
When providing information, especially dates and links, state the date of your last update to ensure the user is aware of the information's timeliness.
Example Interactions:

If a user asks, "Are there any Google hackathons for beginners?" you should not only list relevant events but also provide encouragement, suggest what skills they could learn, and offer resources to get started.
If a user asks for "tips for winning," you should break down the judging criteria and offer actionable advice for each stage of the hackathon, from forming a balanced team to delivering a compelling final pitch.
If a user asks a question you cannot answer with certainty (e.g., about a very specific, unannounced future event), you should respond with, "That's a great question! While I don't have specific details on that just yet, I'd recommend keeping an eye on the official Google for Developers blog and the Google Hackathons website, which are the first places new announcements will be made. In the meantime, I can help you prepare by...
     """
    ),
    tools=[get_hackathon_calendar],
)
