from datetime import datetime
import pytz

"""
OBLIGATORII
1.Funcție care să calculeze și să returneze suma a două numere
"""
print("Ex.1")


def sum_of_2_numbers(x, y):
    return x + y


x, y = input("\nEnter 2 numbers to get their sum:\t").split()
x = int(x)
y = int(y)
print(f"\nThe sum is: {sum_of_2_numbers(x, y)}")
print()

"""
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
"""
print("Ex.2")


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


x = int(input("\nEnter a number to find out if it's even:\t"))
print(is_even(x))
print()

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""
print("Ex.3")


def number_characters(name):
    counter = 0
    list_name = name.split()
    for item in list_name:
        counter = counter + len(item)
    return counter


your_name = input("\nEnter your full name:\t")
print(f"\nYour name has a total of {number_characters(your_name)} characters")
print()

"""
4. Funcție care returnează aria dreptunghiului
"""
print("Ex.4")


def rectangle_area(a, b):
    r_area = a * b
    return r_area


x, y = input("\nEnter the lenghts of the members of a rectangle:\t").split()
x = float(x)
y = float(y)
print(f"\nThe area of the rectangle is {rectangle_area(x , y)}")
print()

"""
5. Funcție care returnează aria cercului
"""
print("Ex.5")


def circle_area(r):
    c_area = 3.14*r**2
    return c_area


x = float(input("\nEnter the radius of a circle:\t"))
print(f"\nThe area of the circle is {circle_area(x)}")
print()

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește
"""
print("Ex.6")


def char_search(c, s):
    if c in s:
        return True
    return False


user_str = input("\nEnter a string:\t")
user_char = input("\nEnter a character to search it in the string:\t")
print(char_search(user_char, user_str))
print()

"""
7. Funcție fără return, primește un string și printează pe ecran:
- Nr de caractere lower case este x
- Nr de caractere upper case exte y
"""
print("Ex.7")


def lower_upper(user_str):
    lower_counter = 0
    upper_counter = 0
    for i in user_str:
        if i.islower():
            lower_counter += 1
        elif i.isupper():
            upper_counter += 1
    print(f"\nNumber of lower characters: {lower_counter}\nNumber of upper characters: {upper_counter}")


str1 = input("\nEnter a string to count the lower and upper characters:\n")
lower_upper(str1)
print()

"""
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
"""
print("Ex.8")


def positive_user_list(user_list):
    positive_list = []
    for item in user_list:
        if item > 0:
            positive_list.append(item)
    return positive_list


numbers_list = [0, 15, -6, -45, 0, -6, 30, 15, 77, -155]
print(f"The original numbers list: {numbers_list}")
print(f"The posistive numbers list: {positive_user_list(numbers_list)}")
print()

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
- Primul număr x este mai mare decat al doilea nr y
- Al doilea nr y este mai mare decat primul nr x
- Numerele sunt egale
"""
print("Ex.9")


def compare(x, y):
    if x > y:
        print(f"\n{x} is bigger than {y}")
    elif x < y:
        print(f"\n{y} is bigger than {x}")
    else:
        print(f"\n{x} is equal to {y}")


a, b = input("\nEnter 2 numbers to compare:\t").split()
a = int(a)
b = int(b)
compare(a, b)
print()

"""
10. Funcție care primește un număr și un set de numere.
- Printeaza ‘am adaugat numărul nou în set’ + returnează True
- Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
"""
print("Ex.10")


def enter_set(user_set, new_number):
    if new_number not in user_set:
        user_set.add(new_number)
        print(f"\n{new_number} was added to the set")
        return True, user_set
    else:
        print(f"\n{new_number} was not added to the set, it already exists")
        return False, user_set


set1 = {-45, 0, 2, 3, 10, -55, -12, 66}
while True:
    x = int(input(f"\nEnter a new number to add it to the set\nThe set: {set1}\n"))
    print(enter_set(set1, x))

    user_wish = input("\nDo you want to continue?(Y/N)\t")
    if user_wish.upper() == 'Y':
        continue
    elif user_wish.upper() == 'N':
        break
    else:
        print("\nInvalid input! Programul se opreste!")
        break
print()

"""
OPTIONALE
O1. Funcție care primește o lună din an și returnează câte zile are acea l
"""
print("Ex.O1")


def month_checker(user_month):
    months = {
        'January': '31',
        'February': '28/29',
        'March': '31',
        'April': '30',
        'May': '31',
        'June': '30',
        'July': '31',
        'August': '31',
        'September': '30',
        'October': '31',
        'November': '30',
        'December': '31'
    }
    user_month = user_month.capitalize()
    print(f"\n{user_month} has {months[user_month]} days")


while True:
    month = input("\nEnter a month to find the number of days(letters):\t")
    month_checker(month)

    continue_answer = input("\nDo you want to continue?(Y/N)\t")
    if continue_answer.upper() == 'Y':
        continue
    elif continue_answer.upper() == 'N':
        break
    else:
        print("\nInvalid input! Program stopped")
        break
print()

"""
O2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
- print("Suma: ", a)
- print("Diferenta: ", b)
- print("Inmultirea: ", c)
- print("Impartirea: ", d)
"""
print("Ex.O2")


def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d


user_x, user_y = input("\nEnter 2 numbers:\t").split()
user_x = int(user_x)
user_y = int(user_y)

a, b, c, d = calculator(user_x, user_y)
print(f"\nSum: {a}")
print(f"Difference: {b}")
print(f"Multiplication: {c}")
print(f"Division: {d}")
print()


"""
O3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""
print("Ex.O3")


def list_dict(user_list):
    number_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for i in number_dict:
        counter = 0
        for item in user_list:
            if item == i:
                counter += 1
        number_dict[i] = counter
    return number_dict


list1 = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(f"The original list: {list1}")
print(f"Counter dictionary: {list_dict(list1)}")
print()

"""
O4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
"""
print("Ex.O4")


def max_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


x, y, z = input("\nEnter 3 numbers to find out the max:\t").split()
x = int(x)
y = int(y)
z = int(z)
print(f"\nThe max number is: {max_number(x, y, z)}")
print()

"""
O5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
"""
print("Ex.O5")


def total_sum(user_nb):
    nb_sum = 0
    for i in range(user_nb+1):
        nb_sum += i
    return nb_sum


x = int(input("\nEnter a number to get the sum of all the numbers from zero to the number:\t"))
print(f"The sum of all the numbers from 0 to {x} is {total_sum(x)}")
print()


"""
OPTIONALE BONUS
B1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""
print("Ex.B1")


def lists_intersection(user_list1, user_list2):
    set1 = set(user_list1)
    set2 = set(user_list2)
    return set1.intersection(set2)


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
print(f"The intersection of {list1} and {list2} is {lists_intersection(list1, list2)}")
print()

"""
B2.Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă
"""
print("Ex.B2")


def discount_calculator(user_price, user_discount):
    if 0 < user_discount < 100:
        final_price = user_price - user_price * user_discount / 100
        return final_price
    else:
        print("\nThe entered discount is invalid!")


price = float(input("\nEnter the product price to calculate the discount price:\t"))
discount = float(input("\nEnter the discount (%):\t"))
print(f"\nThe final price is: {round(discount_calculator(price, discount), 2)}")
print()

"""
B3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
"""
print("Ex.B3")


def romania_time():
    romania_time_now = datetime.now().time()
    return romania_time_now


def china_time():
    china_timezone = pytz.timezone('Asia/Shanghai')
    china_time_now = datetime.now(china_timezone).time()
    return china_time_now


print(f"\nOra in Romania: {romania_time()}")
print(f"\nOra in China: {china_time()}")
print()

"""
B4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""
print("Ex.B4")


def calculator_aniversare(data_aniversare):
    data_curenta = datetime.now()
    data_curenta_string = str(datetime.now())
    if int(data_curenta_string[5:7]) > int(aniversare[0:2]) and int(data_curenta_string[8:10]) > int(aniversare[3:]):
        data_aniversare = data_aniversare + '/2023'
        data_aniversare_ms = datetime.strptime(data_aniversare, "%m/%d/%Y")
        delta = data_aniversare_ms - data_curenta
        return delta.days
    else:
        data_aniversare = data_aniversare + '/2022'
        data_aniversare_ms = datetime.strptime(data_aniversare, "%m/%d/%Y")
        delta = data_aniversare_ms - data_curenta
        return delta.days


aniversare = input("\nIntrodu data aniversarii tale (ll/zz):\t")
print(f"\nMai sunt {calculator_aniversare(aniversare)} zile pana la ziua ta")
print()
