import re
class Espreg :
    def __init__(self, espressione_regolare:str):
        self.espressione_regolare = espressione_regolare
    def match(self, stringa:str) -> bool:
        return re.fullmatch(self.espressione_regolare, stringa) is not None
    
def main():
    espreg = Espreg(r"(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])\/(19[0-9][0-9]|20[0-1][0-9]|20[2][0-5])")
    stringa = input("Inserisci una stringa da confrontare: ")
    if espreg.match(stringa):
        print("La stringa corrisponde all'espressione regolare.")
    else:
        print("La stringa non corrisponde all'espressione regolare.")
if __name__ == "__main__":
    main()

