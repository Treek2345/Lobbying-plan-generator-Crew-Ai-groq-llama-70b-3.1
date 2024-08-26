import streamlit as st
from dotenv import load_dotenv
from crewai import Crew
from Tasks import LobbyingTasks
from Agents import LobbyingAgents
from tools import ExaSearchToolset

# Load environment variables from .env
load_dotenv()

st.title("Lobbying Crew")

policy_topic = st.text_input("Enter the policy topic:")
lobbying_request = st.text_input("Enter your lobbying request:")

if st.button("Run Lobbying Crew"):
    # Create tasks and agents
    tasks = LobbyingTasks()
    agents = LobbyingAgents()
    public_opinion_analyst = agents.public_opinion_analyst()
    coalition_builder = agents.coalition_builder()
    message_crafter = agents.message_crafter()
    grassroots_organizer = agents.grassroots_organizer()
    media_specialist = agents.media_specialist()
    lobbying_plan_integrator = agents.lobbying_plan_integrator()

    # Create tasks (using the created agents and lobbying_request as the query)
    analyze_public_opinion_task = tasks.analyze_public_opinion_task(public_opinion_analyst, lobbying_request)
    identify_allies_task = tasks.identify_allies_task(coalition_builder, lobbying_request)
    craft_messaging_task = tasks.craft_messaging_task(message_crafter, lobbying_request)
    suggest_grassroots_efforts_task = tasks.suggest_grassroots_efforts_task(grassroots_organizer, lobbying_request)
    propose_media_engagement_task = tasks.propose_media_engagement_task(media_specialist, lobbying_request)
    integrate_lobbying_plan_task = tasks.integrate_lobbying_plan_task(lobbying_plan_integrator)

    # Set context for the final integration task
    integrate_lobbying_plan_task.context = [
        analyze_public_opinion_task,
        identify_allies_task,
        craft_messaging_task,
        suggest_grassroots_efforts_task,
        propose_media_engagement_task
    ]

    # Create and run the Crew
    crew = Crew(
        agents=[
            public_opinion_analyst,
            coalition_builder,
            message_crafter,
            grassroots_organizer,
            media_specialist,
            lobbying_plan_integrator
        ],
        tasks=[
            analyze_public_opinion_task,
            identify_allies_task,
            craft_messaging_task,
            suggest_grassroots_efforts_task,
            propose_media_engagement_task,
            integrate_lobbying_plan_task
        ]
    )

    result = crew.kickoff()

    # Display the results
    st.write(result)