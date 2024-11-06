fireball_damage = 500
potion_mana = 100
fireball_cost = 50


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target):
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        self.mana -= fireball_cost
        target.get_fireballed()
            

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def get_fireballed(self):
        self.health -= fireball_damage

    def drink_mana_potion(self):
        self.mana += potion_mana

def main():

    dumbledore = Wizard("Albus Dumbledore", 150, 400)
    voldemort = Wizard("Lord Voldemort", 220, 370)

    dumbledore.cast_fireball(voldemort)
    print(dumbledore.is_alive())

main()