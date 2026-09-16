from fractran import Fraction, Fractran, Facteur
print("Somme :") 
somme = [Fraction(3, 2)] 
facteurs = Facteur([2, 3, 5]) 

for i in range(10): 
    for j in range(10): 
        retour = Fractran(somme).run(facteurs.nombre([i, j]))
        décomposition = facteurs.décomposition(retour)
        print(i, "+", j, "=", décomposition[1], "(retour =", retour, "; décomposition =", décomposition, ")")


print("Produit :")
produit = [Fraction(455, 33), Fraction(11, 13), Fraction(1, 11), Fraction(3, 7), Fraction(11, 2), Fraction(1, 3)]
for i in range(10):
    for j in range(10):
        retour = Fractran(produit).run(facteurs.nombre([i, j]))
        décomposition = facteurs.décomposition(retour)
        print(i, "*", j, "=", décomposition[2], "(retour =", retour, "décomposition =", décomposition, ")")


print("Fibonacci rend les couples (F(n), F(n+1)) :")
fibonacci = [Fraction(23, 95), Fraction(57, 23), Fraction(17, 39), Fraction(130, 17), Fraction(11, 14), 
          Fraction(35, 11), Fraction(19, 13), Fraction(1, 19), Fraction(35, 2), Fraction(13, 7), 
          Fraction(7, 1)]

sortie_brute = Fractran(fibonacci).suite(3, 1000) 
sortie = []
for n in sortie_brute:
    if n == Facteur([2, 3]).nombre(Facteur([2, 3]).décomposition(n)):
        sortie.append(Facteur([2, 3]).décomposition(n))

print(sortie)
#Le programme utilise un programme FRACTRAN pour générer les nombres de la suite de Fibonacci. La méthode suite(3, 1000) commence avec le nombre 3 et applique successivement les fractions du programme FRACTRAN. 
#À chaque étape, elle cherche la première fraction dont le dénominateur divise le nombre courant, puis calcule le nombre suivant. La suite obtenue est ensuite parcourue pour sélectionner les nombres qui peuvent être décomposés uniquement avec les facteurs 2 et 3. 
#Pour ces nombres, Facteur([2, 3]).décomposition(n) donne leurs exposants pour 2 et 3. Ces exposants représentent les couples (F(n), F(n+1)) de la suite de Fibonacci, qui sont finalement ajoutés à la liste sortie et affichés.

print("Nombres premiers :")
crible = [Fraction(17, 91), Fraction(78, 85), Fraction(19, 51), Fraction(23, 38), Fraction(29, 33), 
          Fraction(77, 29), Fraction(95, 23), Fraction(77, 19), Fraction(1, 17), Fraction(11, 13), 
          Fraction(13, 11), Fraction(15, 14), Fraction(15, 2), Fraction(55, 1)]

sortie = [Facteur([2]).décomposition(n)[0] for n in Fractran(crible).suite(2, 500000) 
          if n == Facteur([2]).nombre(Facteur([2]).décomposition(n))]

print(sortie)