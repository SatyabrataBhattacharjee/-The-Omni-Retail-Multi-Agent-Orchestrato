from db.connections import get_shopcore_conn

class ShopCoreAgent:
    def run(self, payload: dict) -> dict:
        task = payload["task"]
        entities = payload["entities"]

        conn = get_shopcore_conn()
        cur = conn.cursor()

        if task == "list_recent_orders":
            user_id = entities["user_id"]

            # Fetch ALL orders for the user, sorted by date (most recent first)
            cur.execute("""
                SELECT
                    o.OrderID,
                    p.Name,
                    o.Status,
                    o.OrderDate
                FROM Orders o
                JOIN Products p ON o.ProductID = p.ProductID
                WHERE o.UserID = ?
                ORDER BY o.OrderDate DESC
            """, (user_id,))

            rows = cur.fetchall()
            conn.close()

            if not rows:
                return {"orders": []}

            # Return all orders as a list
            orders = []
            for row in rows:
                orders.append({
                    "order_id": row[0],
                    "product_name": row[1],
                    "status": row[2],
                    "date": str(row[3])  # convert datetime to string for display
                })

            return {"orders": orders}

        elif task == "get_order_details":
            order_id = entities["order_id"]

            cur.execute("""
                SELECT
                    o.OrderID,
                    p.Name,
                    o.Status,
                    o.OrderDate
                FROM Orders o
                JOIN Products p ON o.ProductID = p.ProductID
                WHERE o.OrderID = ?
            """, (order_id,))

            row = cur.fetchone()
            conn.close()

            if not row:
                return None

            return {
                "order_id": row[0],
                "product_name": row[1],
                "order_status": row[2],
                "date": str(row[3])
            }

        else:
            conn.close()
            raise ValueError(f"Unknown ShopCore task: {task}")