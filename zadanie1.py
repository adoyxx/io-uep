def oblicz(J, p1, p2, x1, x2):

    U = min(x1,15*x2)

    czy_wystarczylo = p1*x1+p2*x2 < J
   
    print(f"Użyteczność koszyka: {U}. Czy wystarczyło budżetu: {czy_wystarczylo}.")

    

def main():
    J = int(input("Podaj budżet: "))
    p1 = float(input("Podaj cenę roweru: "))
    p2 = float(input("Podaj cenę butelki koniaku: "))
    x1 = float(input("Podaj liczbę rowerów, które chcesz kupić: "))
    x2 = float(input("Podaj liczbę butelek koniaku, które chcesz kupić: "))
    oblicz(J, p1, p2, x1, x2)
    
main()