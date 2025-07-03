# Re-run everything after kernel reset
import os
import pandas as pd
from collections import Counter

# Load uploaded parsed log file
df = pd.read_csv("/mnt/data/parsed_log.csv")

# Drop NaNs and ensure sorting
df = df.dropna(subset=["case_id", "timestamp", "activity"])
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(by=["case_id", "timestamp"])

# Build sequences per case_id
grouped = df.groupby("case_id")["activity"].apply(list).reset_index()
sequences = grouped["activity"].tolist()

# Filter very short sequences
sequences = [seq for seq in sequences if len(seq) >= 3]

# Count N-grams (event chains)
def extract_ngrams(sequence, n=3):
    return [tuple(sequence[i:i+n]) for i in range(len(sequence) - n + 1)]

all_ngrams = []
for seq in sequences:
    for n in [3, 4, 5]:
        all_ngrams.extend(extract_ngrams(seq, n))

# Count top-N frequent patterns
ngram_counts = Counter(all_ngrams)
top_k = ngram_counts.most_common(50)

# Prepare dataframe for saving
df_top_sequences = pd.DataFrame([
    {"sequence": " → ".join(ng), "count": count}
    for ng, count in top_k
])

# Save results
os.makedirs("data/mined", exist_ok=True)
output_path = "data/mined/frequent_sequences.csv"
df_top_sequences.to_csv(output_path, index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Top Frequent Event Sequences", dataframe=df_top_sequences)
