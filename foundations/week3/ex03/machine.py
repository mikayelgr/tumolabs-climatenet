from beverages import Coffee, Tea, Chocolate, Cappuccino, HotBeverage
import random

class CoffeeMachine:
    def __init__(self):
        self.drinks_served = 0

    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.drinks_served = 0

    def serve(self, beverage_class):
        if self.drinks_served >= 10:
            raise self.BrokenMachineException()

        self.drinks_served += 1
        return random.choice([beverage_class(), self.EmptyCup()])

if __name__ == "__main__":
    machine = CoffeeMachine()
    beverages = [Coffee, Tea, Chocolate, Cappuccino]

    while True:
        try:
            drink = machine.serve(random.choice(beverages))
            print(drink)
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            print("Repairing the machine...")
            machine.repair()
