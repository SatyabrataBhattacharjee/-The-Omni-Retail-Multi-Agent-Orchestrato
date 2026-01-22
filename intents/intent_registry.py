INTENTS = {
    "TRACK_ORDER": {
        "intent_name": "TRACK_ORDER",
        "business_objective": "Determine current delivery status of an order",
        "required_context": ["user_id"],
        "resolvable_entities": ["order_id"],
        "clarification_rules": "Ask user to choose if multiple orders exist",
        "allowed_agents": ["ShopCore", "ShipStream"],
        "plan_template": [
            {
                "agent": "ShopCore",
                "task": "list_recent_orders"
            },
            {
                "agent": "ShipStream",
                "task": "track_shipment",
                "depends_on": "ShopCore"
            }
        ],
        "success_criteria": "Shipment status and ETA obtained",
        "failure_modes": [
            "NO_ACTIVE_ORDERS",
            "SHIPMENT_NOT_FOUND"
        ],
        "fallback_behavior": "Explain current order state to the user"
    },

    "GET_SHIPMENT_ETA": {
        "intent_name": "GET_SHIPMENT_ETA",
        "business_objective": "Retrieve the estimated arrival date of an order",
        "required_context": ["user_id"],
        "resolvable_entities": ["order_id"],
        "clarification_rules": "Ask user to choose if multiple orders exist",
        "allowed_agents": ["ShopCore", "ShipStream"],
        "plan_template": [
            {
                "agent": "ShopCore",
                "task": "list_recent_orders"
            },
            {
                "agent": "ShipStream",
                "task": "get_shipment_eta",
                "depends_on": "ShopCore"
            }
        ],
        "success_criteria": "Estimated arrival date obtained",
        "failure_modes": [
            "NO_ACTIVE_ORDERS",
            "SHIPMENT_NOT_FOUND",
            "ETA_NOT_AVAILABLE"
        ],
        "fallback_behavior": "Explain that the delivery date is not yet finalized"
    },
    "GET_ORDER_DETAILS": {
    "intent_name": "GET_ORDER_DETAILS",
    "business_objective": "Retrieve detailed information about an order",
    "required_context": ["user_id"],
    "resolvable_entities": ["order_id"],
    "clarification_rules": "Ask user to choose if multiple orders exist",
    "allowed_agents": ["ShopCore"],
    "plan_template": [
        {
            "agent": "ShopCore",
            "task": "list_recent_orders"
        },
        {
            "agent": "ShopCore",
            "task": "get_order_details",
            "depends_on": "ShopCore"
        }
    ],
    "success_criteria": "Order details successfully retrieved",
    "failure_modes": [
        "NO_ACTIVE_ORDERS",
        "ORDER_NOT_FOUND"
    ],
    "fallback_behavior": "Explain that order details cannot be retrieved at this time"
},    "CHECK_REFUND_STATUS": {
        "intent_name": "CHECK_REFUND_STATUS",
        "business_objective": "Check whether a refund has been initiated or completed",
        "required_context": ["order_id"],
        "allowed_agents": ["PayGuard"],
        "plan_template": [
            { "agent": "PayGuard", "task": "check_refund" }
        ],
        "failure_modes": ["NO_TRANSACTIONS_FOUND"]
    },    "GET_WALLET_BALANCE": {
        "intent_name": "GET_WALLET_BALANCE",
        "business_objective": "Retrieve user's wallet balance",
        "required_context": ["user_id"],
        "allowed_agents": ["PayGuard"],
        "plan_template": [
            { "agent": "PayGuard", "task": "get_wallet_balance" }
        ],
        "failure_modes": ["WALLET_NOT_FOUND"]
    },    "CHECK_SUPPORT_TICKET": {
        "intent_name": "CHECK_SUPPORT_TICKET",
        "business_objective": "Check the status of the user's latest support ticket",
        "required_context": ["user_id"],
        "allowed_agents": ["CareDesk"],
        "plan_template": [
            { "agent": "CareDesk", "task": "check_ticket" }
        ],
        "failure_modes": ["NO_ACTIVE_TICKETS"]
    },    "GET_SHIPMENT_LOCATION": {
        "intent_name": "GET_SHIPMENT_LOCATION",
        "business_objective": "Retrieve current shipment location",
        "required_context": ["order_id"],
        "allowed_agents": ["ShipStream"],
        "plan_template": [
            { "agent": "ShipStream", "task": "get_current_location" }
        ],
        "failure_modes": ["SHIPMENT_NOT_FOUND"]
    }
}






