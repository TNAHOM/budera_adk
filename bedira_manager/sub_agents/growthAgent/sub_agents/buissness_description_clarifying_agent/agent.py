from google.adk.agents import Agent
from bedira_manager.utilities.openFile import open_file

instruction_text = open_file("businessDescriptionPrompt.md")

buissness_description_clarifying_agent = Agent(
    name="buissness_description_clarifying_agent",
    model="gemini-2.0-flash",
    description="Clarifies audience, problem, offer, value prop, model & stage for structured profile.",
    instruction=instruction_text,
    sub_agents=[],
    tools=[],
)
