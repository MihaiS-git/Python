"""
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă

variabila = o casuta din memorie, cu eticheta, unde punem date; se aloca memorie
o data cu initializarea isi pierde valoarea dupa rularea programului
"""

"""
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :

- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
"""

nume = "Tom"
varsta = 20
venit = 1000.55
casatorit = False

"""
3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat
"""
print("Pct.3")
print("Afisarea si verificarea tipurilor de date declarate si initializate la exercitiul anterior:\n")
print(f"Variabila: {nume}\nTipul variabilei: {type(nume)}")
print(f"Variabila: {varsta}\nTipul variabilei: {type(varsta)}")
print(f"Variabila: {venit}\nTipul variabilei: {type(venit)}")
print(f"Variabila: {casatorit}\nTipul variabilei: {type(casatorit)}")
print()

"""
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere): - Verifică tipul acesteia
"""
print("Pct.4")
print("Rotunjire variabila tip float si afisarea tipului:")
venit = round(venit)
print(f"Variabila: {venit} Tipul variabilei: {type(venit)}")
print()

"""
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești
"""
print("Pct.5")
print(f"Numele lui este {nume}")
varsta = str(varsta)
print(f"Varsta lui {nume} este {varsta}")
print(type(varsta))
venit = float(venit)
print(f"Venitul anual al lui {nume} este {12*venit}")
print(type(venit))
print(f"{nume} este casatorit? {casatorit}")
print()

"""
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'
"""
print("Pct.6")
nume = str(input("Introdu numele:\n"))
prenume = str(input("Introdu prenumele:\n"))
print(f"Lungimea numelui complet este de {len(nume)+len(prenume)} caractere")
print()

"""
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'
"""
print("Pct.7")
a = float(input("Introduceti latimea dreptunghiului:\n"))
b = float(input("Introduceti lungimea dreptunghiului:\n"))
print(f"Aria dreptunghiului este: {a*b}")
print()

"""
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
"""
print("Pct.8")
str1 = "Coral is either the stupidest animal or the smartest rock"
print(str1)
print(f"Grupul 'the' apare de {str1.count('the')} ori in stringul dat")
print()

"""
9. Același string.
Afișează de câte ori apare cuvântul 'the';
Printează rezultatul
"""
print("Pct.9")
print(f"Cuvantul 'the' apare de {str1.count(' the ')} ori in stringul dat")
print()

"""
10. Același string.
Folosiți un assert ca să verificați dacă acest string conține doar numere
"""
# print("Pct.10")
# assert str1.isnumeric(),"Stringul nu contine doar numere"

"""
O1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc
"""
print("Pct.O1")
str2 = input("Introduceti un string de dimensiune impara:\n")
print(f"Caracterul din mijloc este: {str2[int(len(str2)/2)]}")
print()

"""
O2. Folosind assert, verifică dacă un string este palindrom.
"""
# print("Pct.O2")
# str3 = input("Introduceti un string pentru a verifica daca este palindrom\n")
# assert str3 == str3[::-1], "Stringul introdus nu este un palindrom"
# print()

"""
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare
"""
print("Pct.O3")
a, b = input("Introdu un string din 2 cuvinte pentru a-l imparti in 2 variabile:\n").split(' ')
print(b, a)
print()

"""
O4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla
"""
print("Pct.O4")
str4 = input("Introdu un string pentru a capitaliza primul caracter peste tot, exceptand prima si ultima pozitie\n")
letter0 = str4[0]
lettern = str4[len(str4)-1]
str4b = str4[1:-1]
Letter0 = letter0.upper()
str4int = str4b.replace(letter0.lower(), Letter0)
str4fin = letter0 + str4int + lettern
print(str4fin)
print()

"""
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.

eg: parola abc => ***
parola abcd => ****
"""
print("Pct.O5")
print("Login - introduceti datele")
user = input("User: ")
password = input("Pass: ")
hidden_password = "*" * len(password)
print(f"Parola pentru user-ul '{user}' este: {hidden_password} si are {len(password)} caractere")
print()
