from bedira_manager.sub_agents.growthAgent.orchestrator import orchestrate_growth_flow


class FakeAgent:
    def __init__(self, response: str):
        self._response = response

    def run(self, text: str) -> str:
        return self._response


def test_orchestrator_approved_flow():
    package = "Business: X\nGoals: G1...\nObstacles: O1..."
    clarifier = FakeAgent("STATUS: APPROVED\nNote: Looks good.")
    obstacle_agent = FakeAgent("O1: Task A; Task B")

    def confirm_cb(tasks_text: str) -> bool:
        assert "O1" in tasks_text
        return True

    result = orchestrate_growth_flow(package, clarifier, obstacle_agent, user_confirm_callback=confirm_cb)
    assert result["status"] in ("approved", "confirmation_required")
    assert result["obstacle_tasks"] is not None
    assert result["clarifying_response"].startswith("STATUS:")


def test_orchestrator_issues_flow():
    package = "Business: Y\nGoals: G1...\nObstacles: O1..."
    clarifier = FakeAgent("STATUS: ISSUES\n1) Missing baseline for G1")
    obstacle_agent = FakeAgent("should not be called")

    result = orchestrate_growth_flow(package, clarifier, obstacle_agent)
    assert result["status"] == "issues"
    assert result["obstacle_tasks"] is None
    assert "ISSUES" in result["clarifying_response"].upper()
