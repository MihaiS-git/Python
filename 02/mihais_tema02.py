import random

"""
OBLIGATORII
Punctul 1
if-else = daca (conditie) -> faci (asta), altfel -> faci (cealalta); conditionare in rularea programului, daca
conditia e indeplinita, programul va rula pe o ramura de cod, daca conditia este False, programul va rula pe cealalta
ramura de cod elif - ramuri suplimentare in cadrul if-ului cu conditionare in plus pentru cazul in care conditia
principala este False
"""

"""
2. Verifică și afișează dacă x este număr natural sau nu
"""
print("# Punctul 2")
x = input("Introdu un numar de la tastatura:\t")
if x.isdigit():
    print("Numarul introdus este un numar natural")
else:
    print("Numarul introdus nu este numar natural")
print()

"""
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru
"""
print("# Punctul 3")
x = int(x)
if x < 0:
    print("Numarul este negativ")
elif x > 0:
    print("Numarul este pozitiv")
else:
    print("Numarul este neutru")
print()

"""
4. Verifică și afișează dacă x este între -2 și 13
"""
print("# Punctul 4")
if (x > -2) and (x < 13):
    print("Numarul este intre -2 si 13")
else:
    print("Numarul nu este intre -2 si 13")
print()

"""
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5
"""
print("# Punctul 5")
x = int(input("Introdu un numar x: \t"))
y = int(input("Introdu un numar y: \t"))
if abs(x - y) < 5:
    print("Diferenta este mai mica decat 5")
elif abs(x - y) == 5:
    print("Diferenta este 5")
else:
    print("Diferenta este mai mare decat 5")
print()

"""
6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
"""
print("# Punctul 6")
x = int(input("Introduceti un numar x: \t"))
if x >= 0:
    if not (x < 5) and not (x > 27):
        print("Numarul introdus este intre 5 si 27")
    else:
        print("Numarul introdus nu este intre 5 si 27")
else:
    print("Numarul introdus este negativ, va rugam reluati")
print()

"""
7. x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
"""
print("# Punctul 7")
x = int(input("Introdu un numar x: \t"))
y = int(input("Introdu un numar y: \t"))
if x == y:
    print("Numerele introduse sunt egale")
else:
    if x > y:
        print(f"{x} este mai mare, diferenta este de {x-y}")
    else:
        print(f"{y} este mai mare, diferenta este de {y-x}")
print()

"""
8. X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare
"""
print("# Punctul 8")
print("x, y, z sunt laturile unui triunghi")
x = int(input("Introdu x: \t"))
y = int(input("Introdu y: \t"))
z = int(input("Introdu z: \t"))
if ((x + y) > z) and ((x + z) > y) and ((y + z) > x):
    if x == y and x == z and y == z:
        print("Triunhiul este echilateral")
    elif x == y or x == z or y == z:
        print("Triunghiul este isoscel")
    else:
        print("Triunghiul este oarecare")
else:
    print("Laturile introduse nu formeaza un triunghi!!!")
print()

"""
9. Citește o literă de la tastatură.
Verifică și afișează dacă este vocală sau nu
"""
print("# Punctul 9")
litera = input("Introdu o litera:\t")
if litera in {"a", "e", "i", "o", "u"}:
    print("Litera este vocala")
else:
    print(f"Litera {litera} este consoana")
print()

"""
10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""
print("# Punctul 10")
nota = float(input("Introdu nota:\t"))
if 1 < nota <= 10:
    if nota >= 9:
        print(f"In noul sistem, nota {nota} este echivalata cu 'A'")
    elif nota >= 8:
        print(f"In noul sistem, nota {nota} este echivalata cu 'B'")
    elif nota >= 7:
        print(f"In noul sistem, nota {nota} este echivalata cu 'C'")
    elif nota >= 6:
        print(f"In noul sistem, nota {nota} este echivalata cu 'D'")
    elif nota > 4:
        print(f"In noul sistem, nota {nota} este echivalata cu 'E'")
    else:
        print(f"In noul sistem, nota {nota} este echivalata cu 'F'")
else:
    print("Nota introdusa este invalida")
print()

"""
OPTIONALE
O1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""
print("# Punctul O1")
x = int(input("Introdu un numar:\n"))
if x/1000 >= 1:
    print("Numarul introdus are minim 4 cifre")
else:
    print("Numarul introdus nu are minim 4 cifre")
print()

"""
O2.Verifică dacă x are exact 6 cifre
"""
print("# Punctul O2")
x = int(input("Introdu un numar:\n"))
if (x/100000 >= 1) and (x/100000 < 10):
    print("Numarul introdus are exact 6 cifre")
else:
    print("Numarul introdus nu are exact 6 cifre")
print()

"""
O3.Verifică dacă x este număr par sau impar (x e int)
"""
print("# Punctul O3")
x = int(input("Introdu un numar:\n"))
if x % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")
print()

"""
O4. x, y, z (int)
Afișează care este cel mai mare dintre ele?
"""
print("# Punctul O4")
x = int(input("Introdu un numar:\t"))
y = int(input("Introdu un numar:\t"))
z = int(input("Introdu un numar:\t"))
if (x > y) and (x > z):
    print(f"{x} este cel mai mare")
elif (y > x) and (y > z):
    print(f"{y} este cel mai mare")
else:
    print(f"{z} este cel mai mare")
print()

"""
O5. X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu
"""
print("# Punctul O5")
print("Introdu unghiurile triunghiului pentru a verifica daca este valid:")
x = int(input("Introdu primul unghi:\t"))
y = int(input("Introdu al doilea unghi:\t"))
z = int(input("Introdu al treilea unghi:\t"))
if x > 0 and y > 0 and z > 0:
    if x+y+z == 180:
        print("Triunghiul este valid")
    else:
        print("Triunghiul nu este valid")
print()

"""
O6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citiți de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
"""
print("# Punctul O6")
str1 = "Coral is either the stupidest animal or the smartest rock"
print(str1)
print()
x = int(input("Introdu numarul de caractere pe care vrei sa il tai de la sfarsitul stringului de mai sus:\n"))
if (x > 0) and (x <= len(str1)):
    print(str1[0:(len(str1)-x)])
elif x == len(str1):
    print("Numarul de caractere cerut este egal cu lungimea stringului, nu se mai afiseaza nimic")
else:
    print("Numarul de caractere cerut este mai mare decat lungimea stringului")
print()

"""
O7.Același string. Declară un string nou care să fie format din primele 5 caractere
+ ultimele 5
"""
print("# Punctul O7")
str2 = str1[0:5] + str1[(len(str1)-5):len(str1)]
print(str2)
print()

"""
O8. Același string.
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
output: 'Coral is either the stupidest animal or the smartest '
"""
print("# Punctul O8")
index_rock = str1.find("rock")
print(f"Indexul cuvantului 'rock' este {index_rock}")
str3 = str1[0:index_rock]
print(str3)
print()

# """
# O9. Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
# """
# print("# Punctul O9")
# str4 = input("Introdu un string pentru a verifica daca primul si ultimul caracter sunt acelasi:\n")
# assert str4[0] == str4[len(str4)-1] or str4[0] == str4.upper()[len(str4)-1] or str4[0] == str4.lower()[len(str4)-1]; "Eroare!!!"

"""
O10. Avand stringul '0123456789'
Afișați doar numerele pare
Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)
"""
print("# Punctul O10")
str5 = "0123456789"
print(f"Avem stringul: {str5}")
par = str5[0:-1:2]
impar = str5[1:len(str5)+1:2]
print(f"Numerele pare: {par}")
print(f"Numerele impare: {impar}")
print()

"""
O11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
Ai ghicit. Felicitari! Ai ales x si zarul a fost y
"""
print("# Punctul O11")
dice_roll = random.randint(0, 6)
guess_dice = int(input(f"Ghiceste numarul de pe zar(1-6):\t"))
if (guess_dice > 0) and (guess_dice <= 6):
    if guess_dice == dice_roll:
        print(f"Ai ghicit. Felicitari! Ai ales {guess_dice} si zarul a fost {dice_roll}")
    elif guess_dice < dice_roll:
        print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {guess_dice}, dar zarul a fost {dice_roll}")
    else:
        print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {guess_dice}, dar zarul a fost {dice_roll}")
else:
    print("Numarul introdus de tine este invalid!")
