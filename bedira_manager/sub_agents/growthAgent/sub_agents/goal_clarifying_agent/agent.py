from google.adk.agents import Agent

from bedira_manager.utilities.openFile import open_file

instruction_text = open_file("goalClarifyingPrompt.md")

goal_clarifying_agent = Agent(
    name="goal_clarifying_agent",
    model="gemini-2.0-flash",
    description="Structures SMART goals: baseline, metric, target, timeframe, priority.",
    instruction=instruction_text,
    sub_agents=[],
    tools=[],
)
