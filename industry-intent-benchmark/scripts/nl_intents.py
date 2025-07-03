import random

# Define templates for phrasing natural language intents
nl_templates = [
    "Please {activity} the {thing} to support {scope}, expecting {outcome}.",
    "The system must perform {activity} on the {thing} as part of {scope} to achieve {outcome}.",
    "Schedule {activity} using the {thing} for {scope} purposes with the outcome being {outcome}.",
    "Use {thing} to execute {activity} related to {scope}, targeting {outcome}.",
    "Carry out {activity} tasks through {thing} for the objective of {scope}, resulting in {outcome}."
]

# Generate few-shot natural language intents
def generate_nl_intents(df):
    nl_intents = []
    for _, row in df.iterrows():
        activity = row["Activity"]
        thing = row["Things"]
        scope = row["Scope of Service"]
        outcome = row["Outcome"]

        template = random.choice(nl_templates)
        intent = template.format(activity=activity, thing=thing, scope=scope, outcome=outcome)
        nl_intents.append(intent)

    return nl_intents

# Apply transformation
df_structured_enriched["NL_Intent"] = generate_nl_intents(df_structured_enriched)

import ace_tools as tools; tools.display_dataframe_to_user(name="Few-Shot NL Intents", dataframe=df_structured_enriched[["Activity", "Things", "Scope of Service", "Outcome", "NL_Intent"]])
