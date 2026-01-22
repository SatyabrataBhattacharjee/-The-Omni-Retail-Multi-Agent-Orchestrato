# graph/runner.py or graph/executor.py
from graph.workflow import build_workflow
from graph.state import AgentState

def run_plan(user_id: int, execution_plan: list):
    workflow = build_workflow()
    state = AgentState()

    # Initialize immutable plan once
    state["plan"] = {"execution_plan": execution_plan}
    state["ctx"] = {"user_id": user_id}

    while not state.get("done"):
        state = workflow.invoke(state)

    return state