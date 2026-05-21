def calcul_moyenne(numbers: list[float]) -> float:
    if len(numbers) == 0:
        return 0
    somme = sum(numbers)
    return somme / len(numbers)

def recherche_min(numbers: list[float]) -> float:
    if len(numbers) == 0:
        return 0
    
    minimum = numbers[0]
    for i in numbers:
        if i < minimum:
            minimum = i
    return minimum

def generer_email(prenom: str, nom: str, domain: str = "gmail.com") -> str:
    return f"{prenom}.{nom}@{domain}"

def compte_mots(text: str) -> int:
    return len(text.split(" "))

def convertir_temperature(celsius: float) -> float:
    return 32 + 9/5 * celsius

def nombres_pairs_impairs(nombres: list[int]) -> tuple[list[int], list[int]]:
    pairs = [nombre for nombre in nombres if not nombre % 2]
    impairs = [nombre for nombre in nombres if nombre % 2]
    return (pairs, impairs)

def reverse(text: str) -> str:
    return text[::-1]

def valider_mot_de_passe(text: str) -> bool:
    if len(text) < 8:
        return False

    haslowercase = False
    hasuppercase = False
    hasnumeric = False
    hasspecial = False
    
    for c in text:
        if c.isalpha():
            if c == c.lower():
                haslowercase = True
            else:
                hasuppercase = True
        elif c.isdigit():
            hasnumeric = True
        else:
            hasspecial = True
    return haslowercase and hasuppercase and hasnumeric and hasspecial

def main() -> None:
    result = calcul_moyenne([1, 2, 3, 4, 5])
    print(result)

    result = recherche_min([5, 3, 1, -1])
    print(result)

    result = generer_email("Friedrich", "Hegel")
    print(result)
    
    result = convertir_temperature(27)
    print(result)

    result = compte_mots("Toute la vie des sociétés dans lesquelles règnent les conditions modernes de production s'annonce comme une immense accumulation de spectacles.")
    print(result)
    
    result = nombres_pairs_impairs([1, 2, 3, 4, 5, 6])
    print(result)
    
    result = reverse("Toute la vie des sociétés dans lesquelles règnent les conditions modernes de production s'annonce comme une immense accumulation de spectacles.")
    print(result)
    
    result = valider_mot_de_passe("Techn0b€l")
    print(result)
    return

if __name__ == "__main__":
    main()