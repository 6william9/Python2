import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        if self.hunger > 10:
            self.hunger -= 10
            self.happiness += 5
            print(f"{self.name} поїв і став щасливішим!")
        else:
            print(f"{self.name} не голодний.")

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.hunger += 10
        print(f"{self.name} поспав і відновив енергію!")

    def play(self):
        if self.energy > 20:
            self.happiness += 15
            self.energy -= 20
            print(f"{self.name} погрався і став щасливішим!")
        else:
            print(f"{self.name} занадто втомлений, щоб гратися.")

    def status(self):
        print(f"{self.name} ({self.species})\n"
              f"Голод: {self.hunger}/100\n"
              f"Енергія: {self.energy}/100\n"
              f"Щастя: {self.happiness}/100\n")

    def live_a_day(self):
        print(f"--- День з {self.name} ---")
        self.status()
        self.hunger += random.randint(5, 15)
        self.energy -= random.randint(5, 15)
        self.happiness -= random.randint(5, 10)

        action = random.choice([self.feed, self.sleep, self.play])
        action()
        self.status()

# Приклад використання
pet = Pet("Барсик", "котик")
for _ in range(3):
    pet.live_a_day()
