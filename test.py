# test.py
from graph.executor import run_plan

def main():
    # Define a sample execution plan
    execution_plan = {
        "user_id": 1,
        "plan": [
            { "intent": "GET_ORDER_DETAILS" },
            { "intent": "TRACK_ORDER" },
            { "intent": "GET_SHIPMENT_LOCATION" },
            { "intent": "GET_SHIPMENT_ETA" },
            { "intent": "CHECK_REFUND_STATUS" },
            { "intent": "GET_WALLET_BALANCE" }
        ]
    }


    # Run the plan through your LangGraph runner
    result = run_plan(user_id=1, execution_plan=execution_plan)

    # Print results nicely
    print("\n=== Execution Result ===")
    print("Executed Plan:", result.get("executed_plan"))
    print("Final State:", {k: v for k, v in result.items() if k not in ["executed_plan", "per_intent"]})
    print("Per-Intent Outputs:", result.get("per_intent"))

if __name__ == "__main__":
    main()