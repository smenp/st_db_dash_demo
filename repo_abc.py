from abc import ABC, abstractmethod

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
        
        