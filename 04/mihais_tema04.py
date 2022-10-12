import random

"""
OBLIGATORII
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while
"""
print("Pct.1")
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for i in range(len(cars)):
    if cars[i] == 'Opel':
        print(f"My favourite car is {cars[i]}")
print()

for item in cars:
    if item == 'Opel':
        print(f"My favourite car is {item}")
print()

i = 0
while i <= len(cars)-1:
    if cars[i] == 'Opel':
        print(f"My favourite car is {cars[i]}")
    i += 1
print()

"""
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează list
"""
print("Pct.2")
for i in range(0, len(cars)):
    if i == 0 or i == len(cars)-1:
        continue
    else:
        cars[i] = cars[i].upper()
else:
    print(cars)
print()

"""
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
"""
print("Pct.3")
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
wanted = 'BMW'
for item in cars:
    if item == wanted:
        print(f"I found the car {item} that you wanted")
        break
    else:
        print(f"I found the car {item}. Keep searching")
else:
    print("The car you want is not available")
print()

"""
4. Aceași listă
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
"""
print("Pct.4")
for item in cars:
    if item in ('Lastun', 'Trabant'):
        continue
    print(f"Maybe you would like the car {item}")
print()

"""
5. Modernizează parcul de mașini:
Crează o listă goală, masini_vechi.
Itereaza prin mașini.
Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.
"""
print("Pct.5")
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
old_cars = []

for i in range(len(cars)):
    if cars[i] == 'Lastun' or cars[i] == 'Trabant':
        old_cars.append(cars[i])
        cars[i] = 'Tesla'

print(f"Lista de masini vechi: {old_cars}")
print(f"Noua lista de masini: {cars}")
print()

"""
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezintă doar mașinile care se încadrează în acest buget.
Itereaza prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașina Lastun
Iterează prin listă
"""
print("Pct.6")
cars_prices = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

client_budget = 15000
affordable_cars = []

for item in cars_prices.items():
    if item[1] <= 15000:
        print(f"For a budget under {client_budget}, you can buy the {item} car")
        affordable_cars.append(item)
print(f'The list of the affordable cars under the budget of {client_budget}: {affordable_cars}')
chosen_car = input('You should choose one car of the above list:\t')
chosen_car = chosen_car.title()
for item in affordable_cars:
    if item[0] == chosen_car:
        print(f"You bought the {item}")
print()

"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count)
"""
print("Pct.7")
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
counter = 0
print(f"The original list: {numbers}")
for item in numbers:
    if item == 3:
        counter += 1
print(f"We have '3' {counter} times in the list")
print()

"""
8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum)
"""
print("Pct.8")
nbs_sum = 0
for item in numbers:
    nbs_sum += item
print(f"The sum of the list numbers is: {nbs_sum}")
print()

"""
9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).
"""
print("Pct.9")
nbs_max = numbers[0]
for item in numbers:
    if nbs_max < item:
        nbs_max = item
print(f"The max number is: {nbs_max}")
print()

"""
10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.
"""
print("Pct.10")
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(f"The original list: {numbers}")
for i in range(len(numbers)):
    if numbers[i] > 0:
        numbers[i] = -numbers[i]
print(f"The list of the negative numbers: {numbers}")
print()

"""
OPTIONAL
1.alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
"""
print("Pct.O1")
other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []

print(f"The original list: {other_numbers}")
for item in other_numbers:
    if item % 2 == 0:
        even_numbers.append(item)
    else:
        odd_numbers.append(item)
    if item > 0:
        positive_numbers.append(item)
    else:
        negative_numbers.append(item)
print(f"Even numbers list: {even_numbers}")
print(f"Odd numbers list: {odd_numbers}")
print(f"Positive numbers list: {positive_numbers}")
print(f"Negative numbers list: {negative_numbers}")
print()

"""
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort
"""
print("Pct.O2")
numbers_list = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
print(f"Original list = {numbers_list}")
for i in range(len(numbers_list) - 1):
    changed = False
    for j in range(len(numbers_list) - 1 - i):
        if numbers_list[j] > numbers_list[j + 1]:
            numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
            changed = True
    if not changed:
        break
print(f"Sorted list = {numbers_list}")
print()

"""
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while. User alege un număr. Programul îi spune:
-Nr secret e mai mare
-Nr secret e mai mic
-Felicitări! Ai ghicit!
"""
print("Pct.O3")
while True:
    secret_number = random.randint(1, 30)
    while True:
        guessed_number = input("\nGuess the secret number of the interval (1,30):\t")
        if guessed_number.isdigit():
            if 0 < int(guessed_number) <= 30:
                if int(guessed_number) < secret_number:
                    print("The secret number is bigger! Try again!\n")
                    continue
                elif int(guessed_number) > secret_number:
                    print("The secret number is smaller! Try again!\n")
                    continue
                else:
                    print(f"Congratulations! You've guessed the secret number! {secret_number}")
                    break
            else:
                print("\nInvalid input! Try again!\n")
        else:
            print("\nInvalid input! Try again!\n")

    answer = input("\nDo you want to continue?(Y/N)\t")
    if answer.upper() == 'Y':
        continue
    elif answer.upper() == 'N':
        break
    else:
        print("\nInvalid input! Program stops!")
        break
print()

"""
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
"""
print("Pct.O4")
x = int(input("Enter a number: "))
for row in range(x+1):
    for col in range(row):
        print(row, end='')
    print()
print()

"""
5.tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
"""
print("Pct.O5")
phone_keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i in phone_keypad:
    for j in i:
        print(f"The current digit is {j}")
print()
