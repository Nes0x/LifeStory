import random

def game():
    name = ("Andrzej", "Kuba", "Janusz", "Adrian", "Artur", "Stasiek", "Marek", "Sławek", "Maciek", "Mirosław", "Karol", "Patryk", "Zuzia", "Aleksandra", "Ola", "Nina")
    rich = ("Bogaty/a", "Biedny/a")
    dead_information = ("apokalipsy", "wypadku samochodowego", "katastrofy lotniczej", "zestarzenia", "powód niezany")
    profession = ("Programista", "Budowlaniec", "Lekarz", "Kasjer", "Nauczyciel", "Architekt", "Pracownik obsługi klienta")
    birthday = ("Styczniu", "Lutym", "Marcu", "Kwietniu", "Maju", "Czerwcu", "Lipcu", "Sierpniu", "Wrześniu", "Październiku", "Listopadzie", "Grudniu")


    birthday_rand = random.choice(birthday)
    profession_rand = random.choice(profession)
    name_rand = random.choice(name)
    rich_rand = random.choice(rich)
    age = random.randint(16, 100)
    dead = random.randint(age, 100)
    dead_information_rand = random.choice(dead_information)
    marry = random.randint(age, dead)

    if rich_rand == 0:
        money = random.randint(5000, 9000)
    else:
        money = random.randint(2800, 4000)

    print(f"""Masz na imie {name_rand} 
Masz {age} lat/a
Jesteś {rich_rand}
Urodziłeś/aś się w {birthday_rand}
Swoją drugą połówkę znalazłeś/aś w wieku {marry} lat
Miesięcznie zarabiasz {money} zł
Pracujesz jako {profession_rand}
Umarłes/aś w wieku {dead} lat w wyniku {dead_information_rand}""")



game()

while True:
    game_information = input("Czy chcesz grać dalej? Wpisz 1 jeśli chcesz przerwać, jeśli chcesz grać dalej kliknij enter")
    if gameInformation == "1":
    	print("Żegnaj!")
    	break
    else:
    	game()
