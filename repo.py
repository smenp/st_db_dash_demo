import json
import os
import duckdb
import pandas
from uuid import uuid4

def add(name, number):
    probe_id = str(uuid4())
    probe = {"id": probe_id, "name": name, "number": number}

    json_probe = json.dumps(probe)

    os.makedirs("probes", exist_ok=True)
    with open(f"probes/probe-{probe_id}.json", "w") as f:
        f.write(json_probe)

def get_all_probes():
    try:
        probe_table = duckdb.sql("SELECT * FROM 'probes/probe-*.json'")
    except duckdb.IOException:
        return pandas.DataFrame()
     
    probe_df = probe_table.to_df()
    return probe_df