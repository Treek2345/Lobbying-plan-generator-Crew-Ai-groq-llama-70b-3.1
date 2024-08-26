from textwrap import dedent
from crewai import Task
from Agents import groq_llm  # Import groq_llm

class LobbyingTasks:
    def analyze_public_opinion_task(self, agent, user_query):
        print("Starting analyze_public_opinion_task")  # Log task start
        return Task(
            description=f"Analyze public opinion data related to: {user_query} (using web research). Use the Groq LLM to get insights.",
            agent=agent,
            expected_output="A bulleted list of key public opinion trends."
        )

    def identify_allies_task(self, agent, user_query):
        print("Starting identify_allies_task")  # Log task start
        return Task(
            description=f"Identify potential allies to support: {user_query} (using web research). Use the Groq LLM to get insights.",
            agent=agent,
            expected_output="A bulleted list of potential allies."
        )

    def craft_messaging_task(self, agent, user_query):
        print("Starting craft_messaging_task")  # Log task start
        return Task(
            description=f"Develop persuasive messaging for: {user_query} (using web research). Use the Groq LLM to get insights.",
            agent=agent,
            expected_output="A bulleted list of persuasive messaging points."
        )

    def suggest_grassroots_efforts_task(self, agent, user_query):
        print("Starting suggest_grassroots_efforts_task")  # Log task start
        return Task(
            description=f"Suggest grassroots efforts to support: {user_query} (using web research). Use the Groq LLM to get insights.",
            agent=agent,
            expected_output="A bulleted list of grassroots strategies."
        )

    def propose_media_engagement_task(self, agent, user_query):
        print("Starting propose_media_engagement_task")  # Log task start
        return Task(
            description=f"Propose media engagement strategies to promote: {user_query} (using web research). Use the Groq LLM to get insights.",
            agent=agent,
            expected_output="A bulleted list of media engagement strategies."
        )

    def integrate_lobbying_plan_task(self, agent):
        print("Starting integrate_lobbying_plan_task")  # Log task start
        return Task(
            description="Integrate all research into a final lobbying plan based on the previous outputs. Use the Groq LLM to synthesize the information.",
            agent=agent,
            expected_output="A comprehensive lobbying plan."
        )