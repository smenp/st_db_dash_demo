import json
import os
import duckdb
import pandas
from abc import ABC, abstractmethod
import ipdb
from uuid import uuid4

class IProbeRepo(ABC):

    @abstractmethod 
    def add(self, name, number):
        ...

    @abstractmethod 
    def get_all_probes(self):
        ...

    @abstractmethod 
    def delete(self, probe_ids):
        ...

class JsonDuckDBProbeRepo(IProbeRepo):

    def add(self, name, number):
        probe_id = str(uuid4())
        probe = {"id": probe_id, "name": name, "number": number}

        json_probe = json.dumps(probe)

        os.makedirs("probes", exist_ok=True)
        with open(f"probes/probe-{probe_id}.json", "w") as f:
            f.write(json_probe)

    def get_all_probes(self):
        try:
            probe_table = duckdb.sql("SELECT * FROM 'probes/probe-*.json'")
        except duckdb.IOException:
            return pandas.DataFrame()
         
        probe_df = probe_table.to_df()
        return probe_df

    def delete(self, probe_ids):
#    ipdb.set_trace()
        print(f'Trying to delete:\n{probe_ids}')
        for probe in probe_ids:
            os.remove(f"probes/probe-{str(probe)}.json")