import random
from modules.classes import Pokemon, PokemonEau, PokemonFeu, PokemonPlante


experience = random.randint(80, 123)

i1 = 0
i2 = 0
i3 = 0
while i1 == i2 or i1 == i3 or i2 == i3:
    i1 = random.randint(0, 5)
    i2 = random.randint(0, 5)
    i3 = random.randint(0, 5)

pokemon = [
    PokemonFeu("Salamèche"),
    PokemonFeu("Dracaufeu"),
    PokemonPlante("Bulbizarre"),
    PokemonPlante("Florizarre"),
    PokemonEau("Carapuce"),
    PokemonEau("Tortank")
]

def fight():
    
    while pokemon[i1].sante > 0 and pokemon[i2].sante > 0 or pokemon[i1].sante > 0 and pokemon[i3].sante > 0 or pokemon[i2].sante > 0 and pokemon[i3].sante > 0:
      
        if pokemon[i1].sante > 0:
            if pokemon[i2].sante > 0:
                pokemon[i1].attaquer(pokemon[i2])
            elif pokemon[i1].attaquer(pokemon[i3]):
                pass

      
        if pokemon[i2].sante > 0:
            if pokemon[i3].sante > 0:
                pokemon[i2].attaquer(pokemon[i3])
            elif pokemon[i2].attaquer(pokemon[i1]):
                pass

    
        if pokemon[i3].sante > 0:
            if pokemon[i1].sante > 0:
                pokemon[i3].attaquer(pokemon[i1])
            elif pokemon[i3].attaquer(pokemon[i2]):
                pass


    if pokemon[i1].sante == 0 and pokemon[i2].sante == 0:
        print(f"{pokemon[i1].nom} et {pokemon[i2].nom} sont KO ! {pokemon[i3].nom} remporte le combat !")
        print(f"\n{pokemon[i3].nom} remporte {experience} points d'expérience !")
    elif pokemon[i1].sante == 0 and pokemon[i3].sante == 0:
        print(f"{pokemon[i1].nom} et {pokemon[i3].nom} sont KO ! {pokemon[i2].nom} remporte le combat !")
        print(f"\n{pokemon[i2].nom} remporte {experience} points d'expérience !")
    elif pokemon[i2].sante == 0 and pokemon[i3].sante == 0:
        print(f"{pokemon[i2].nom} et {pokemon[i3].nom} sont KO ! {pokemon[i1].nom} remporte le combat !")
        print(f"\n{pokemon[i1].nom} remporte {experience} points d'expérience !")