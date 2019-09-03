word_list = list()

def libs():
    location = input("Where do you like to eat?: ")
    word_list.append(location)
    food = input("What is your favorite food?: ")
    word_list.append(food)
    animal = input("What is the animal?: ")
    word_list.append(animal)
    instrument = input("What is the instrument?: ")
    word_list.append(instrument)
    noun = input("Put in a noun: ")
    word_list.append(noun)
    car = input("Put in a type of car: ")
    word_list.append(car)


    print("I went to {} then cruised down the street in my {} to get some grub over at {}. Went to the {} to get the scoop. {} out there shooting some hoop. All I wanted to do was go home and play my {} but then quickly realized I didn't get enough {}. Headed back home and went back to sleep.".format(location, car, location, location, noun, instrument, animal))
libs()

