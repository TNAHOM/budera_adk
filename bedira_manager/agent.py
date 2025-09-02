from google.adk.agents import Agent
from .sub_agents.growthAgent.agent import growth_agent
from .sub_agents.roadmapAgent.agent import roadmap_agent

from .utilities.openFile import open_file
from google.adk.planners import BuiltInPlanner
from google.genai import types

prompt_text = open_file("rootAgentPrompt.md")

root_agent = Agent(
    name="bedira_manager",
    model="gemini-2.0-flash",
    description="Central orchestrator: routes clarification vs planning, integrates child outputs, prevents scope drift.",
    instruction=prompt_text,
    sub_agents=[growth_agent, roadmap_agent],
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(include_thoughts=False, thinking_budget=0)
    ),
)
