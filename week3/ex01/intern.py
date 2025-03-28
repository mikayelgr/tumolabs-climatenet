class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."

class Intern:
    def __init__(self, Name="My name? I’m nobody, an intern, I have no name."):
        self.Name = Name

    def __str__(self):
        return self.Name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return Coffee()

if __name__ == "__main__":
    intern1 = Intern()
    intern2 = Intern("Mark")
    
    print(intern1)
    print(intern2)
    
    coffee = intern2.make_coffee()
    print(coffee)
    
    try:
        intern1.work()
    except Exception as e:
        print(e)
