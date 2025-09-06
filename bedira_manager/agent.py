from google.adk.agents import Agent
from .sub_agents.growthAgent.agent import growth_agent
from .sub_agents.roadmapAgent.agent import roadmap_agent

from .utilities.openFile import open_file
from google.adk.planners import BuiltInPlanner
from google.genai import types

prompt_text = open_file("rootAgentPrompt.md")
global_instruction = open_file("globalInstruction.md")

root_agent = Agent(
    name="budera_manager",
    model="gemini-2.5-flash",
    description="Budera: solopreneur companion & root orchestrator — captures core business + status, then delegates goals/obstacles to growth and planning to roadmap.",
    # global_instruction=global_instruction,
    instruction=prompt_text,
    sub_agents=[growth_agent, roadmap_agent],
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(include_thoughts=False, thinking_budget=0)
    ),
)
