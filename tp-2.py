def triangularisation(A, b):
    n = len(b)  # taille de la matrice carrée A (nombre de lignes/colonnes)

    for k in range(n - 1):
        pivot = A[k][k]
        
        # Vérifier que le pivot n'est pas nul
        if pivot != 0:
            for i in range(k + 1, n):
                q = A[i][k]
                A[i][k] = 0  # Mettre la valeur sous le pivot à 0
                
                # Mettre à jour le vecteur b
                b[i] = b[i] - (q / pivot) * b[k]
                
                # Mettre à jour les éléments de la matrice A pour les colonnes restantes
                for j in range(k + 1, n):
                    A[i][j] = A[i][j] - (A[k][j] * q / pivot)
        else:
            print("Problème : pivot nul détecté.")
            return None, None  # Retourner None pour indiquer un problème dans le calcul

    return A, b  # Retourner la matrice triangulaire et le vecteur b modifié


def back_substitution(A, b):
    n = len(b)
    x = np.zeros(n)
    
    # Set the last element of x
    x[n - 1] = b[n - 1] / A[n - 1, n - 1]
    
    # Back-substitution loop
    for i in range(n - 2, -1, -1):
        sum_ = 0
        for k in range(i + 1, n):
            sum_ += A[i, k] * x[k]
        x[i] = (b[i] - sum_) / A[i, i]
    
    return x
