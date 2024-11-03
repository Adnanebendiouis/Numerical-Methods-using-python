def gaussian_elimination(A, b):
    n = len(b)  
    m = len(A[0])  
    for k in range(n - 1):
        pivot = A[k][k]
        if pivot != 0:
            for i in range(k + 1, n):
                q = A[i][k]
                A[i][k] = 0 
                b[i] = b[i] - (q / pivot) * b[k]
                for j in range(k + 1, m):
                    A[i][j] = A[i][j] - (A[k][j] * q / pivot)
            print("iteratuion ",k)
            print("A: ")
            afficher_matrice(A)
            print("b: ")
            afficher_vecteur(b)
        else:
            print("Problem: pivot is zero")
            return None
    afficher_matrice(A)
    afficher_vecteur(b)    
    return A, b  

def lireMatrice(T,l,c):
    for i in range(l):
        for j in range(c):
            T[i][j] = int(input(f"Entrer la case ({i},{j}): "))
    return T    
def lireVecteur(V,N):
    
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

def afficher_matrice(T):
    N = len(T)
    for i in range(N):
        for j in range(N):
            print(T[i][j], end=" ")
        print()

def menu():
    l = int(input("\nEntrez LE nombre des lignes  de matrice  :"))
    c = int(input("\nEntrez LE nombre des colones  de matrice  :"))
    print("\nEntrez la matrice triangulaire inférieure :")
    A = [[0] * l for _ in range(c)]
    A = lireMatrice(A, l,c)
    t = int(input("\nEntrez la taille de vecteur :"))
    print("\nentre le vecteur b :")
    b = [0] * t
    lireVecteur(b, t)
    gaussian_elimination(A,b)
    X=Algorithmede_la_methodede_remontee(A,b)
    afficher_vecteur(X)
    
    
if __name__ == "__main__":
    menu()