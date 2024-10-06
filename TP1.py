def lireMatrice(N, T):
    for i in range(N):
        for j in range(N):
            T[i][j] = int(input(f"Entrer la case ({i},{j}): "))

def affichierMatrice(N, T):
    for i in range(N):
        for j in range(N):
            print(T[i][j], end=" ")
        print()

def matriceIdentite(N, T):
    for i in range(N):
        for j in range(N):
            if i == j:
                T[i][j] = 1
            else:
                T[i][j] = 0

def laSomme(N, A, B, C):
    for i in range(N):
        for j in range(N):
            C[i][j] = A[i][j] + B[i][j]

def leProduit(N, A, B, C):
    for i in range(N):
        for j in range(N):
            C[i][j] = 0
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]

def laTransposee(N, A, C):
    for i in range(N):
        for j in range(N):
            C[j][i] = A[i][j]

def isSuperieur(N, A):
    for i in range(N):
        for j in range(i):
            if A[i][j] != 0:
                return False
    return True

def isInferieur(N, A):
    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] != 0:
                return False
    return True

def estDiagonal(N, A):
    for i in range(N):
        for j in range(N):
            if i != j and A[i][j] != 0:
                return False
    return True

def estSymetrique(N, T):
    for i in range(N):
        for j in range(i, N):
            if T[i][j] != T[j][i]:
                return False
    return True
def menu():
    print("menu")
    print("1_ Lire une matrice")
    print("2_ Afficher une matrice carrée")
    print("3_ Afficher l'identité d'ordre N")
    print("4_ La somme de deux matrices")
    print("5_ Le produit de deux matrices")
    print("6_ La transposée d'une matrice")
    print("7_ Tester triangulaire supérieur")
    print("8_ Tester triangulaire inférieur")
    print("9_ Tester matrice carrée diagonale")
    print("10_ Tester une matrice carrée symétrique")
    print("0_ Quitter")
    choice = int(input("Entrer votre choix: "))
    while choice:
        if choice == 1:
            N = int(input("Entrer la taille d'une matrice carrée N: "))
            T = [[0 for _ in range(N)] for _ in range(N)]
            lireMatrice(N, T)
        elif choice == 2:
            affichierMatrice(N, T)
        elif choice == 3:
            N = int(input("Entrer la taille d'une matrice carrée N: "))
            T = [[0 for _ in range(N)] for _ in range(N)]
            matriceIdentite(N, T)
            affichierMatrice(N, T)
        elif choice == 4:
            N = int(input("Entrer la taille d'une matrice carrée N: "))
            A = [[0 for _ in range(N)] for _ in range(N)]
            B = [[0 for _ in range(N)] for _ in range(N)]
            C = [[0 for _ in range(N)] for _ in range(N)]
            print("Lire Matrice A:")
            lireMatrice(N, A)
            print("Lire Matrice B:")
            lireMatrice(N, B)
            laSomme(N, A, B, C)
            affichierMatrice(N, C)
        elif choice == 5:
            N = int(input("Entrer la taille d'une matrice carrée N: "))
            A = [[0 for _ in range(N)] for _ in range(N)]
            B = [[0 for _ in range(N)] for _ in range(N)]
            C = [[0 for _ in range(N)] for _ in range(N)]
            print("Lire Matrice A:")
            lireMatrice(N, A)
            print("Lire Matrice B:")
            lireMatrice(N, B)
            leProduit(N, A, B, C)
            affichierMatrice(N, C)
        elif choice == 6:
            N = int(input("Entrer la taille d'une matrice carrée N: "))
            A = [[0 for _ in range(N)] for _ in range(N)]
            C = [[0 for _ in range(N)] for _ in range(N)]
            print("Lire Matrice A:")
            lireMatrice(N, A)
            laTransposee(N, A, C)
            affichierMatrice(N, C)
        elif choice == 7:
            N = int(input("Entrer la taille d'une matrice carrée N: "))
            A = [[0 for _ in range(N)] for _ in range(N)]
            print("Lire Matrice A:")
            lireMatrice(N, A)
            if isSuperieur(N, A):
                print("La matrice est triangulaire supérieure.")
            else:
                print("La matrice n'est pas triangulaire supérieure.")
        elif choice == 8:
            N = int(input("Entrer la taille d'une matrice carrée N: "))
            A = [[0 for _ in range(N)] for _ in range(N)]
            print("Lire Matrice A:")
            lireMatrice(N, A)
            if isInferieur(N, A):
                print("La matrice est triangulaire inférieure.")
            else:
                print("La matrice n'est pas triangulaire inférieure.")
        elif choice == 9:
            N = int(input("Entrer la taille d'une matrice carrée N: "))
            A = [[0 for _ in range(N)] for _ in range(N)]
            print("Lire Matrice A:")
            lireMatrice(N, A)
            if estDiagonal(N, A):
                print("La matrice est diagonale.")
            else:
                print("La matrice n'est pas diagonale.")
        elif choice == 10:
            N = int(input("Entrer la taille d'une matrice carrée N: "))
            A = [[0 for _ in range(N)] for _ in range(N)]
            print("Lire Matrice A:")
            lireMatrice(N, A)
            if estSymetrique(N, A):
                print("La matrice est symétrique.")
            else:
                print("La matrice n'est pas symétrique.")
        elif choice == 0:
            break
        choice = int(input("Entrer votre choix: "))
menu()


