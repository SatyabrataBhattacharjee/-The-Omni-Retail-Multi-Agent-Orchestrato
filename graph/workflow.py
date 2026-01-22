# graph/workflow.py
from langgraph.graph import StateGraph
from graph.super_agent import super_agent_node
from graph.nodes import shopcore_node, shipstream_node, payguard_node, caredesk_node
from graph.state import AgentState

def build_workflow():
    graph = StateGraph(AgentState)

    graph.add_node("SuperAgent", super_agent_node)
    graph.add_node("ShopCore", shopcore_node)
    graph.add_node("ShipStream", shipstream_node)
    graph.add_node("PayGuard", payguard_node)
    graph.add_node("CareDesk", caredesk_node)

    graph.set_entry_point("SuperAgent")

    # Conditional routing from SuperAgent
    def stop_node(state):
        return state  # no-op

    graph.add_node("STOP", stop_node)

    graph.add_conditional_edges(
        "SuperAgent",
        lambda s: s.get("next_agent") or "STOP",
        {
            "ShopCore": "ShopCore",
            "ShipStream": "ShipStream",
            "PayGuard": "PayGuard",
            "CareDesk": "CareDesk",
            "STOP": "STOP",
        }
    )

    # After each agent, return to SuperAgent
    graph.add_edge("ShopCore", "SuperAgent")
    graph.add_edge("ShipStream", "SuperAgent")
    graph.add_edge("PayGuard", "SuperAgent")
    graph.add_edge("CareDesk", "SuperAgent")

    return graph.compile()