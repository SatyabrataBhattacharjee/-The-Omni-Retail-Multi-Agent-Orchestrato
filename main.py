from planner.llm_planner import plan_from_query
from langgraph.executor import execute_plan

USER_ID = 1
USER_QUERY = "My package is late, I already asked for a refund, and I contacted support."

plan = plan_from_query(USER_QUERY)

final_state = execute_plan(
    user_id=USER_ID,
    plan=plan
)

print("\nFINAL STATE:")
print(final_state)
