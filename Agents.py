from textwrap import dedent
from crewai import Agent
from tools import ExaSearchToolset
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq 

# Load environment variables
load_dotenv()

# Create a ChatGroq instance
groq_llm = ChatGroq(api_key=os.environ.get("GROQ_API_KEY"), model="llama-3.1-70b-versatile")

class LobbyingAgents:
    def public_opinion_analyst(self):
        return Agent(
            role="Public Opinion Analyst",
            goal="Analyze public opinion on the given lobbying request.",
            backstory="An experienced data analyst who uses web research and a large language model to analyze public opinion data.",
            tools=ExaSearchToolset.tools(),
            verbose=True,
            llm=groq_llm  # Pass the ChatGroq instance
        )

    def coalition_builder(self):
        return Agent(
            role="Coalition Builder",
            goal="Identify potential allies to support the lobbying request.",
            backstory="A skilled networker who uses web research and a large language model to identify key allies.",
            tools=ExaSearchToolset.tools(),
            verbose=True,
            llm=groq_llm  # Pass the ChatGroq instance
        )

    def message_crafter(self):
        return Agent(
            role="Message Crafter",
            goal="Develop persuasive messaging points for the lobbying request.",
            backstory="A master communicator who uses web research and a large language model to craft resonant messages.",
            tools=ExaSearchToolset.tools(),
            verbose=True,
            llm=groq_llm  # Pass the ChatGroq instance
        )

    def grassroots_organizer(self):
        return Agent(
            role="Grassroots Organizer",
            goal="Suggest grassroots efforts to support the lobbying request.",
            backstory="A passionate organizer who uses web research and a large language model to mobilize public support.",
            tools=ExaSearchToolset.tools(),
            verbose=True,
            llm=groq_llm  # Pass the ChatGroq instance
        )

    def media_specialist(self):
        return Agent(
            role="Media Specialist",
            goal="Propose media engagement strategies to promote the lobbying request.",
            backstory="A media-savvy professional who uses web research and a large language model to effectively communicate with the public.",
            tools=ExaSearchToolset.tools(),
            verbose=True,
            llm=groq_llm  # Pass the ChatGroq instance
        )

    def lobbying_plan_integrator(self):
        return Agent(
            role="Lobbying Plan Integrator",
            goal="Synthesize all inputs from other agents into a cohesive lobbying plan.",
            backstory="A skilled strategist who creates actionable plans.",
            verbose=True,
            llm=groq_llm  # Pass the ChatGroq instance
        )