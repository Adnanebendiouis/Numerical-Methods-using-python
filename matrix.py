def menu():
    print("1_ lire une matrice")
    print("2_ affichier une matrice carre")
    print("3_ affichier l'identite d'ordre N ")
    print("4_ la somme de deux matrices ")
    print("5_ le produit de deux matrices")
    print("6_ la transpose d'une matrice")
    print("7_tester triongulair superieur ")
    print("8_ tester triongulair inferieur")
    print("9_tester matrice carrre diagonal ")
    print("10_tester une matrice carre symetrique ")
    x = int(input("enter votre choix"))
N = int(input("entrer la taille d'une matrice carre N "))
T = [[0 for _ in range(N)] for _ in range(N)]
def lireMatrice(N,T):
    for i in range (0,N):
     for j in range(0,N):
        T[i][j] = int(input(f"entrer la case ({i},{j})"))

def affichierMatrice(N,T):
    for i in range (0,N):
     for j in range(0,N):
        print(T[i][j],end=" ")
     print()   
lireMatrice(N,T)  
affichierMatrice(N,T)  
N = int(input("entrer la taille d'une matrice carre N "))
T = [[0 for _ in range(N)] for _ in range(N)]
def matriceIdentite(N,T):
    for i in range (0,N):
     for j in range(0,N):
        if i == j:
            T[i][j] = 1
        else:
            T[i][j] = 0
def affichierMatrice(N,T):
    for i in range (0,N):
     for j in range(0,N):
        print(T[i][j],end=" ")
     print()  
matriceIdentite(N,T)
affichierMatrice(N,T)
N = int(input("entrer la taille d'une matrice  A "))
M = int(input("entrer la taille d'une matrice  B "))
while N!=M:
    print("les matrices ne sont pas de meme taille")
    N = int(input("entrer la taille d'une matrice  A "))
    M = int(input("entrer la taille d'une matrice  B "))
    
   

def lireMatrice(N,T):
    for i in range (0,N):
     for j in range(0,N):
        T[i][j] = int(input(f"entrer la case ({i},{j})"))
def laSomme(N,A,B,C):
    for i in range (0,N):
     for j in range(0,N):
        C[i][j] = A[i][j] + B[i][j]
def affichierMatrice(N,T):
    for i in range (0,N):
     for j in range(0,N):
        print(T[i][j],end=" ")
     print()  


A = [[0 for _ in range(N)] for _ in range(N)]
B = [[0 for _ in range(N)] for _ in range(M)]
C = [[0 for _ in range(N)] for _ in range(N)]

def leProduit(N,A,B,C):
    for i in range(N):
        for j in range(N):
            C[i][j] = 0
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
def laTransposee(N,A,C):
    for i in range(N):
        for j in range(N):
            C[j][i] = A[i][j]        
def isSuperieur(N,A):
    for i in range(N):
        for j in range(i):
            if A[i][j] != 0:
                return False          
    return True       
def isInferieur(N,A):
    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] != 0:
                return False
    return True  
def estDiagonal(N,A):
    for i in range(N):
        for j in range(N):
            if i != j and A[i][j] != 0:
                return False   
    return True                 
def estSymetrique(N,T):
    for i in range(N):
        for j in range(i, N):
            if T[i][j] != T[j][i]:
                return False
    return True         
     
               
                
                
                
                
lireMatrice(N,A)
lireMatrice(N,B)
laSomme(N,A,B,C)
leProduit(N,A,B,C)
laTransposee(N,A,C)
affichierMatrice(N,A)
s = isSuperieur(N,A)
s = isInferieur(N,A)
s = estDiagonal(N,A)
s = estSymetrique(N,A)
print(s)

    