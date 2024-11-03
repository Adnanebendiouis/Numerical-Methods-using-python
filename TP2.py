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
def lireMatrice(T,l,c):
    for i in range(l):
        for j in range(c):
            T[i][j] = int(input(f"Entrer la case ({i},{j}): "))
    return T    
def lireVecteur(V,N):
    1
    for i in range(N):
        V[i] = int(input(f"Entrer l'élément {i}: "))    
def afficher_vecteur(V):
    N = len(V)
    for i in range(N):
        print(V[i], end=" ")
    print()        
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

def Algorithmede_la_methodede_remontee(A, b):
    n = len(b)
    x = [0] * n
    x[-1] = b[-1] / A[-1][-1]

    for i in range(n - 2, -1, -1):
        somme = 0
        for k in range(i + 1, n):
            somme += A[i][k] * x[k]
        x[i] = (b[i] - somme) / A[i][i]

    return x
def testmat(A,b):
    n = len(A)
    if isSuperieur(n,A):
        x=Algorithmede_la_methodede_remontee(A, b)
        afficher_vecteur(x)
        afficher_matrice(A)
    elif isInferieur(n,A):
        x=Algorithmede_la_methodede_descente(A, b)
        afficher_vecteur(x)
        afficher_matrice(A)
    else:
        print("la matrice n'est pas triangulaire")
        
def afficher_matrice(T):
    N = len(T)
    for i in range(N):
        for j in range(N):
            print(T[i][j], end=" ")
        print()
l = int(input("\nEntrez LE nombre des lignes  de matrice  :"))
c = int(input("\nEntrez LE nombre des colones  de matrice  :"))
print("\nEntrez la matrice triangulaire inférieure :")
A = [[0] * l for _ in range(c)]
A = lireMatrice(A, l,c)
t = int(input("\nEntrez la taille de vecteur :"))
print("\nentre le vecteur b :")
b = [0] * t
lireVecteur(b, t)
testmat(A,b)
# x = Algorithmede_la_methodede_descente(A, b)
#            afficher_vecteur(x)
# testmat([[1,0,0],[2,3,0],[4,5,6]],[1,2,3])

# def menu():
#     while True:
#         print("\n--- Solveur de Système Linéaire ---")
#         print("1. Résoudre avec Substitution Avant (Matrice Triangulaire Inférieure)")
#         print("2. Résoudre avec Substitution Arrière (Matrice Triangulaire Supérieure)")
#         print("3. Quitter")
#         choix = input("Entrez votre choix : ")

#         if choix == "1":
#            l = int(input("\nEntrez LE nombre des lignes  de matrice  :"))
#            c = int(input("\nEntrez LE nombre des colones  de matrice  :"))
#            print("\nEntrez la matrice triangulaire inférieure :")
#            A = [[0] * l for _ in range(c)]
#            A = lireMatrice(A, l,c)
#            t = int(input("\nEntrez la taille de vecteur :"))
#            print("\nentre le vecteur b :")
#            b = [0] * t
#            lireVecteur(b, t)
#            x = Algorithmede_la_methodede_descente(A, b)
#            afficher_vecteur(x)
           

#         elif choix == "2":
#            N = int(input("\nEntrez la taille de matrice  :"))
#            print("\nEntrez la matrice triangulaire inférieure :")
#            A = [[0] * N for _ in range(N)]
#            A = lireMatrice(A, N)
#            t = int(input("\nEntrez la taille de vecteur :"))
#            print("\nentre le vecteur b :")
#            b = [0] * t
#            lireVecteur(b, t)
#            x = Algorithmede_la_methodede_remontee(A, b)
#            afficher_vecteur(x)

#         elif choix == "3":
#             print("Sortie...")
#             break

#         else:
#             print("Choix invalide. Veuillez réessayer.")

# if __name__ == "__main__":
#     menu()
