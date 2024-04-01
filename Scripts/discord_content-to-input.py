import json
import re

input_file = 'content.json'
output_file = 'output.txt'

# regex pattern to match usernames and timestamps
user_pattern = re.compile(r'@\w+\s?-?\s?\w+\s?\d+:\d+\s?(AM|PM)?')

# load json file
with open(input_file, 'r', encoding="utf-8") as f:
    data = json.load(f)

# extract content and filter out usernames and timestamps
qa_pairs = []
for item in data:
    content = item['content']
    # remove usernames and timestamps
    content = re.sub(user_pattern, '', content)
    # split into lines and filter out useless conversations
    lines = content.split('\n')
    q = None
    for line in lines:
        # ignore empty lines and those less than 10 characters
        if not line.strip() or len(line) < 10:
            continue
        # set the first non-empty line as question
        if not q:
            q = line.strip()
        # append the rest as answer
        else:
            qa_pairs.append({'question': q, 'answer': line.strip()})
            q = None

# save qa pairs to output file
with open(output_file, 'w', encoding="utf-8") as f:
    for qa in qa_pairs:
        f.write(f'Q: {qa["question"]}\n')
        f.write(f'A: {qa["answer"]}\n')
        f.write('\n')
