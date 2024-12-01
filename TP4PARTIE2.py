def methode_jacobi(A, b, x0, n):
    x = x0[:]
    for k in range(n):
        x_new = x[:]
        for i in range(len(A)):
            sum1 = 0
            for j in range(len(A)):
                if j != i:
                    sum1 += A[i][j] * x[j]
            x_new[i] = (1 / A[i][i]) * (b[i] - sum1)
        x = x_new[:]
    return x



def gauss_seidel_method(A, b, x0, n):
    x = x0

    for k in range(n):
        for i in range(len(A)):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, len(A)))
            x[i] = (1 / A[i][i]) * (b[i] - sum1 - sum2)
    return x
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


def menu():
    while True:
     print("\n--- Solveur de Système Linéaire ---")
     print("1. Lire la matrice A et le vecteur b.")
     print("2. Afficher la matrice A initiale et le vecteur b initial.")
     print("3. Algorithme de Jacobi")
     print("4. Algorithme de Gauss‐Seidel")
     print("5. Quitter.")
     choix = input("Entrez votre choix : ")
     if choix == "1":
            N=3
            A = [[0 for _ in range(N)] for _ in range(N)]
            lireMatrice(A,N,N)
            b = [0 for _ in range(N)]
            lireVecteur(b,N)
     elif choix == "2":
            print("\nMatrice A:")
            afficher_matrice(A)
            print("\nVecteur b:")
            afficher_vecteur(b)
     elif choix == "3":
            x0 = [0, 0, 0]
            n = 1
            solution = methode_jacobi(A, b, x0, n)    
            print("Solution:", solution)
     elif choix == "4":
            x0 = [0, 0, 0]
            n = 25
            solution = gauss_seidel_method(A, b, x0, n)
            print("Solution:", solution)
     elif choix == "5":
            break
if __name__ == "__main__":
    menu()