from google.adk.agents import Agent

buissness_description_clarifying_agent = Agent(
    name="buissness_description_clarifying_agent",
    model="gemini-2.5-flash",
    description="Business Description Clarifying Agent",
    instruction="""Focus on clarifying the business description and objectives.""",
    sub_agents=[],
    tools=[]
)