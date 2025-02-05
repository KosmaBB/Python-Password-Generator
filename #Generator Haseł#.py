# Generator Haseł #

import string
import random

while True:  
    length = int(input("Wprowadź długość hasła: "))

    print('''Wybierz rodzaje znaków jakie zostaną użyte do stworzenia hasła: 
            1. Litery
            2. Cyfry
            3. Znaki specjalne
            4. Dalej''')

    characterList = ""

    while True:  
        choice = int(input("Wybierz liczbę (1-4): "))

        if choice == 1:
            characterList += string.ascii_letters
        
        elif choice == 2:
            characterList += string.digits
        
        elif choice == 3:
            characterList += string.punctuation
        
        elif choice == 4:
            if characterList: 
                break  
            else:
                print("Musisz wybrać przynajmniej jedną opcję zanim przejdziesz dalej!")
        else:
            print("Błędna wartość! Wybierz liczbę od 1 do 4.")

    password = []

    for i in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)

    print("Twoje hasło brzmi: " + "".join(password))

    another = input("Czy chcesz stworzyć kolejne hasło? (tak/nie): ").strip().lower()
    if another != 'tak':
        break

print("Dziękujemy za skorzystanie z generatora haseł!")
