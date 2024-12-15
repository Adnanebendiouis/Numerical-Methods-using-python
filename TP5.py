import math

def dichotomie(f, a, b, epsilon):
    if f(a) * f(b) > 0:
        print("On ne peut pas résoudre cette équation par la méthode de Dichotomie !")
        return None
    while (b - a) > epsilon:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return c

def dichotomie_recursive(f, a, b, epsilon):
    c = (a + b) / 2
    if abs(b - a) < epsilon:
        return c
    if f(a) * f(c) <= 0:
        return dichotomie_recursive(f, a, c, epsilon)
    else:
        return dichotomie_recursive(f, c, b, epsilon)

def point_fixe(g, x0, epsilon):
    while True:
        x1 = g(x0)
        if abs(x1 - x0) < epsilon:
            return x1
        x0 = x1

def point_fixe_recursive(g, x0, epsilon):
    x1 = g(x0)
    if abs(x1 - x0) < epsilon:
        return x1
    return point_fixe_recursive(g, x1, epsilon)

def newton(f, df, x0, epsilon):
    while True:
        if df(x0) == 0:
            print("Dérivée nulle ! Newton ne peut pas continuer.")
            return None
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < epsilon:
            return x1
        x0 = x1

def newton_recursive(f, df, x0, epsilon):
    if df(x0) == 0:
        print("Dérivée nulle ! Newton ne peut pas continuer.")
        return None
    x1 = x0 - f(x0) / df(x0)
    if abs(x1 - x0) < epsilon:
        return x1
    return newton_recursive(f, df, x1, epsilon)

def f1(x):
    return x**3 + 4*x - 2

def df1(x):
    return 3 * x**2 + 4

def f2(x):
    return math.exp(x) - 2*x - 1

def f3(x):
    return x - math.cos(x)

def df(x):
    return 3*x**2 + 4

def df2(x):
    return math.exp(x) - 2

def df3(x):
    return 1 + math.sin(x)

def g2(x):
    return 2 / (x**2 + 4)

if __name__ == "__main__":
    while True:
        print("\nChoisir une méthode pour résoudre l'équation :")
        print("1. Dichotomie")
        print("2. Dichotomie (récursive)")
        print("3. Point Fixe")
        print("4. Point Fixe (récursive)")
        print("5. Newton")
        print("6. Newton (récursive)")
        print("7. Quitter")
        
        choix = input("Votre choix : ")

        print("\n--- Choisissez une fonction ---")
        print("1. f(x) = x^3 + 4x - 2 sur [0, 1]")
        print("2. f(x) = exp(x) - 2x - 1 sur [1, 2]")
        print("3. f(x) = x - cos(x) sur [0, 1]")
        print("4. g(x) = 2 / (x^2 + 4)")
        sous_choix = input("Votre choix de fonction : ")

        if sous_choix == "1":
            f, a, b, epsilon, df = f1, 0, 1, 1e-8, df1
        elif sous_choix == "2":
            f, a, b, epsilon, df = f2, 1, 2, 1e-4, df2
        elif sous_choix == "3":
            f, a, b, epsilon, df = f3, 0, 1, 1e-5, df3
        elif sous_choix == "4":
            g, x0, epsilon = g2, 0.5, 1e-3
            f, df = None, None
        else:
            print("Choix de fonction invalide.")
            continue

        if choix == "1":
            if f:
                print("Résultat :", dichotomie(f, a, b, epsilon))
            else:
                print("Dichotomie non applicable pour cette fonction.")
        elif choix == "2":
            if f:
                print("Résultat :", dichotomie_recursive(f, a, b, epsilon))
            else:
                print("Dichotomie récursive non applicable pour cette fonction.")
        elif choix == "3":
            if sous_choix == "4":
                print("Résultat :", point_fixe(g, x0, epsilon))
            else:
                print("Point fixe non applicable.")
        elif choix == "4":
            if sous_choix == "4":
                print("Résultat :", point_fixe_recursive(g, x0, epsilon))
            else:
                print("Point fixe non applicable.")
        elif choix == "5":
            if f and df:
                print("Résultat :", newton(f, df, 0.5, epsilon))
            else:
                print("Newton non applicable pour cette fonction.")
        elif choix == "6":
            if f and df:
                print("Résultat :", newton_recursive(f, df, 0.5, epsilon))
            else:
                print("Newton non applicable pour cette fonction.")
        elif choix == "7":

            break
        else:
            print("Choix invalide, réessayez.")
