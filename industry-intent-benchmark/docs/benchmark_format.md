## Benchmark Format

This document outlines the structure and principles behind the Industry-Intent Benchmark, designed to evaluate LLMs in extracting structured operational intents from smart manufacturing event sequences.

+  To provide a reproducible and semantically rich benchmark that:
- Translates low-level IoT event traces into high-level intents.
- Evaluates LLMs on structured semantic parsing within a constrained ontology.
- Enables zero-shot/few-shot prompting with gold-aligned validation.


Each prompt input is a **natural language event description** derived from frequent activity chains in the smart factory log.

Example:
```text
The gantry robot transports the component to the quality station where it is inspected and logged.
```

+ Output Format: the LLMs are expected to generate a structured 5 elements JSON intent:

{
  "Scope": "transport",
  "Attribute": ["position", "status"],
  "Things": ["gantry robot", "component", "quality station"],
  "Activity": ["transport", "inspect", "log"],
  "Outcome": "component inspected and recorded"
}

+ Each gold intent was generated by domain-aware annotators based on:

Contextual abstraction of sensor-augmented actions.

Ontological grounding per our 5-class schema.

Industrial relevance of Scope and Outcome.

+ The benchmark is:
  - Domain-adaptable (other factories can plus inXES logs)
  - Ptompt-style agnostic
  - Extendable to new schema slots
