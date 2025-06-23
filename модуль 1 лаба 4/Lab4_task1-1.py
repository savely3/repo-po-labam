import json

def task() -> float:
    """Calculate the weighted sum from JSON data."""
    total_sum = 0.0
    current_score = 0.0
    current_weight = 0.0
    
    with open("input.json", "r") as file:
        data = json.load(file)
    
    for item in data:
        current_score = item["score"]
        current_weight = item["weight"]
        total_sum += current_score * current_weight
    
    return round(total_sum, 3)

if __name__ == "__main__":
    print(task())
    
