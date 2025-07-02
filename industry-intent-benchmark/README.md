# 🏭 Industry Intent Benchmark (IIBench)


This benchmark provides a reusable, few-shot evaluation dataset for **intent extraction in smart manufacturing** using real-world **IoT-enriched event logs**. It supports benchmarking LLMs on extracting structured industrial intents (Scope, Attribute, Things, Activity, Outcome) from natural language.

## 🔍 Motivation
While most intent benchmarks target conversational agents or general QA, this work focuses on **manufacturing-oriented semantic parsing**, where low-level logs are abstracted into high-level operational intents.

## 💡 Use Case
Derived from the publicly available [IoT Event Log for Smart Factories (Trier University)](https://figshare.com/articles/dataset/Dataset_An_IoT-Enriched_Event_Log_for_Process_Mining_in_Smart_Factories/20130794), we extract frequent patterns (mining frequent action chains from real factory logs) and annotate them using a 5-class structured intent model grounded in real process automation.

The 5-class structure is:
| Intent Element | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| `Scope`        | The operational scope (e.g., cooling, transport, inspection)      |
| `Attribute`    | A property or condition (e.g., temperature, weight, position)     |
| `Things`       | The equipment or resource involved (e.g., gantry robot, conveyor) |
| `Activity`     | The actual action to perform (e.g., move, inspect, align)         |
| `Outcome`      | The expected result (e.g., quality verified, part delivered)      |


## 🧪 Evaluation Pipeline
Includes:
- Pattern mining from XES logs
- Intent structuring + NL templating
- Few-shot LLM prompting
- Automated evaluation of JSON outputs

## 📦 Directory Structure
├── data/ # Source logs, parsed events, structured intents
├── scripts/ # Preprocessing, mining, prompting, evaluation
├── examples/ # Sample prompts and completions
├── docs/ # Use-case, schema, benchmark format
└── README.md
