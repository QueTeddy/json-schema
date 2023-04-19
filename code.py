
import json

with open('data/data_2.json', 'r') as f:
    data = json.load(f)


def get_schema(json_obj):
    schema = {}
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if key == "attributes":
                continue
            if isinstance(value, str):
                schema[key] = {
                    "type": "string",
                    "description": "",
                    "tag": "",
                },
            elif isinstance(value, int):
                schema[key] = {
                    "type": "integer",
                    "description": "",
                    "tag": "",
                }
            elif isinstance(value, list) and value and isinstance(value[0], dict):
                schema[key] = {
                    "type": "array",
                    "description": "",
                    "items": get_schema(value[0]),
                    "tag": "",
                    "required": False,
                }
            elif isinstance(value, list) and value and isinstance(value[0], str):
                schema[key] = {
                    "type": "array",
                    "description": "",
                    "tag": "",
                    "items": {"type": "string", "enum": value},
                    "required": False,
                }
            else:
                schema[key] = {
                    "type": "object",
                    "tag": "",
                    "description": "",
                    "properties": get_schema(value),
                    "required": False,
                }
    return schema


schema = get_schema(data)
print(json.dumps(schema, indent=4))
