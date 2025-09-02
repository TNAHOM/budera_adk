from google.adk.agents import Agent

obstacle_clarifying_agent = Agent(
    name="obstacle_clarifying_agent",
    model="gemini-2.5-flash",
    description="Obstacle Clarifying Agent",
    instruction="""Focus on identifying and clarifying obstacles to achieving business goals.""",
    sub_agents=[],
    tools=[]
)