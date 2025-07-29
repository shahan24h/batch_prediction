import json
import csv
import requests

API_URL = "https://gore-toolbar-tide-accessed.trycloudflare.com/predict"
input_file = r"ocr_results.jsonl"
output_file = r"classified_results.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["file_name", "prediction"])

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                doc = json.loads(line)
                file_name = doc.get("file_name", "unknown")
                ocr_text = doc.get("ocr_text", "")

                response = requests.post(API_URL, json={"text": ocr_text})
                response.raise_for_status()
                prediction = response.json().get("prediction")

                writer.writerow([file_name, prediction])
                print(f"[DONE] {file_name} → {prediction}")
            except Exception as e:
                print(f"[ERROR] {line[:50]}... | {e}")

print(f"\n✅ Classification completed. Results saved to {output_file}")
