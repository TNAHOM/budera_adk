from google.adk.agents import Agent
from bedira_manager.utilities.openFile import open_file

instruction_text = open_file("obstacleClarifyingPrompt.md")

obstacle_clarifying_agent = Agent(
    name="obstacle_clarifying_agent",
    model="gemini-2.0-flash",
    description="Elicits & structures obstacles with impact, root cause & goal linkage.",
    instruction=instruction_text,
    sub_agents=[],
    tools=[],
)
