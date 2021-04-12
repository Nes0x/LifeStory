import random

def game():
    name = ["Andrzej", "Kuba", "Janusz", "Adrian", "Artur", "Stasiek", "Marek", "Sławek", "Maciek", "Mirosław", "Karol", "Patryk", "Zuzia", "Aleksandra", "Ola", "Nina"]
    rich = ["Bogaty/a", "Biedny/a"]
    deadInformation = ["apokalipsy", "wypadku samochodowego", "katastrofy lotniczej", "zestarzenia", "powód niezany"]
    profession = ["Programista", "Budowlaniec", "Lekarz", "Kasjer", "Nauczyciel", "Architekt", "Pracownik obsługi klienta"]
    birthday = ["Styczniu", "Lutym", "Marcu", "Kwietniu", "Maju", "Czerwcu", "Lipcu", "Sierpniu", "Wrześniu", "Październiku", "Listopadzie", "Grudniu"]



    valueOfNames = len(name) - 1
    valueOfDeadInformation = len(deadInformation) - 1
    valueOfProfession = len(profession) - 1
    valueOfBirthday = len(birthday) - 1

    birthdayRand = random.randint(0, valueOfBirthday)
    professionRand = random.randint(0, valueOfProfession)
    nameRand = random.randint(0, valueOfNames)
    richRand = random.randint(0, 1)
    age = random.randint(16, 100)
    dead = random.randint(age, 100)
    deadInformationRand = random.randint(0, valueOfDeadInformation)
    marry = random.randint(age, dead)

    if richRand == 0:
        money = random.randint(5000, 9000)
    else:
        money = random.randint(2800, 4000)

    print(f"Masz na imie {name[nameRand]} \nMasz {age} lat/a \nJesteś {rich[richRand]} \nUrodziłeś/aś się w {birthday[birthdayRand]} \nSwoją drugą połówkę znalazłeś/aś w wieku {marry} lat \nMiesięcznie zarabiasz {money} zł \nPracujesz jako {profession[professionRand]} \nUmarłes/aś w wieku {dead} lat w wyniku {deadInformation[deadInformationRand]}")


while True:
    gameInformation = input("Czy chcesz grać? Wpisz nie jeśli chcesz przerwać, jeśli chcesz grać dalej kliknij enter")
    if gameInformation == "nie":
        break
    else:
        game()
