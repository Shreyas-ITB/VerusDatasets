import json

# read the existing data from the file, if it exists
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    # if the file doesn't exist, start with an empty list
    data = []

while True:
    prompt = input("Enter the prompt: ")
    completion = input("Enter the completion: ")

    # create a dictionary to store the prompt, input, and completion
    data.append({"prompt": prompt, "input": "", "completion": completion})

    # ask the user if they want to continue adding data
    choice = input("Do you want to add more data? (Y/N): ")
    if choice.lower() == "n":
        break

# write the updated data to the JSON file
with open("data.json", "w") as f:
    json.dump(data, f)