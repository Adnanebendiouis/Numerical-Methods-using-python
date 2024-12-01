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


def matrix_to_triangular(A, b):
    n = len(A)
    m = len(A[0])  
    for k in range(n):
        p = A[k][k]
        l = k
        for i in range(k, n):
            if abs(A[i][k]) > abs(p):
                p = A[i][k]
                l = i
        if l != k:
            for j in range(k, m):
                temp = A[k][j]
                A[k][j] = A[l][j]
                A[l][j] = temp
            b[k], b[l] = b[l], b[k]  # Swap the corresponding elements in b
        for i in range(k + 1, n):
            q = A[i][k]
            A[i][k] = 0
            for j in range(k + 1, m):
                A[i][j] = A[i][j] - A[k][j] * q / p
            b[i] = b[i] - b[k] * q / p  # Adjust b accordingly
        print("\nMatrice après élimination (étape de Gauss):")
        afficher_matrice(A)
        print("Vecteur b après modification :")
        afficher_vecteur(b)
    return A


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


def menu():
    while True:
        print("\n--- Solveur de Système Linéaire ---")
        print("1. Lire la matrice A et le vecteur b.")
        print("2. Afficher la matrice A initiale et le vecteur b initial.")
        print("3. Algorithme d'élimination de Gauss avec pivot partiel.")
        print("4. Quitter.")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            l = int(input("\nEntrez le nombre des lignes de la matrice : "))
            c = int(input("\nEntrez le nombre des colonnes de la matrice : "))
            A = [[0] * c for _ in range(l)]
            A = lireMatrice(A, l, c)
            t = int(input("\nEntrez la taille du vecteur : "))
            print("\nEntrez les éléments du vecteur b :")
            b = [0] * t
            lireVecteur(b, t)
            print("\nVecteur b initial :")
            afficher_vecteur(b)

        elif choix == "2":
            print("\nMatrice A initiale :")
            afficher_matrice(A)
            print("\nVecteur b initial :")
            afficher_vecteur(b)

        elif choix == "3":
            print("\nÉlimination de Gauss avec pivot partiel...")
            A = matrix_to_triangular(A, b)
            print("\nMatrice triangulaire finale :")
            afficher_matrice(A)
            print("\nVecteur b final :")
            afficher_vecteur(b)
            x = Algorithmede_la_methodede_remontee(A, b)
            afficher_vecteur(x)

        elif choix == "4":
            print("Programme terminé.")
            break


if __name__ == "__main__":
    menu()

