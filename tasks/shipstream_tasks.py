from db.connections import get_shipstream_conn

class ShipStreamAgent:
    """
    Deterministic agent for DB_ShipStream.
    Handles shipment tracking and logistics queries.
    """

    def run(self, payload: dict) -> dict:
        task = payload.get("task")
        entities = payload.get("entities", {})

        if task == "track_shipment":
            return self._track_shipment(entities)

        if task == "get_shipment_eta":
            return self._get_shipment_eta(entities)

        if task == "get_current_location":
            return self._get_current_location(entities)

        raise ValueError(f"Unknown ShipStream task: {task}")

    def _get_current_location(self, entities: dict) -> dict:
        order_id = entities.get("order_id")

        conn = get_shipstream_conn()
        cur = conn.cursor()

        cur.execute("""
            SELECT TOP 1 W.Location
            FROM Shipments S
            JOIN TrackingEvents T ON S.ShipmentID = T.ShipmentID
            JOIN Warehouses W ON T.WarehouseID = W.WarehouseID
            WHERE S.OrderID = ?
            ORDER BY T.EventTimestamp DESC
        """, order_id)

        row = cur.fetchone()
        conn.close()

        if not row:
            return {
                "shipment_location": "Location Not Available"
            }

        (location,) = row

        return {
            "shipment_location": location
        }
    def _track_shipment(self, entities: dict) -> dict:
        order_id = entities.get("order_id")

        conn = get_shipstream_conn()
        cur = conn.cursor()

        cur.execute("""
            SELECT TOP 1 W.Location, T.StatusUpdate
            FROM Shipments S
            JOIN TrackingEvents T ON S.ShipmentID = T.ShipmentID
            JOIN Warehouses W ON T.WarehouseID = W.WarehouseID
            WHERE S.OrderID = ?
            ORDER BY T.EventTimestamp DESC
        """, order_id)

        row = cur.fetchone()
        conn.close()

        if not row:
            return {}

        location, status = row

        return {
            "shipment_location": location,
            "shipment_status": status
        }

    def _get_shipment_eta(self, entities: dict) -> dict:
        order_id = entities.get("order_id")

        conn = get_shipstream_conn()
        cur = conn.cursor()

        cur.execute("""
            SELECT EstimatedArrival
            FROM Shipments
            WHERE OrderID = ?
        """, order_id)

        row = cur.fetchone()
        conn.close()

        if not row or not row[0]:
            return {}

        return {
            "estimated_arrival": str(row[0])
        }


