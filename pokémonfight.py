import random

print(f"Un combat se lance entre 2 dresseurs : ")
print(f"\nJoueur 1 invoque : Salamèche ")
print(f"Joueur 2 invoque : Bulbizarre ")

class PokemonFeu:
    def __init__(self, nom):
        self.nom = nom
        self.sante = 100

    def attaquer(self, pokemon_plante):
        print(f"\n{self.nom} attaque {pokemon_plante.nom} !")
        degats = random.randint(15, 20)
        print(f"{self.nom} fait un coup critique !! Les dégâts sont multipliés par 2. \n{pokemon_plante.nom} perd {degats * 2} points de vie!!")
        pokemon_plante.sante -= degats * 2
        if pokemon_plante.sante < 0:
            pokemon_plante.sante = 0  
        print(f"Il reste {pokemon_plante.sante} points de vie à {pokemon_plante.nom}!")


class PokemonPlante:
    def __init__(self, nom):
        self.nom = nom
        self.sante = 100

    def attaquer(self, pokemon_feu):
        print(f"\n{self.nom} attaque {pokemon_feu.nom} !")
        degats = random.randint(15, 20)
        print(f"L'attaque de {self.nom} n'est pas très efficace. \n{pokemon_feu.nom} perd {degats} points de vie!!")
        pokemon_feu.sante -= degats
        if pokemon_feu.sante < 0:
            pokemon_feu.sante = 0  
        print(f"Il reste {pokemon_feu.sante} points de vie à {pokemon_feu.nom}!")


salameche = PokemonFeu("Salamèche")
bulbizarre = PokemonPlante("Bulbizarre")
expérience = random.randint(80,123)

while bulbizarre.sante > 0 and salameche.sante > 0:
    salameche.attaquer(bulbizarre)
    
    if bulbizarre.sante > 0: 
        bulbizarre.attaquer(salameche)


if bulbizarre.sante == 0:
    print(f"{bulbizarre.nom} est KO ! {salameche.nom} remporte le combat !")
else:
    print(f"{salameche.nom} est KO ! {bulbizarre.nom} remporte le combat !")

print(f"\n{salameche.nom} remporte {expérience} points d'expérience !")
