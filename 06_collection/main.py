import random

def main() -> None:
    random.seed()
    rnd_list = []
    for i in range(10):
        rnd_list.append(random.randint(1, 100))
    print(sum(rnd_list))

    first_name = input("Entrez votre prénom : ")
    name = input("Entrez votre nom : ")
    data = (first_name, name)
    print(*data, sep="\n")

    random.seed()
    set1 = []
    set2 = []
    for i in range(10):
        set1.append(random.randint(1, 20))
        set2.append(random.randint(1, 20))
    print(set1, set2)
    intersection = set(set1).intersection(set(set2))
    print(intersection)

    fruits = {
        "pomme": 0.5,
        "avocat": 1,
        "noix": 0.3
    }
    choice = input("Choisissez un fruit parmi : " + " ".join(fruits.keys()))
    match choice:
        case "pomme":
            print(fruits["pomme"], "€")
        case "avocat":
            print(fruits["avocat"], "€")
        case "noix":
            print(fruits["noix"], "€")
        case _:
            print("Vous n'avez sélectionné aucun des fruits demandés.")

    listtuple = [
        ("Simon", 31), 
        ("Bernard", 14),
        ("Bertrand", 62),
    ]
    oldest = max(listtuple, key = lambda x: x[1])
    print(oldest)

    random.seed()
    nombres = []
    for i in range(10):
        nombres.append(random.randint(1, 50))
    print(nombres)
    nombres = list(filter(lambda x: not x%2, nombres))
    print(nombres)

    mots = ["bonjour", "bonjour", "banane", "chocolat", "bonjour", "chocolat"]
    print(set(mots))

    cours = {
        "idéalisme allemand": ["Robert", "José", "Karl"],
        "phénoménologie": ["David", "Martin", "Herbert"],
        "analyse réelle": ["Henri", "Isaac", "Bernahard"]
    }
    choice = input("Choisissez un cours parmi : " + " ".join(cours.keys()))
    match choice:
        case "idéalisme allemand":
            print(cours["idéalisme allemand"])
        case "phénoménologie":
            print(cours["phénoménologie"])
        case "analyse réelle":
            print(cours["analyse réelle"])
        case _:
            print("Vous n'avez sélectionné aucun des cours existants.")
    
    commandes = [
        ("agraffeuse", 1),
        ("recharge", 10),
        ("tasse", 2)
    ]
    prix = {
        "agraffeuse": 10,
        "recharge": 1,
        "tasse": 2.5
    }
    total = 0
    for marchandise, quantite in commandes:
        total += quantite * prix.get(marchandise)
    print("prix total : ", total)

    entreprise = [
        {
            "nom": "Bernard",
            "salaire": 1700,
            "département": "data"
        },
                {
            "nom": "Robert",
            "salaire": 1900,
            "département": "data"
        },
                {
            "nom": "Pierre",
            "salaire": 1650,
            "département": "analyst"
        }
    ]
    salaire_total = sum(map(lambda x: x.get("salaire"), entreprise))
    salaire_moyen = salaire_total / len(entreprise)
    print(f"Salaire total : {salaire_total}", f"Salaire moyen : {salaire_moyen}")
    department = set(map(lambda x: x["département"], entreprise))
    for i in list(department):
        salaire_department = list(map(lambda x: x.get("salaire"), filter(lambda x: x.get("département") == i, entreprise)))
        salaire_moyen = sum(salaire_department) / len(salaire_department)
        print("Salaire moyen du département ", i, " : ", salaire_moyen)
    return

if __name__ == "__main__":
    main()