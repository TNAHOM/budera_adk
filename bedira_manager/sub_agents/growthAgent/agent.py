from google.adk.agents import Agent

from .sub_agents.clarifying_agent.agent import clarifying_agent
from .sub_agents.obstacle_task_generation_agent.agent import obstacle_task_generation_agent

from bedira_manager.utilities.openFile import open_file
from google.adk.tools.agent_tool import AgentTool


instruction_text = open_file("growthAgentPrompt.md")


growth_agent = Agent(
    name="growthAgent",
    model="gemini-2.0-flash",
    description="Clarification hub: orchestrates child agents to structure business, goals & obstacles for planning readiness.",
    instruction=instruction_text,

    tools=[AgentTool(clarifying_agent), AgentTool(obstacle_task_generation_agent)],
)
