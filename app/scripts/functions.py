# recive un nombre (string)
# regresa una frase (string)
def Greeting(name : str) -> str:
    if name:
        print(f"Hello {name}")
    else:
        pass

def get_name() -> str:
    name = input("Name: ")
    if len(name) == 0:
        print("Name cant be empty")
        return None
    return name