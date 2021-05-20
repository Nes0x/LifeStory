import random

def game():
    name = ("Andrzej", "Kuba", "Janusz", "Adrian", "Artur", "Stasiek", "Marek", "Sławek", "Maciek", "Mirosław", "Karol", "Patryk", "Zuzia", "Aleksandra", "Ola", "Nina")
    rich = ("Bogaty/a", "Biedny/a")
    deadInformation = ("apokalipsy", "wypadku samochodowego", "katastrofy lotniczej", "zestarzenia", "powód niezany")
    profession = ("Programista", "Budowlaniec", "Lekarz", "Kasjer", "Nauczyciel", "Architekt", "Pracownik obsługi klienta")
    birthday = ("Styczniu", "Lutym", "Marcu", "Kwietniu", "Maju", "Czerwcu", "Lipcu", "Sierpniu", "Wrześniu", "Październiku", "Listopadzie", "Grudniu")


    birthdayRand = random.choice(birthday)
    professionRand = random.choice(profession)
    nameRand = random.choice(name)
    richRand = random.choice(rich)
    age = random.randint(16, 100)
    dead = random.randint(age, 100)
    deadInformationRand = random.choice(deadInformation)
    marry = random.randint(age, dead)

    if richRand == 0:
        money = random.randint(5000, 9000)
    else:
        money = random.randint(2800, 4000)

    print(f"""Masz na imie {nameRand} 
Masz {age} lat/a
Jesteś {richRand}
Urodziłeś/aś się w {birthdayRand}
Swoją drugą połówkę znalazłeś/aś w wieku {marry} lat
Miesięcznie zarabiasz {money} zł
Pracujesz jako {professionRand}
Umarłes/aś w wieku {dead} lat w wyniku {deadInformationRand}""")



game()

while True:
    gameInformation = input("Czy chcesz grać dalej? Wpisz 1 jeśli chcesz przerwać, jeśli chcesz grać dalej kliknij enter")
    if gameInformation == "1":
    	print("Żegnaj!")
    	break
    else:
    	game()
