import os
import sqlite3

import pandas as pd

from repo_abc import IProbeRepo

# library portion
class SqliteRepo(IProbeRepo):
    def __init__(self, sqlite_file: str):
        self.sqlite_file = sqlite_file
        self.conn = sqlite3.connect(sqlite_file)
        self.create_db()
        
    def create_db(self):
        try:
            self.conn.execute(f"""
                CREATE TABLE probes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR,
                    number INTEGER
                )""")
            self.conn.commit()
        except sqlite3.OperationalError:
            ...

    def add(self, name, number):
        self.conn.execute(f"""
            INSERT INTO probes(name, number)
            VALUES ("{name}", {number})
        """)
        self.conn.commit()
    
    def get_all_probes(self) -> pd.DataFrame:
        probe_column_names = \
            [row[1] for row in self.conn.execute(\
                "PRAGMA table_info(probes)").fetchall()]
            
        data = self.conn.execute("SELECT * FROM probes").fetchall()
        self.conn.commit()
        
        return pd.DataFrame(data, columns=probe_column_names)
        
    def delete(self, probe_ids: list[int]):
        for probe_id in probe_ids:
            self.conn.execute(f"""
                DELETE FROM probes
                WHERE id = {probe_id}
            """) 
        self.conn.commit()
        
# script portion --part run from command line
if __name__ == "__main__":
    sqlite_file = 'probes.sqlite'
    os.remove(sqlite_file)
    repo = SqliteRepo(sqlite_file)
    repo.add("probe1",1)
    repo.add("probe2",2)
    print(repo.get_all_probes())
    repo.delete([1]) 
    print(repo.get_all_probes())
