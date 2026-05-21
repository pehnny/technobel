import random

def is_prime_number(number: int) -> bool:
    for i in range(2, number):
        if not number % i:
            return False
    return True

def is_major(age: int) -> bool:
    return True if age > 17 else False

def guess_game() -> None:
    random.seed()
    number = random.randint(1, 100)
    while answer := input("Devinez un nombre entre 1 et 100. 'stop' pour arrêter : ") != "stop":
        try:
            guess = int(answer)
            if guess == number:
                print("Vous avez trouvé !")
                return
        except:
            pass
        finally:
            print("Vous vous êtes trompé !")
    return

def printc(text: str) -> None:
    for c in text:
        print(c)
    return

def order_cafe() -> None:
    total_price = 0

    def cafe(size: str = "small", kind: str = "expresso", sugar: int = 2) -> int:
        price = 0

        size = input("Taille ? 'small' ou 'large'")
        match size:
            case "small":
                price += 1
            case "large":
                price += 1.5
            case _:
                pass

        kind = input("Type ? 'expresso' ou 'capuccino'")
        match kind:
            case "expresso":
                price += 0.5
            case "capuccino":
                price += 0.7
            case _:
                pass

        sugar = input("Combien de sucre ?")
        try:
            n_sugar = int(sugar)
            match n_sugar:
                case 0:
                    pass
                case _:
                    price += n_sugar * 0.1
        except:
            pass
        return price
    
    while answer := input("'stop' pour arrêter") != "stop":
        price = cafe()
        print(f"Ca fera {price}€")
        print("Autre chose ?")
        total_price += price 
    
    print(f"Ca fera {total_price}")
    return

def print_reverse(text: str) -> None:
    s_reverse = ""
    for i in range(len(text)-1, -1, -1):
        s_reverse += text[i]
    print(s_reverse)
    return

def main() -> None:
    prime_number = []
    number = 2
    while len(prime_number) < 100:
        if is_prime_number(number):
            prime_number.append(number)
        number += 1
    
    print(*prime_number)

    major = is_major(20)
    match major:
        case True:
            print("Bonjour adulte")
        case False:
            print("Au revoir enfant")
            
    guess_game()

    printc("Toute la vie des sociétés dans lesquelles règnent les conditions modernes de production s'annonce comme une immense accumulation de spectacles.")

    order_cafe()

    print_reverse("bonjour")
    return

if __name__ == "__main__":
    main()