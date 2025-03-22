

class Dog:
    def __init__(self,name: str,race: str, weight: float, pedigree: bool, color: str,age: int):
        self.name = name
        self.race = race
        self.weight = weight 
        self.pedigree = pedigree
        self.color = color
        self.age = age
        self.status_awake = 1
    
    def sleep(self):
        if self.status_awake
            self.status_awake = False
            return f"o {self.name} foi dormir."
        else:
            return "Mas esse cachorro já está dormindo!!"
    
    def awake(self):
        if self.status_awake
            return "Mas esse cachorro já está acordado"
        else
            self.status_awake = True
            return "Está acordado"
        
    def bark(self):
        return "Au, au, au"
        
    def eat(self,meal):
        return(f"Seu Aumigo {self.name} esta comendo {meal}: Sletp, sletp, sletp...")
    
    def play(self, game):
        return(f"Seu Aumigo {self.name} esta brincando de {game}: e está te chamando para brincar com ele: 'U-ul, ul,ul'")
    
    
    
        
dog1 = Dog(name="Catucha", race="cocker spaniel", weight=12,pedigree=1,color="Dourado",age=5)
dog2 = Dog(name="Dru", race="vira-lata", weight=20,pedigree=0,color="Dalmatado",age=2)

print(dog1.bark())
comida = input("Escreva o que vai de comer para o cachorro:  =>  ")
print(dog1.eat(meal=comida)) 
brinca = input("Diga o quê vai dar para o cachorro brincar. :) =>   ")  
print(dog1.play(game=brinca))
        
    
        