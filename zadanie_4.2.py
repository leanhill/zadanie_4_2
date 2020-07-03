import logging
import math

logging.basicConfig(level=logging.DEBUG,format='%(message)s')
type_of_operation = float(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
if type_of_operation == 1 or type_of_operation == 3: # blok daje możliwośc wpisania większej ilości liczb dla mnozenia i dodawania
    numbers = input("Podaj liczby, które mają być poddane obliczeniu, oddzielając je przecinkami.")
    numbers = numbers.split(",") #zamieniam wpisane liczby na listę
    for i in numbers: # ta pętla sprawdza czy wszystkie wpisy są liczbami.
        i = str(i)
        i = bool(i.replace('.', '').isdigit()) # rodzielam liczby float bym mógł efektywnie użyć isdigit().
        if i == False:
            print("Podałeś niepoprawny format liczby")
            exit()
        else:
            for i in range(len(numbers)):
                numbers[i] = float(numbers[i]) # zamieniam elelemnty na float by moc skorzystać z sum i math.prod
    if type_of_operation == 1:
        result = sum(numbers)
        logging.info(f'Sumuję liczby {numbers}')
        logging.info(f'Wynik to {result}')
    if type_of_operation == 3:
        result = math.prod(numbers)
        logging.info(f'Sumuję liczby {numbers}')
        logging.info(f'Wynik to {result}')
else:
     number_one = input("Podaj pierwszą liczbę")
     number_two = input("Podaj drugą liczbę")
     if number_one.replace('.', '').isdigit() == False or number_two.replace('.', '').isdigit() == False:
         print("Podałeś niepoprawny format liczby")
     else:
         if type_of_operation == 2:
             operation_name = "Odejmuję"
             result = float(number_one) - float(number_two)
         elif type_of_operation == 4:
             operation_name = "Dzielę"
             result = float(number_one) / float(number_two)
         logging.info(f'{operation_name} {number_one} i {number_two}')
         logging.info(f'Wynik to {result}')




