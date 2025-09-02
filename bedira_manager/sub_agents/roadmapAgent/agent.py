from google.adk.agents import Agent
from bedira_manager.utilities.openFile import open_file

instruction_text = open_file("roadmapAgentPrompt.md")

roadmap_agent = Agent(
    name="roadmapAgent",
    model="gemini-2.0-flash",
    description="Planner: turns clarified inputs into a prioritized, dependency-aware execution roadmap.",
    instruction=instruction_text,
    sub_agents=[],
    tools=[],
)
