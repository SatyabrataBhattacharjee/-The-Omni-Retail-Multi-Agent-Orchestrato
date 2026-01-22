# graph/nodes.py
from intents.intent_registry import INTENTS
from graph.state import AgentState
# graph/nodes.py


# Import agent classes
from tasks.shopcore_tasks import ShopCoreAgent
from tasks.shipstream_tasks import ShipStreamAgent
from tasks.payguard_tasks import PayGuardAgent
from tasks.caredesk_tasks import CareDeskAgent

# Instantiate agents once
shopcore = ShopCoreAgent()
shipstream = ShipStreamAgent()
payguard = PayGuardAgent()
caredesk = CareDeskAgent()
def shopcore_node(state: AgentState):
    cursor = state.get("cursor")
    if not cursor:
        return state

    intent_name = state.get("intent")
    template = INTENTS[intent_name]["plan_template"]
    current_step = template[cursor["step_index"]]

    result = shopcore.run({"task": current_step["task"], "entities": state})
    state.update(result or {})

    cursor["step_index"] += 1
    state.pop("next_agent", None)
    return state


def shipstream_node(state: AgentState):
    cursor = state.get("cursor")
    if not cursor:
        return state

    intent_name = state.get("intent")
    template = INTENTS[intent_name]["plan_template"]
    current_step = template[cursor["step_index"]]

    result = shipstream.run({"task": current_step["task"], "entities": state})
    state.update(result or {})

    cursor["step_index"] += 1
    state.pop("next_agent", None)
    return state


def payguard_node(state: AgentState):
    cursor = state.get("cursor")
    if not cursor:
        return state

    intent_name = state.get("intent")
    template = INTENTS[intent_name]["plan_template"]
    current_step = template[cursor["step_index"]]

    result = payguard.run({"task": current_step["task"], "entities": state})
    state.update(result or {})

    cursor["step_index"] += 1
    state.pop("next_agent", None)
    return state


def caredesk_node(state: AgentState):
    cursor = state.get("cursor")
    if not cursor:
        return state

    intent_name = state.get("intent")
    template = INTENTS[intent_name]["plan_template"]
    current_step = template[cursor["step_index"]]

    result = caredesk.run({"task": current_step["task"], "entities": state})
    state.update(result or {})

    cursor["step_index"] += 1
    state.pop("next_agent", None)
    return state