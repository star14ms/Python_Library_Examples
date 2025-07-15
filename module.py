from rich import print

class Human():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print(f"[bold green]Hello, my name is {self.name} and I am {self.age} years old.[/bold green]")

    def say_goodbye(self):
        print(f"[bold red]Goodbye, my name is {self.name} and I am {self.age} years old.[/bold red]")
        
        
        
x = 1