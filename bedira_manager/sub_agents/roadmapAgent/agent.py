from google.adk.agents import Agent

from bedira_manager.utilities.openFile import open_file

instruction_text = open_file("roadmapAgentPrompt.md")

roadmap_agent = Agent(
    name="roadmapAgent",
    model="gemini-2.5-flash",
    description=(
        "Planner: converts clarified snapshot (incl. unknown/pre-revenue baselines) into a lean, dependency-aware execution roadmap tuned for a solo founder."
    ),
    instruction=instruction_text,
    sub_agents=[],
    tools=[],
)
