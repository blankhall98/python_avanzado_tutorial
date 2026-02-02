from typing import Dict

class Wallet:

    def __init__(self, input_data : Dict):
        self.data = input_data

    def compound(self,time: int, instrument: str) -> float:
        fin_data = self.data["financial data"]
        s = fin_data["savings"]
        i = fin_data["invensting instruments"][instrument]
        return s*(1+i)**time
        