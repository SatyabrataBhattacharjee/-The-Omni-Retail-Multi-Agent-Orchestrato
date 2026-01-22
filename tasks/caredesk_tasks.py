from db.connections import get_caredesk_conn

class CareDeskAgent:
    """
    Deterministic agent for DB_CareDesk.
    Handles customer support tickets.
    """

    def run(self, payload: dict) -> dict:
        task = payload.get("task")
        entities = payload.get("entities", {})

        if task == "check_ticket":
            return self._check_ticket(entities)

        raise ValueError(f"Unknown CareDesk task: {task}")

    def _check_ticket(self, entities: dict) -> dict:
        user_id = entities.get("user_id")

        conn = get_caredesk_conn()
        cur = conn.cursor()

        cur.execute("""
            SELECT TOP 1 TicketID, IssueType
            FROM Tickets
            WHERE UserID = ?
            ORDER BY TicketID DESC
        """, user_id)

        row = cur.fetchone()
        conn.close()

        if not row:
            return {
                "ticket_status": "No Active Tickets"
            }

        ticket_id, issue_type = row

        return {
            "ticket_id": ticket_id,
            "ticket_status": "Open",
            "issue_type": issue_type
        }
