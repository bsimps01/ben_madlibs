word_list = list()

def libs():
    location = input("Location of favorite place to eat: ")
    word_list.append(location)
    food = input("What is your favorite food?: ")
    word_list.append(food)
    animal = input("What is your favorite animal?: ")
    word_list.append(animal)
    instrument = input("What is your favorite instrument?: ")
    word_list.append(instrument)
    noun = input("Put in a noun: ")
    word_list.append(noun)
    car = input("Put in a type of car: ")
    word_list.append(car)
    sport = input("Favorite Sport: ")
    word_list.append(sport)


    print("I went to {} then cruised down the street in my {} to get some grub over at {}. Went to the {} to get the scoop. {} out there shooting some hoop. All I wanted to do was go home and play my {} but then quickly realized I didn't get enough {}. Headed back home and went to sleep after watching {}.".format( location, car, location, location, noun, instrument, animal, sport))
libs()