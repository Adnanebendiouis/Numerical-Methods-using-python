def afficher_matrice(T):
    N = len(T)
    for i in range(N):
        for j in range(len(T[i])):  
            print(f"{T[i][j]:.2f}", end=" ")
        print()


def lireMatrice(T, l, c):
    for i in range(l):
        for j in range(c):
            T[i][j] = float(input(f"Entrer la case ({i},{j}): "))
    return T


def lireVecteur(V, N):
    for i in range(N):
        V[i] = float(input(f"Entrer l'élément {i}: "))


def afficher_vecteur(V):
    N = len(V)
    for i in range(N):
        print(f"{V[i]:.2f}", end=" ")
    print()


def gauss_pivot_total(A, b):
    n = len(A)
    for k in range(n - 1):
        pivot = abs(A[k][k])
        pivot_row, pivot_col = k, k
        for i in range(k, n):
            for j in range(k, n):
                if abs(A[i][j]) > pivot:
                    pivot = abs(A[i][j])
                    pivot_row, pivot_col = i, j
        if pivot_row != k:
            A[k], A[pivot_row] = A[pivot_row], A[k]
            b[k], b[pivot_row] = b[pivot_row], b[k]
        if pivot_col != k:
            for i in range(n):
                A[i][k], A[i][pivot_col] = A[i][pivot_col], A[i][k]
        for i in range(k + 1, n):
            c = A[i][k] / A[k][k]
            b[i] -= c * b[k]
            A[i][k] = 0
            for j in range(k + 1, n):
                A[i][j] -= c * A[k][j]

        print("\nMatrice après une étape d'élimination :")
        afficher_matrice(A)
        print("Vecteur b correspondant :")
        afficher_vecteur(b)

    return A, b
def Algorithmede_la_methodede_remontee(A, b):
    n = len(b)
    x = [0] * n
    x[-1] = b[-1] / A[-1][-1]

    for i in range(n - 2, -1, -1):
        somme = 0
        for k in range(i + 1, n):
            somme += A[i][k] * x[k]
        x[i] = (b[i] - somme) / A[i][i]
    print("\nVecteur solution x après substitution arrière :")
    afficher_vecteur(x)
    return x



def main():
    n = int(input("Entrez la taille de la matrice A (n x n): "))
    A = [[0] * n for _ in range(n)]
    print("Entrez les éléments de la matrice A :")
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input(f"A[{i}][{j}] = "))

    b = [0] * n
    print("Entrez les éléments du vecteur b :")
    for i in range(n):
        b[i] = float(input(f"b[{i}] = "))

    print("\nMatrice A initiale :")
    afficher_matrice(A)
    print("Vecteur b initial :")
    afficher_vecteur(b)

    A, b = gauss_pivot_total(A, b)

    print("\nMatrice triangulaire finale :")
    afficher_matrice(A)
    print("Vecteur b final :")
    afficher_vecteur(b)
    x=Algorithmede_la_methodede_remontee(A, b)
    print("Vecteur solution x :")
    afficher_vecteur(x)


if __name__ == "__main__":
    main()
