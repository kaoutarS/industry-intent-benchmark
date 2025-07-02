import pandas as pd

# Reload parsed sequences
df_sequences = pd.read_csv("data/mined/frequent_sequences.csv")

# Enriched mappings for semantic grounding
scope_keywords = {
    "pick": "warehouse handling",
    "transport": "intra-factory transport",
    "store": "storage operations",
    "unload": "inventory unloading",
    "mount": "assembly",
    "insert": "assembly",
    "remove": "disassembly",
    "qa": "quality inspection",
    "check": "quality inspection",
    "move": "line coordination",
    "cool": "temperature regulation",
    "heat": "temperature regulation"
}

outcome_templates = {
    "pick": "item retrieved",
    "transport": "item moved to target location",
    "store": "item stored in designated slot",
    "unload": "item removed from storage",
    "mount": "component mounted successfully",
    "insert": "component inserted into assembly",
    "remove": "component detached",
    "check": "quality check performed",
    "qa": "defect analysis completed",
    "move": "position updated",
    "cool": "temperature decreased",
    "heat": "heating process completed"
}

thing_keywords = {
    "vgr": "robotic arm",
    "hbw": "high-bay warehouse",
    "mnt": "manual station",
    "qa": "QA unit",
    "slt": "slide transfer",
    "sys": "control system"
}

activity_keywords = {
    "pick": "pick",
    "transport": "transport",
    "store": "store",
    "unload": "unload",
    "mount": "assemble",
    "insert": "insert",
    "remove": "disassemble",
    "check": "inspect",
    "qa": "inspect",
    "move": "move",
    "wait": "pause",
    "cool": "cool",
    "heat": "heat"
}

# Helper function
def enrich_intent(sequence):
    steps = sequence.split(" → ")
    activities = []
    things = set()
    scopes = set()
    outcomes = []

    for step in steps:
        parts = step.strip("/").split("/")
        if len(parts) < 2:
            continue
        system, action = parts[0], parts[-1]
        thing = thing_keywords.get(system, system)
        things.add(thing)

        activity = None
        for kw in activity_keywords:
            if kw in action:
                activity = activity_keywords[kw]
                scopes.add(scope_keywords.get(kw, "general operations"))
                outcomes.append(outcome_templates.get(kw, "subtask complete"))
                break

        if activity:
            activities.append(activity)

    return {
        "Scope of Service": ", ".join(sorted(scopes)),
        "Attribute": "operator with permission to modify equipment",
        "Things": ", ".join(sorted(things)),
        "Activity": " → ".join(activities),
        "Outcome": " → ".join(outcomes)
    }

# Apply to all
df_refined = df_sequences["sequence"].apply(enrich_intent)
df_structured_enriched = pd.DataFrame(df_refined.tolist())

import ace_tools as tools; tools.display_dataframe_to_user(name="Refined Structured Intents", dataframe=df_structured_enriched)
