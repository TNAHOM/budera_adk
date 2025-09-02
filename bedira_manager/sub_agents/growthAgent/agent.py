from google.adk.agents import Agent
from .sub_agents.buissness_description_clarifying_agent.agent import buissness_description_clarifying_agent
from .sub_agents.goal_clarifying_agent.agent import goal_clarifying_agent
from .sub_agents.obstacle_clarifiying_agent.agent import obstacle_clarifying_agent

growth_agent = Agent(
    name="growthAgent",
    model="gemini-2.5-flash",
    description="Growth agent",
    instruction="""Focus on strategies to promote growth and expansion.
    use the following subagents to delegate tasks:
    - Business Description Clarifying Agent
    - Goal Clarifying Agent
    - Obstacle Clarifying Agent
    """,
    sub_agents=[
        buissness_description_clarifying_agent,
        goal_clarifying_agent,
        obstacle_clarifying_agent
    ],
    tools=[]
)