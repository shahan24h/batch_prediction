import json

input_file = r"\\172.23.218.118\allshares\documents\Batch Classify\ocr_source.json"
output_file = r"\\172.23.218.118\allshares\documents\Batch Classify\ocr_results.jsonl"

with open(input_file, "r", encoding="latin-1", errors="ignore") as f_in, \
     open(output_file, "w", encoding="utf-8") as f_out:

    buffer = ""
    for line in f_in:
        buffer += line.strip()
        try:
            obj = json.loads(buffer)
            json.dump(obj, f_out)
            f_out.write("\n")
            buffer = ""  # Reset buffer after success
        except json.JSONDecodeError:
            # Not complete JSON yet, keep reading
            continue

print(f"✅ Converted (ignoring errors) to JSONL: {output_file}")
