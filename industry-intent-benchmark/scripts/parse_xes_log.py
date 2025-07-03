import os
import pandas as pd
from pm4py.objects.log.importer.xes.importer import apply as import_xes_log
from lxml.etree import XMLSyntaxError
from tqdm import tqdm

# === Configuration ===
XES_DIR = "data/logs/cleaned/"
OUTPUT_CSV = "data/parsed/parsed_log.csv"
os.makedirs("data/parsed", exist_ok=True)

# === Main Parsing Function ===
def parse_all_logs(xes_dir):
    all_rows = []
    files = []
    
    # Recursively collect all .xes files
    for root, _, filenames in os.walk(xes_dir):
        for f in filenames:
            if f.endswith(".xes"):
                files.append(os.path.join(root, f))
    
    if not files:
        print(f"❌ No .xes files found in {xes_dir}.")
        return pd.DataFrame()

    # Process each XES file
    for filepath in tqdm(files, desc="Parsing XES files"):
        try:
            log = import_xes_log(filepath)
        except XMLSyntaxError as e:
            print(f"⚠️ Skipping {filepath} due to XMLSyntaxError: {e}")
            continue
        except Exception as e:
            print(f"⚠️ Skipping {filepath} due to unexpected error: {e}")
            continue

        for trace in log:
            case_id = trace.attributes.get("concept:name", None)
            for evt in trace:
                row = {
                    "case_id": case_id,
                    "timestamp": evt.get("time:timestamp", None),
                    "activity": evt.get("concept:name", None),
                    "resource": evt.get("org:resource", None),
                    "sensor": evt.get("stream:concept:name", None),
                    "sensor_value": evt.get("stream:point", None),
                    "file": os.path.basename(filepath)
                }
                all_rows.append(row)

    return pd.DataFrame(all_rows)

# === Run Parser ===
if __name__ == "__main__":
    df = parse_all_logs(XES_DIR)

    if df.empty:
        print("❌ Parsed DataFrame is empty. Please check log quality.")
    else:
        df.sort_values(by=["case_id", "timestamp"], inplace=True)
        df.to_csv(OUTPUT_CSV, index=False)
        print(f"✅ Parsed {len(df)} events across {df['file'].nunique()} files.")
        print(f"📄 Output written to: {OUTPUT_CSV}")
