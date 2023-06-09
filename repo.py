import json

def save(name, number):
    probe = {"name": name, "number": number}

    json_probe = json.dumps(probe)

    with open("probe.json", "w") as f:
        f.write(json_probe)
