import json

# read the existing data from the file, if it exists
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    # if the file doesn't exist, initialize an empty list
    data = []

# read the input text file and split it into lines
with open("input.txt", "r", encoding='utf-8') as f:
    lines = f.read().splitlines()

# initialize variables for the prompt and answer
prompt = ""
answer = ""

# loop through the lines and create a new dictionary for each prompt-completion pair
for line in lines:
    line = line.strip()
    if line.endswith("?"):
        # if the line is a question, save the previous prompt-answer pair, if any
        if prompt != "" and answer != "":
            data.append({"prompt": prompt, "input": "", "completion": answer})
            prompt = ""
            answer = ""
        prompt = line
    elif prompt != "":
        # if there is a pending prompt, add the line to the answer
        if answer != "":
            answer += "\n"
        answer += line

# save the last prompt-answer pair, if any
if prompt != "" and answer != "":
    data.append({"prompt": prompt, "input": "", "completion": answer})

# write the data to the JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
