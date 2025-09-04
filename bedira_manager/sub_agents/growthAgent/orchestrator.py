"""
Orchestrator helper for growthAgent flows.

Assumptions (kept minimal):
- Agent-like objects implement a synchronous `run(text: str) -> str` method that returns a short text response.
- The clarifying agent returns a short machine-friendly response containing a status line starting with "STATUS:".
- The obstacle task generation agent returns plain text describing tasks (it may also return structured text).

This module provides a small, testable function that sequences the flow:
1. Send package_text to clarifying_agent.
2. If clarifying agent responds with `STATUS: APPROVED`, send the package_text to the obstacle agent.
3. Return a confirmation prompt (string) that can be presented to the user, or the clarifying issues if STATUS: ISSUES.

If your real Agent API differs (for example it uses async calls or different method names), swap the calls behind the thin adapters used in tests.
"""

from typing import Callable, Optional


def orchestrate_growth_flow(
    package_text: str,
    clarifying_agent,
    obstacle_agent,
    user_confirm_callback: Optional[Callable[[str], bool]] = None,
) -> dict:
    """Run the clarification -> obstacle task generation -> (optional) user confirmation flow.

    Inputs:
      - package_text: the natural-language package the growth agent assembled (Business/Goals/Obstacles lines)
      - clarifying_agent: agent-like object with run(text)->str
      - obstacle_agent: agent-like object with run(text)->str
      - user_confirm_callback: optional callable(tasks_text)->bool that should return True if user confirms, False otherwise.

    Returns a dict with keys:
      - status: 'approved', 'issues', or 'confirmation_required'
      - clarifying_response: raw response from clarifying agent
      - obstacle_tasks: raw response from obstacle agent (present when approved)
      - confirmation: True/False/None depending on whether confirmation happened or was requested
    """

    # Step 1: run clarifying agent
    clarifying_response = clarifying_agent.run(package_text)

    # Look for STATUS line (case-insensitive)
    status_line = None
    for line in clarifying_response.splitlines():
        stripped = line.strip()
        if stripped.upper().startswith("STATUS:"):
            status_line = stripped
            break

    if status_line is None:
        # If we cannot find an explicit STATUS, treat as issues and return raw response
        return {
            "status": "issues",
            "clarifying_response": clarifying_response,
            "obstacle_tasks": None,
            "confirmation": None,
        }

    if "APPROVED" in status_line.upper():
        # Step 2: run obstacle task generation agent
        obstacle_tasks = obstacle_agent.run(package_text)

        # Step 3: ask user for confirmation (via callback) if provided
        if user_confirm_callback is not None:
            confirmed = bool(user_confirm_callback(obstacle_tasks))
            return {
                "status": "approved",
                "clarifying_response": clarifying_response,
                "obstacle_tasks": obstacle_tasks,
                "confirmation": confirmed,
            }
        else:
            return {
                "status": "confirmation_required",
                "clarifying_response": clarifying_response,
                "obstacle_tasks": obstacle_tasks,
                "confirmation": None,
            }
    else:
        # STATUS: ISSUES or other -> return issues for follow-up
        return {
            "status": "issues",
            "clarifying_response": clarifying_response,
            "obstacle_tasks": None,
            "confirmation": None,
        }
