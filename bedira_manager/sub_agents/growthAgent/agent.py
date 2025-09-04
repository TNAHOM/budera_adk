from google.adk.agents import Agent

from .sub_agents.clarifying_agent.agent import clarifying_agent

from bedira_manager.utilities.openFile import open_file

instruction_text = open_file("growthAgentPrompt.md")


growth_agent = Agent(
    name="growthAgent",
    model="gemini-2.0-flash",
    description="Clarification hub: orchestrates child agents to structure business, goals & obstacles for planning readiness.",
    instruction=instruction_text,
    sub_agents=[
        clarifying_agent
    ],
    tools=[],
)
