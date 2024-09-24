import random

class PokemonFeu:
    def __init__(self, nom):
        self.nom = nom
        self.sante = 100

    def attaquer(self, pokemon):
        print(f"\n{self.nom} attaque {pokemon.nom} !")
        degats = random.randint(15, 20)

        if pokemon.nom == "Bulbizarre" or pokemon.nom == "Florizarre":
            print(f"{self.nom} fait un coup critique !! Les dégâts sont multipliés par 2. \n{pokemon.nom} perd {degats * 2} points de vie!!")
            pokemon.sante -= degats * 2
        else:
            print(f"L'attaque de {self.nom} n'est pas très efficace. \n{pokemon.nom} perd {degats} points de vie!!")
            pokemon.sante -= degats

        if pokemon.sante < 0:
            pokemon.sante = 0  
        print(f"Il reste {pokemon.sante} points de vie à {pokemon.nom}!")

class PokemonPlante:
    def __init__(self, nom):
        self.nom = nom
        self.sante = 100

    def attaquer(self, pokemon):
        print(f"\n{self.nom} attaque {pokemon.nom} !")
        degats = random.randint(15, 20)
        
        print(f"L'attaque de {self.nom} n'est pas très efficace. \n{pokemon.nom} perd {degats} points de vie!!")
        pokemon.sante -= degats

        if pokemon.sante < 0:
            pokemon.sante = 0  
        print(f"Il reste {pokemon.sante} points de vie à {pokemon.nom}!")


salameche = PokemonFeu("Salamèche")
dracofeu = PokemonFeu("Dracofeu")
bulbizarre = PokemonPlante("Bulbizarre")
florizarre = PokemonPlante("Florizarre")

pokemon = []

pokemon.append(salameche)
pokemon.append(dracofeu)
pokemon.append(bulbizarre)
pokemon.append(florizarre)

def state(liste_de_pokemon):
    for pokemon in liste_de_pokemon:
        print(pokemon.nom, pokemon.sante)

experience = random.randint(80,123)

i1 = random.randint(0,3)

i2 = random.randint(0,3)

# Le jeu commence ici

print(f"""
Un combat se lance entre 2 dresseurs :

Joueur 1 invoque : {pokemon[i1].nom}
Joueur 2 invoque : {pokemon[i2].nom}
""")

while pokemon[i1].sante > 0 and pokemon[i2].sante > 0:
    pokemon[i1].attaquer(pokemon[i2])
    state(pokemon)
    
    if pokemon[i2].sante > 0:
        pokemon[i2].attaquer(pokemon[i1])
        state(pokemon)


if pokemon[i1].sante == 0:
    print(f"{pokemon[i1].nom} est KO ! {pokemon[i2].nom} remporte le combat !")
    print(f"\n{pokemon[i2].nom} remporte {experience} points d'expérience !")
else:
    print(f"{pokemon[i2].nom} est KO ! {pokemon[i1].nom} remporte le combat !")
    print(f"\n{pokemon[i1].nom} remporte {experience} points d'expérience !")


