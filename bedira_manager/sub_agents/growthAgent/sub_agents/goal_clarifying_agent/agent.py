from google.adk.agents import Agent

goal_clarifying_agent = Agent(
    name="goal_clarifying_agent",
    model="gemini-2.5-flash",
    description="Goal Clarifying Agent",
    instruction="""Focus on clarifying the business goals and objectives.""",
    sub_agents=[],
    tools=[]
)