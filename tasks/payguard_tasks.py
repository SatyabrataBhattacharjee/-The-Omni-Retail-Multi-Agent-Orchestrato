from db.connections import get_payguard_conn

class PayGuardAgent:
    """
    Deterministic agent for DB_PayGuard.
    Handles payment, refund, and wallet-related queries.
    """

    def run(self, payload: dict) -> dict:
        task = payload.get("task")
        entities = payload.get("entities", {})

        if task == "check_refund":
            return self._check_refund(entities)

        if task == "get_wallet_balance":
            return self._get_wallet_balance(entities)

        raise ValueError(f"Unknown PayGuard task: {task}")

    def _check_refund(self, entities: dict) -> dict:
        order_id = entities.get("order_id")

        conn = get_payguard_conn()
        cur = conn.cursor()

        cur.execute("""
            SELECT TOP 1 Type, Amount
            FROM Transactions
            WHERE OrderID = ?
            ORDER BY TransactionID DESC
        """, order_id)

        row = cur.fetchone()
        conn.close()

        if not row:
            return {
                "refund_status": "No Transactions Found"
            }

        txn_type, amount = row

        if txn_type == "Refund":
            return {
                "refund_status": "Refunded",
                "refund_amount": float(amount)
            }

        return {
            "refund_status": "Not Initiated"
        }

    def _get_wallet_balance(self, entities: dict) -> dict:
        user_id = entities.get("user_id")

        conn = get_payguard_conn()
        cur = conn.cursor()

        cur.execute("""
            SELECT TOP 1 Balance, Currency
            FROM Wallets
            WHERE UserID = ?
        """, user_id)

        row = cur.fetchone()
        conn.close()

        if not row:
            return {
                "wallet_status": "Wallet Not Found"
            }

        balance, currency = row

        return {
            "wallet_balance": float(balance),
            "currency": currency
        }
