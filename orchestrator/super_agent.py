from intents.intent_registry import INTENTS

from tasks.shopcore_tasks import ShopCoreAgent
from tasks.shipstream_tasks import ShipStreamAgent
from tasks.payguard_tasks import PayGuardAgent
from tasks.caredesk_tasks import CareDeskAgent


class SuperAgent:
    def __init__(self):
        self.agents = {
            "ShopCore": ShopCoreAgent(),
            "ShipStream": ShipStreamAgent(),
            "PayGuard": PayGuardAgent(),
            "CareDesk": CareDeskAgent(),
        }

    def execute_plan(self, user_id: int, execution_plan: list) -> dict:
        context = {"user_id": user_id}
        final_state = {}
        executed_intents = []

        for step in execution_plan:
            intent_name = step["intent"]

            if intent_name not in INTENTS:
                raise ValueError(f"Unknown intent: {intent_name}")

            intent_def = INTENTS[intent_name]
            print(f"[INTENT] {intent_name}")

            # ---- Dependency validation ----
            required = intent_def.get("required_context", [])
            missing = [r for r in required if r not in context]

            if missing:
                return {
                    "intent": intent_name,
                    "status": "MISSING_DEPENDENCY",
                    "missing": missing
                }

            # ---- Execute plan template ----
            for task_step in intent_def["plan_template"]:
                agent_name = task_step["agent"]
                task_name = task_step["task"]

                agent = self.agents.get(agent_name)
                if not agent:
                    raise ValueError(f"Agent not registered: {agent_name}")

                payload = {
                    "task": task_name,
                    "entities": context
                }

                result = agent.run(payload)

                # ---- Special handling for order resolution ----
                if task_name == "list_recent_orders":
    # If we already have an order_id in context, skip asking again
                    if "order_id" in context:
                        continue

                    orders = result.get("orders", [])
                    if not orders:
                        return {
                            "intent": intent_name,
                            "status": "NO_ACTIVE_ORDERS"
                        }

                    # Show all orders once
                    print("\nAvailable Orders:")
                    print("{:<10} {:<25} {:<15}".format("OrderID", "Product", "Date"))
                    print("-" * 55)
                    for o in orders:
                        print("{:<10} {:<25} {:<15}".format(
                            o["order_id"], o["product_name"], o.get("date", "N/A")
                        ))

                    choice = input("\nEnter the OrderID of the order you want to continue with: ").strip()
                    selected = next((o for o in orders if str(o["order_id"]) == choice), None)
                    if not selected:
                        print("Invalid selection. Please try again.")
                        return {
                            "intent": intent_name,
                            "status": "INVALID_SELECTION",
                            "options": [o["order_id"] for o in orders]
                        }

                    # Save chosen order in context for reuse
                    order = selected
                    context["order_id"] = order["order_id"]
                    context["product_name"] = order["product_name"]
                    final_state.update({
                        "order_id": order["order_id"],
                        "product_name": order["product_name"]
                    })
                    continue

                # ---- Normal task ----
                context.update(result)
                final_state.update(result)

            executed_intents.append(intent_name)

        return {
            "executed_plan": executed_intents,
            **final_state
        }