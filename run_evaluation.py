import json

with open("evaluation/dataset.json", "r") as f:
    dataset = json.load(f)

print("\nEVALUATION DATASET\n")

for i, item in enumerate(dataset):
    print(f"{i+1}. {item['prompt']}")

print("\nTotal Test Cases:", len(dataset))