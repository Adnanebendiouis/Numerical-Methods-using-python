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
def lu_decomposition(A):
    n = len(A)
    L = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  
    U = [[A[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = U[k][k]
        for i in range(k + 1, n):
            factor = U[i][k] / pivot  
            L[i][k] = factor  
            U[i][k] = 0  
            for j in range(k + 1, n):
                U[i][j] = U[i][j] - factor * U[k][j]  

    return L, U
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
def Algorithmede_la_methodede_descente(A, b):
    n = len(b)
    x = [0] * n
    x[0] = b[0] / A[0][0]

    for i in range(1, n):
        somme = 0
        for j in range(i):
            somme += A[i][j] * x[j]
        x[i] = (b[i] - somme) / A[i][i]

    return x
def main():
    N=3
    A = [[0 for _ in range(N)] for _ in range(N)]
    # lireMatrice(A,N,N)
    b = [0 for _ in range(N)]
    # lireVecteur(b,N)
    # print("\nMatrice A:")
    # afficher_matrice(A)
    # print("\nVecteur b:")
    # afficher_vecteur(b)
    # L, U = lu_decomposition(A)
    # print("\nMatrice L:")
    # afficher_matrice(L)
    # print("\nMatrice U:")
    # afficher_matrice(U)
    # y = Algorithmede_la_methodede_descente(L, b)
    # x = Algorithmede_la_methodede_remontee(U, y)
    #     print("\nVecteur solution x:")
    #     afficher_vecteur(x)
    while True:
     print("\n--- Solveur de Système Linéaire ---")
     print("1. Lire la matrice A et le vecteur b.")
     print("2. Afficher la matrice A initiale et le vecteur b initial.")
     print("3. Afficher les matrices L et U après decomosition")
     print("4. Afficher le systeme Ly=b et le resoudre par descente")
     print("5. Afficher le systeme Ux=y et le resoudre par remontee.")
     print("6. Quitter.")
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
         L,U=lu_decomposition(A)
         print("\nAfficher les matrices L et U apres decomosition")
         print("\nMatrice L:")
         afficher_matrice(L)
         print("\nMatrice U:")
         afficher_matrice(U)
     elif choix == "4":
         print("Afficher le systeme Ly=b et le resoudre par descente")
         y = Algorithmede_la_methodede_descente(L, b)
         afficher_vecteur(y)
     elif choix == "5":
         print("\nAfficher le systeme Ux=y et le resoudre par remontee.")  
         x = Algorithmede_la_methodede_remontee(U, y) 
         afficher_vecteur(x) 
     elif choix == "6":
         break      
main()
    