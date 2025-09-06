from google.adk.agents import Agent

from bedira_manager.utilities.openFile import open_file
from pydantic import BaseModel, Field
from typing import List


class ObstacleTask(BaseModel):
    obstacle: str = Field(..., description="A specific obstacle the user is facing.")
    tasks: List[str] = Field(
        ..., description="A specific, actionable task to overcome the obstacle."
    )


class ObstacleTasksResponse(BaseModel):
    obstacle_tasks: List[ObstacleTask] = Field(
        ..., description="A list of obstacles and their corresponding tasks."
    )


instruction_text = open_file("obstacle_task_generation_agent.md")


obstacle_task_generation_agent = Agent(
    name="obstacle_task_generation_agent",
    model="gemini-2.5-flash",
    description=(
        "Post-approval transformer: expands each approved obstacle into 2–5 concise, high-impact actionable tasks for a solo founder."
    ),
    instruction=instruction_text,
    output_schema=ObstacleTasksResponse,
    # returns structured obstacle->tasks mapping and a short 'Confirm prompt' line for the user
    sub_agents=[],
    tools=[],
)
