from google.adk.agents import Agent
from .sub_agents.buissness_description_clarifying_agent.agent import (
    buissness_description_clarifying_agent,
)
from .sub_agents.goal_clarifying_agent.agent import goal_clarifying_agent
from .sub_agents.obstacle_clarifiying_agent.agent import obstacle_clarifying_agent
from bedira_manager.utilities.openFile import open_file

instruction_text = open_file("growthAgentPrompt.md")

growth_agent = Agent(
    name="growthAgent",
    model="gemini-2.0-flash",
    description="Clarification hub: orchestrates child agents to structure business, goals & obstacles for planning readiness.",
    instruction=instruction_text,
    sub_agents=[
        buissness_description_clarifying_agent,
        goal_clarifying_agent,
        obstacle_clarifying_agent,
    ],
    tools=[],
)
