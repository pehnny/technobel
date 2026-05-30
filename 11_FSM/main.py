class BinaryFSM:
    def __init__(self, modulo: int):
        self.binary = [0, 1]
        self.current_state = 0
        self.modulo = modulo
        
    def is_multiple(self, string: str) -> bool:
        if not string.isdigit():
            raise ValueError("argument string must only contain digits")
            
        for c in string:
            bit = int(c)
            if bit not in self.binary:
                raise ValueError("argument string must only contain '0's and '1's")
                
            self.current_state = (2 * self.current_state + bit) % self.modulo
        return not self.current_state
    
def main() -> None:
    fsm5 = BinaryFSM(5)
    string = "1010110100011111010101101101000011111010110101"
    answer = fsm5.is_multiple(string)
    print("La chaine de caractères", string, "est divisible par 5 ?", answer, sep="\t")
    return

if __name__ == "__main__":
    main()
