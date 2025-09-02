from google.adk.agents import LlmAgent
from .sub_agents.growthAgent.agent import growth_agent
from .sub_agents.roadmapAgent.agent import roadmap_agent


root_agent = LlmAgent(
    name="bedira_manager",
    model="gemini-2.5-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.
    
    Function: Coordinates communication between Growth GPS, Action Generation, and Roadmap Agent. Ensures data flows correctly across sub-agents and outputs a final roadmap.

    You are responsible for delegating tasks to the following agent:
    - growth_agent: Acts like a “business coach” that interacts with the solopreneur. this subagent consists of the following subagents like goal analysis and clarification, obstacle identification, analysis and clarification.
    - roadmap_agent: Role: Final planner and 
        Function: Organizes all actions into a timeline.
        Prioritizes tasks based on urgency, impact, and dependencies.
        Outputs an actionable roadmap with milestones, tasks, and priorities.

    
    """,
    sub_agents=[
        growth_agent,
        roadmap_agent
    ]
)