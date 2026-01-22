ALLOWED_INTENTS = {
    "GET_ORDER_DETAILS",
    "TRACK_ORDER",
    "GET_SHIPMENT_LOCATION",
    "GET_SHIPMENT_ETA",
    "CHECK_REFUND_STATUS",
    "GET_WALLET_BALANCE",
    "CHECK_SUPPORT_TICKET"
}


def validate_execution_plan(plan: dict):
    if "execution_plan" not in plan:
        raise ValueError("Missing execution_plan")

    if not isinstance(plan["execution_plan"], list):
        raise ValueError("execution_plan must be a list")

    for step in plan["execution_plan"]:
        if "intent" not in step:
            raise ValueError("Each step must have an intent")

        if step["intent"] not in ALLOWED_INTENTS:
            raise ValueError(f"Invalid intent: {step['intent']}")
