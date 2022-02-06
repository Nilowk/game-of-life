import random

secret_number = random.randint(1, 10001)

while True:
    selected_number = int(input("choisissez un nombre entre 0 et 10 000 >> "))

    if secret_number == selected_number:
        print("bravo tu as gagné")
        break