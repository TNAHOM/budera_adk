from google.adk.agents import Agent


roadmap_agent = Agent(
    name="roadmapAgent",
    model="gemini-2.5-flash",
    description="Roadmap agent",
    instruction="Focus on creating and managing the project roadmap.",
    sub_agents=[],
    tools=[]
)