# Pavage 2 couleur -> A(n,p) = n^p (n = 2 motifs, p = tirages|nombre de pavés)
# Nombre de motifs pour k pavés -> Fibonacci(k)
def pavage(longueur: int, motifs: int = 2, largeur: int = 2, motif_size: tuple[int, int] = (1, 2)) -> int:
    if longueur == 1 :
        return motifs
    
    return motifs**longueur* motifs**(longueur-1)


def main() -> None:
    print(pavage(4))
    return

if __name__ == "__main__":
    main()
