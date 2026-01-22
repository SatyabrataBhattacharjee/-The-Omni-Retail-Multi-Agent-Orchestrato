# Omni-Retail Multi-Agent Orchestrator (LangGraph + SQL)

A hierarchical, agentic orchestration system that unifies customer support across multiple siloed enterprise databases using LangGraph, deterministic SQL agents, and an LLM-based planner.

This project demonstrates how complex, multi-domain customer queries can be resolved by coordinating independent, database-isolated agents under a single intelligent orchestrator.

🚀 Problem Statement

Large e-commerce platforms often operate multiple isolated systems:

Orders & products

Logistics & shipment tracking

Payments & refunds

Customer support & tickets

Customer support agents usually cannot see across these silos, making it difficult to answer real-world questions like:

“I ordered a product last week, it hasn’t arrived, I paid already, and I opened a support ticket. What’s the current status?”

This project solves that problem using an agentic architecture.

🧠 Solution Overview

The system is built as a Hierarchical Multi-Agent System:

🔹 One Orchestrator (Planner)

Interprets natural-language user queries

Generates a structured execution plan

Decides which agents to invoke and in what order

Uses an LLM only for planning, not execution

🔹 Four Specialized Sub-Agents (Workers)

Each agent:

Owns exactly one database

Executes deterministic SQL

Cannot access other databases

Agent	Responsibility	Database
ShopCore	Orders, users, products	DB_ShopCore
ShipStream	Shipments, warehouses, tracking	DB_ShipStream
PayGuard	Payments, wallets, transactions	DB_PayGuard
CareDesk	Support tickets & messages	DB_CareDesk
🔹 LangGraph Orchestration

Each agent is a LangGraph node

Shared state flows through the graph

Dependencies (OrderID, UserID) are enforced automatically

No manual orchestration logic
