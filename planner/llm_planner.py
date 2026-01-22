def plan_from_query(user_query: str) -> dict:
    """
    Simulated LLM output.
    Replace later with real LLM call.
    """
    return {
        "execution_plan": [
            {"intent": "GET_ORDER_DETAILS"},
            {"intent": "TRACK_ORDER"},
            {"intent": "GET_SHIPMENT_LOCATION"},
            {"intent": "GET_SHIPMENT_ETA"},
            {"intent": "CHECK_REFUND_STATUS"},
            {"intent": "GET_WALLET_BALANCE"},
            {"intent": "CHECK_SUPPORT_TICKET"}
        ]
    }
