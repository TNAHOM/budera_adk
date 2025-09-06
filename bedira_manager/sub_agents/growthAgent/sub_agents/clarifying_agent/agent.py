from google.adk.agents import Agent

from budera_manager.utilities.openFile import open_file

instruction_text = open_file("ClarifyingPrompt.md")

# TODO: the agent must add critical obstacles missed by the growth agent
clarifying_agent = Agent(
    name="clarifying_agent",
    model="gemini-2.5-flash",
    description="Final guardrail: validates candidate business/goal/obstacle packages and returns STATUS: APPROVED or STATUS: ISSUES with focused follow-ups.",
    instruction=instruction_text,
    # returns short STATUS lines; no structured output key enforced here
    sub_agents=[],
    tools=[],
)
