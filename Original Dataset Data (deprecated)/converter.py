import json
import random

# Load the data from the input file
with open('data.json') as f:
    data = json.load(f)

# Convert the data to the desired format
converted_data = []
for i, item in enumerate(data):
    random_number = random.randint(100000, 999999)
    conversation = {
        "from": "human",
        "value": f"<image>\n{item['prompt']}"
    }
    converted_item = {
        "id": f"{'0' * 6}{random_number}",
        "image": f"{'0' * 6}{random_number}.jpg",
        "conversations": [conversation]
    }
    if item['completion']:
        gpt_conversation = {
            "from": "gpt",
            "value": item['completion']
        }
        converted_item['conversations'].append(gpt_conversation)
    converted_data.append(converted_item)

# Save the converted data to a new JSON file
with open('output.json', 'w') as f:
    json.dump(converted_data, f, indent=2)
