import json
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

def normalize_field(val):
    if isinstance(val, list):
        return set([str(v).strip().lower() for v in val if v])
    elif isinstance(val, str):
        return set([val.strip().lower()]) if val.strip() else set()
    return set()

def compute_metrics(gt_list, pred_list):
    assert len(gt_list) == len(pred_list), "Mismatched list lengths!"
    fields = ["Scope", "Attribute", "Things", "Activity", "Outcome"]
    results = {field: {"TP": 0, "FP": 0, "FN": 0} for field in fields}

    for gt, pred in zip(gt_list, pred_list):
        for field in fields:
            gt_vals = normalize_field(gt.get(field, ""))
            pred_vals = normalize_field(pred.get(field, ""))

            tp = len(gt_vals & pred_vals)
            fp = len(pred_vals - gt_vals)
            fn = len(gt_vals - pred_vals)

            results[field]["TP"] += tp
            results[field]["FP"] += fp
            results[field]["FN"] += fn

    metrics = {}
    for field in fields:
        tp, fp, fn = results[field]["TP"], results[field]["FP"], results[field]["FN"]
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
        metrics[field] = {"Precision": precision, "Recall": recall, "F1": f1}
    return metrics

# === Load Data ===
with open("data/parsed/ground_truth_intents.json") as f:
    gt_intents = json.load(f)
with open("data/parsed/llm_outputs_simulated.json") as f:
    llm_intents = json.load(f)

# === Evaluate ===
metrics = compute_metrics(gt_intents, llm_intents)

# === Display ===
print("📊 Evaluation Results")
for field, scores in metrics.items():
    print(f"\n🔹 {field}")
    for metric, value in scores.items():
        print(f"   {metric}: {value:.3f}")
