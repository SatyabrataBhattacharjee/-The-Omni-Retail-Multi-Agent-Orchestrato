# 🧠 Omni-Retail Multi-Agent Orchestrator  
### LangGraph · SQL Agents · LLM-Driven Planning

> A production-style **hierarchical multi-agent system** that unifies siloed e-commerce databases using **LangGraph orchestration**, **deterministic SQL agents**, and an **LLM-based planner**.

---

## ✨ Overview

Large e-commerce platforms often operate multiple isolated systems:

- 🛒 Orders & products  
- 🚚 Logistics & delivery tracking  
- 💳 Payments & transactions  
- 🎧 Customer support & tickets  

This project builds a **Super Agent** capable of answering **cross-domain customer queries** by orchestrating multiple **database-isolated agents** in real time.

---

## 🧩 Core Principle

> **LLMs plan. Deterministic agents execute. LangGraph orchestrates.**

- LLMs are used **only for planning**
- SQL execution is **fully deterministic**
- Each agent owns **exactly one database**
- No cross-database access
- Dependencies are enforced via state

---

## 🏗️ Architecture

User Query
↓
Planner (LLM)
↓
Execution Plan (JSON)
↓
LangGraph Orchestrator
├── ShopCore Agent
├── ShipStream Agent
├── PayGuard Agent
└── CareDesk Agent
↓
Synthesizer
↓
Final Response



---

## 🤖 Agents

| Agent | Responsibility | Database |
|------|---------------|----------|
| **ShopCore** | Orders, users, products | DB_ShopCore |
| **ShipStream** | Shipments, warehouses, tracking | DB_ShipStream |
| **PayGuard** | Payments, wallets, transactions | DB_PayGuard |
| **CareDesk** | Support tickets & messages | DB_CareDesk |

Each agent:
- Executes **parameterized SQL**
- Has **no knowledge of other systems**
- Is independently testable

---

## 🧠 Planner (LLM Role)

The planner converts natural language into a **strict execution plan**.

### Example User Query


### Planner Output (Strict JSON)

```json
[
  {
    "agent": "ShopCore",
    "task": {
      "intent": "find_order_by_product_name",
      "entities": {
        "product_name": "Gaming Monitor"
      }
    }
  },
  { "agent": "ShipStream", "depends_on": "OrderID" },
  { "agent": "PayGuard", "depends_on": "OrderID" },
  { "agent": "CareDesk", "depends_on": "UserID" }
]


Your order is at Bangalore Warehouse.
Payment of ₹24999.0 was processed successfully.
Your support ticket about 'Delivery Delay' is being handled.
