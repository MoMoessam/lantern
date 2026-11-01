import json

def load():
    try:
        with open('tasks.json', 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    

def save(data):
    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)