import random

def cafe(size: str = "small", kind: str = "expresso", sugar: int = 2) -> None:
    price = 0
    match size:
        case "small":
            price += 1
        case "large":
            price += 1.5
        case _:
            pass
    
    match kind:
        case "expresso":
            price += 0.5
        case "cappucino":
            price += 0.7
        case _:
            pass
    
    match sugar:
        case 0:
            pass
        case _:
            price += sugar * 0.1
    
    return price

def num_note_to_alph_note(note: int) -> str:
    if note == 0:
        return "F"
    elif note < 3:
        return "E"
    elif note < 5:
        return "D"
    elif note < 7:
        return "C"
    elif note < 9:
        return "B"
    return "A"

def guess_num() -> None:
    random.seed()
    number = random.randint(0, 10)
    guess = input("guess the number between 0 and 10 included : ")
    return guess == number

def calcul_imc(taille: float, poids: float) -> str:
    imc = poids / taille**2
    if imc < 18.5:
        return "maigreur"
    if imc < 25:
        return "idéal"
    if imc < 30:
        return "surpoids"
    return "obésité"

def meal() -> None:
    petit_dejeuner = {
        1: "croissant",
        2: "pain et confiture"
    }

    dejeuner = {
        1: "steak frite",
        2: "carbonades flamendes"
    }

    diner = {
        1: "bouillon de légumes",
        2: "oeuf sur riz"
    }

    user_petit_dejeuner = int(input(f"Entrez {1} pour {petit_dejeuner[1]} ou {2} pour {petit_dejeuner[2]}"))
    user_dejeuner = int(input(f"Entrez {1} pour {dejeuner[1]} ou {2} pour {dejeuner[2]}"))
    user_diner = int(input(f"Entrez {1} pour {diner[1]} ou {2} pour {diner[2]}"))

    match user_petit_dejeuner:
        case 1:
            print(f"Votre petit déjeuner est : {petit_dejeuner[1]}")
        case 2:
            print(f"Votre petit déjeuner est : {petit_dejeuner[2]}")
        case _:
            print("Vous avez joué au malin, vous n'aurez rien !")

    match user_dejeuner:
        case 1:
            print(f"Votre petit déjeuner est : {dejeuner[1]}")
        case 2:
            print(f"Votre petit déjeuner est : {dejeuner[2]}")
        case _:
            print("Vous avez joué au malin, vous n'aurez rien !")

    match user_diner:
        case 1:
            print(f"Votre petit déjeuner est : {diner[1]}")
        case 2:
            print(f"Votre petit déjeuner est : {diner[2]}")
        case _:
            print("Vous avez joué au malin, vous n'aurez rien !")
    return

def citation() -> None:
    themes = ["Debord", "Hegel"]
    citation = {
        "Debord": [
            "Toute la vie des sociétés dans lesquelles règnent les conditions modernes de production s'annonce comme une immense accumulation de spectacles.",
            "L'imprécision du langage est désormais utile aux journalistes, et cela tombe bien, puisqu'ils seraient tous incapables d'écrire mieux.",
            "Pour savoir écrire, il faut avoir lu, et pour savoir lire, il faut savoir vivre."
        ],
        "Hegel": [
            "Le principe conceptuel que la violence se détruit elle-même a sa manifestation réelle en ceci qu'on annule une violence par une violence.",
            "La grande ruse, c'est que les choses soient comme elles sont.",
            "La chouette de Minerve prend son envol au crépuscule."
        ]
    }

    random.seed()
    user_input = input(f"Choisissez un auteur parmi : {", ".join(themes)} : ")
    match user_input:
        case "Debord":
            rnd = random.randint(0, len(citation["Debord"]) - 1)
            print(citation["Debord"][rnd])
        case "Hegel":
            rnd = random.randint(0, len(citation["Hegel"]) - 1)
            print(citation["Hegel"][rnd])
        case _:
            print("Il est bientôt midi")
 

def main() -> None:
    price = cafe()
    print(price)

    note = num_note_to_alph_note(9)
    print(note)

    guess = guess_num()
    print(f"You guessed {"succescfully" if guess else "wrong"}")

    imc = calcul_imc(1.84, 149)
    print(f"imc: {imc}")

    citation()
    return

if __name__ == "__main__":
    main()