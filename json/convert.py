import json

input_path = "comments.json"
output_path = "comments_nd.json"

# Load the JSON array
with open(input_path, "r") as f:
    data = json.load(f)

# Write newline-delimited JSON
with open(output_path, "w") as f:
    for item in data:
        f.write(json.dumps(item) + "\n")

print("Converted to newline-delimited JSON format.")
