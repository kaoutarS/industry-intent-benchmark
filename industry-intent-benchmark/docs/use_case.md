## Smart Factory Use Case
This benchmark is based on the real-world production data of a smart factory environment.
The goal is to extract **abstract operational intents** from raw event sequences logged by cyber-physical systems.

## Factory Environment

**Dataset**: IoT-Enriched Event Log for Smart Factories  
**Source**: Trier University, public on Figshare  
**Sensors involved**:
- Vision systems (QA)
- RFID/Barcode scanners (identification)
- Robotic motion encoders (gantry robot)
- Conveyor and buffer position trackers
- System control signals (via sys/** logs)

## Process Modules (Trace Prefix Mapping)

| Prefix |          Module                |       Description        |
|--------|--------------------------------|--------------------------|
| /vgr/  | Vertical Gantry Robot          | Movement & pickup        |
| /mnt/  | Manual Station                 | Human transfer zone      |
| /qa/   | Quality Assurance              | Inspection               |
| /slt/  | Slide Transfer                 | Conveyor path            |
| /hbw/  | High Bay Warehouse             | Storage unit             |
| /sys/  | System Controller              | Scheduling, routing logic|

Traditional process mining stops at control-flow visualization and conformance checking. While intent-based processing enables:
- Semantic  translation of logs into business objectives
- Enrichment for LLM applications (reasoning, QA, simulation)
- Evaluation of process-aware language models

 1. We mine frquent trace patterns such as: /vgr/pick → /mnt/place → /qa/inspect
 2. Then we abstract them into high-level intents (transform them into natural language sentences).
