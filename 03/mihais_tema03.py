import random
"""
OBLIGATORII
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială
"""
print("Punctul 1")
lista_note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(f"Lista note muzicale: {lista_note_muzicale}")
for i in range(0, int(len(lista_note_muzicale)/2)):
    lista_note_muzicale[i], lista_note_muzicale[-i-1] = lista_note_muzicale[-i-1], lista_note_muzicale[i]
# lista_note_muzicale = lista_note_muzicale[::-1]
print(f"Lista inversata si suprascrisa: {lista_note_muzicale}")
lista_note_muzicale.reverse()
print(f"Lista note muzicale inversata a 2a oara cu metoda reverse: {lista_note_muzicale}")
print()


"""
2. De câte ori apare ‘do’?
"""
print("Punctul 2")
print(f"'do' apare de {lista_note_muzicale.count('do')} ori")
print()

"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă
"""
print("Punctul 3")
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4, 5]
print(f"Lista 1 = {list1}")
print(f"Lista 2 = {list2}")
print()
# Metoda 1
print("Metoda 1")
list3 = list1 + list2
print(f"Lista 3 = {list3}")
print()
# Metoda 2
print("Metoda 2")
list1.extend(list2)
print(f"Lista 1 = {list1}")
print()
# Metoda 3
print("Metoda 3")
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4, 5]
list4 = [*list1, *list2]
print(f"Lista 4 = {list4}")
print()

"""
4.Sortează și afișază lista generată la exercițiul anterior.
Sortează numărul 0 folosind o funcție.
Afișaza iar lista
"""
print("Punctul 4")
list4.sort()
print(f"Lista sortata in ordine crescatoare: {list4}")
list4.sort(reverse=True)
print(f"Lista sortata descrescator {list4}")
print(f"Afisarea listei ordonata crescator(fara suprascriere) {sorted(list4)} "
      f"versus lista in realitate {list4}")
list4.sort()
element_0 = list4.pop(list4.index(0))
print(f"Dupa \"sortarea\" lui '0' lista devine: {list4}")
print(f"Afisarea lui '0' din variabila in care l-am \"sortat\": {element_0}")
print()

"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
Lista este goală.
Lista nu este goală
"""
print("Punctul 5")
if list4:
    print("Lista nu este goala")
else:
    print("Lista este goala")
print()

"""
6. Folosește o funcție care să șteargă lista de la exercițiul 3
"""
print("Punctul 6")
print("Se sterg elementele listei")
list4.clear()
# del list4
# print("Am sters lista!")
print()

"""
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală
"""
print("Punctul 7")
if len(list4) != 0:
    print("Lista nu este goala")
else:
    print("Lista este goala")
print()

"""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""
print("Punctul 8")
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())
print()

"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""
print("Punctul 9")
for i in dict1:
    print(f"{i} a luat nota {dict1[i]}")
print()

"""
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
"""
print("Punctul 10")
dict1['Dorel'] = 6
print(f"Dorel a facut contestatie si a primit {dict1['Dorel']}")
print()

"""
11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi
"""
print("Punctul 11")
print("Gigel se transfera din clasa")
dict1.pop('Gigel')
print(dict1)
print("Vine un coleg nou")
dict1['Ionica'] = 9
print(dict1)
print()

"""
12.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișeaza zile_sapt
"""
print("Punctul 12")
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)
# 'luni' nu este adaugat pentru ca exista deja in set
print()

"""
13.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii
"""
print("Punctul 13")
if weekend.issubset(zile_sapt):
    print(f"Weekend = {weekend} este subset al zile_sapt = {zile_sapt}")
else:
    print(f"Weekend = {weekend} nu este subset al zile_sapt = {zile_sapt}")
print()

"""
14. Afișează diferențele dintre aceste 2 seturi
"""
print("Punctul 14")
print("Metoda 1")
print(f"Diferentele dintre cele 2 seturi: {zile_sapt-weekend}")
print("Metoda 2")
print(f"Diferentele dintre cele 2 seturi: {zile_sapt.difference(weekend)}")
print()

"""
15. Afișază intersecția elementelor din aceste 2 seturi
"""
print("Punctul 15")
print(zile_sapt.intersection(weekend))
print('*'*80)

"""
OPTIONALE
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
- Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori
"""
print("OPTIONAL - Punctul 1 - ECHIPA DE FOTBAL")

echipa = ['j01', 'j02', 'j03', 'j04', 'j05', 'j06', 'j07', 'j08', 'j09', 'j10']
titulari = []
jucatori_out = []
SCHIMBARI_MAX = 3
schimbari_efectuate = 0

mesaj_start = "Ai o echipa de fotbal cu 10 jucatori, titulari si rezerve\n" \
              "Introdu numarul de titulari pe care ii vrei in teren la un moment dat\n" \
              "(sugestie intervalul 3-7)\n"
nr_titulari = int(input(mesaj_start))

for i in range(0, nr_titulari, 1):
    jucator = random.choice(echipa)
    titulari.append(jucator)
    echipa.remove(jucator)
rezerve = echipa[:]
echipa.extend(titulari)

titulari.sort()
rezerve.sort()
echipa.sort()
print(f"\nEchipa este compusa din {echipa}\n")
print(f"Titularii sunt: {titulari}\nRezervele sunt: {rezerve}\n")

while schimbari_efectuate < SCHIMBARI_MAX:
    titular_out = random.choice(titulari)
    rezerva_in = random.choice(rezerve)
    titulari.remove(titular_out)
    jucatori_out.append(titular_out)
    titulari.append(rezerva_in)
    rezerve.remove(rezerva_in)
    schimbari_efectuate += 1
    mesaj_schimbare_1 = f"Se va efectua schimbarea cu numarul {schimbari_efectuate}!!!\n" \
                        f"Iese din teren jucatorul {titular_out}\n" \
                        f"Intra in teren jucatorul {rezerva_in}"
    if schimbari_efectuate == 1:
        mesaj_schimbare_2 = f"Mai sunt disponibile {SCHIMBARI_MAX - schimbari_efectuate} schimbari!\n"
    elif schimbari_efectuate == 2:
        mesaj_schimbare_2 = "Mai este disponibila o singura schimbare!!\n"
    else:
        mesaj_schimbare_2 = "Nu mai sunt schimbari disponibile!!!\n"
    print(mesaj_schimbare_1), print(mesaj_schimbare_2)

rezerve.extend(jucatori_out)
titulari.sort()
rezerve.sort()
jucatori_out.sort()

mesaj_final_meci = f"Echipa la sfarsitul meciului:\n" \
                   f"Jucatorii din teren la sfarsitul meciului: {titulari}\n" \
                   f"Rezervele de pe banca la sfarsitul meciului {rezerve}\n" \
                   f"Jucatorii care au fost scosi de pe teren in timpul meciului: {jucatori_out}"
print(mesaj_final_meci)
