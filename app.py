from app.scripts.functions import Greeting, get_name
from app.models.objects import Wallet

if __name__ == "__main__":

    name = get_name()
    
    data = {
        'name': name,
        "financial data": {
            "savings": 10000,
            "invensting instruments": {
                "BOND": 0.08
            }
        }
    }

    w = Wallet(input_data=data)

    print(w.data)
    print(w.compound(10,"BOND"))