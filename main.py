import sys
import json
from code import get_schema

if len(sys.argv) != 3:
    print("Usage: python main.py <input_json_file_path> <output_schema_file_path>")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# Load input JSON data from file
with open(input_file_path, 'r') as f:
    data = json.load(f)

# Generate schema based on input JSON data
schema = get_schema(data)

# Save schema to output file
with open(output_file_path, 'w') as f:
    json.dump(schema, f, indent=4)

print(f"Schema generated successfully and saved to {output_file_path}")
