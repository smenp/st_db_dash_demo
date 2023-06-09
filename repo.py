import json
import os
from uuid import uuid4

def add(name, number):
    probe_id = str(uuid4())
    probe = {"id": probe_id, "name": name, "number": number}

    json_probe = json.dumps(probe)

    os.makedirs("probes", exist_ok=True)
    with open(f"probes/probe-{probe_id}.json", "w") as f:
        f.write(json_probe)
