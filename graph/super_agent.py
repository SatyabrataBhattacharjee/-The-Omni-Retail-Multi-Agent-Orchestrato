# graph/super_agent.py
from graph.state import AgentState
from intents.intent_registry import INTENTS

def super_agent_node(state: AgentState):
    if "cursor" not in state:
        plan_dict = state.get("plan", {})
        plan = plan_dict.get("execution_plan", [])
        state["cursor"] = {"index": 0, "step_index": 0, "plan": plan}

    cursor = state["cursor"]
    plan = cursor["plan"]

    # Stop condition
    if cursor["index"] >= len(plan):
        state["done"] = True
        return state

    # Current intent
    intent_name = plan[cursor["index"]]["intent"]
    intent_def = INTENTS[intent_name]
    template = intent_def["plan_template"]

    # If all tasks in this intent are finished, advance to next intent
    if cursor["step_index"] >= len(template):
        cursor["index"] += 1
        cursor["step_index"] = 0
        return state

    # Prepare current step
    current_step = template[cursor["step_index"]]
    state["intent"] = intent_name
    state["next_agent"] = current_step["agent"]

    return state