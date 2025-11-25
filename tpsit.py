import re
class Espreg :
    def __init__(self, espressione_regolare:str):
        self.espressione_regolare = espressione_regolare
    def match(self, stringa:str) -> bool:
        return re.fullmatch(self.espressione_regolare, stringa) is not None
    
def main():
    espressione = input("Inserisci un'espressione regolare: ")
    espreg = Espreg(espressione)
    stringa = input("Inserisci una stringa da confrontare: ")
    if espreg.match(stringa):
        print("La stringa corrisponde all'espressione regolare.")
    else:
        print("La stringa non corrisponde all'espressione regolare.")
if __name__ == "__main__":
    main()

