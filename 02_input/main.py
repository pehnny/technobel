def parsenum(text: str) -> float:
    try:
        return float(text)
    except:
        return 0

def main() -> None:
    # 1.
    name = input("Entrez votre nom de famille : ")
    first_name = input("Entrez votre prénom : ")
    print("Bonjour ", name, first_name, sep="*-*")
    # 2.
    print("Toute", "la", "vie", "des", "sociétés", "dans", "lesquelles", "règnent", "les", "conditions", "modernes", "de", "production", "s'annonce", "comme", "une", "immense", "accumulation", "de", "spectacles.", sep="$$\t",end="$$\n")
    # 3.
    first_input = input("Quel jour sommes-nous ?")
    second_input = input("Quel est votre prénom ?")
    print(f"{first_input}{second_input}")
    # 4.
    first_number = parsenum(input("Entrez un nombre : "))
    second_number = parsenum(input("Entrez un nombre : "))
    print(sum([first_number, second_number]), end="$$\n")
    # 5.
    print("big brother", "is watching", "you", sep="xXx", end="**")
    return    

if __name__ == "__main__":
    main()