# Pavage 2 couleur -> A(n,p) = n^p (n = 2 motifs, p = tirages|nombre de pavés)
# Nombre de motifs pour k pavés -> Fibonacci(k)
def pavage(longueur: int, couleurs: int = 2) -> int:
    if longueur == 0 :
        return 0
    if longueur == 1 :
        return couleurs
    if longueur == 2:
        return longueur * couleurs**2
    
    return 2 * pavage(longueur - 1) + 4 * pavage(longueur - 2)


def main() -> None:
    for i in range(10):
        print(pavage(i))
    return

if __name__ == "__main__":
    main()
