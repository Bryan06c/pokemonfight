import random

from utils.custom_logs import RED, GREEN, BLUE, RESET

degats = random.randint(15, 20)

class Pokemon:
    def __init__(self,nom,sante):
        self.nom = nom
        self.sante = sante

    def attaquer(self, pokemon):
        print(f"\n{self.nom} attaque {pokemon.nom} !")

        if self.cat == "feu":
            PokemonFeu.attaqueFeu(self, pokemon)
        
        if self.cat == "plant":
            PokemonPlante.attaquePlante(self, pokemon)

        if self.cat == "water":
            PokemonEau.attaqueEau(self, pokemon)

        if pokemon.sante < 0:
            pokemon.sante = 0  
        print(f"Il reste {pokemon.sante} points de vie à {pokemon.nom}!")

class PokemonFeu(Pokemon):
    def __init__(self, nom):
        super().__init__(nom)
        self.cat = "feu"
    
    def attaqueFeu(self, pokemon):
        if pokemon.cat == "plant":
            print(f"{RED}{self.nom} envoie Lance Flamme !! Les dégâts sont multipliés par 2.{RESET} \n{pokemon.nom} perd {degats * 2} points de vie!!")
            pokemon.sante -= degats * 2
        else:
            print(f"{RED}L'attaque Lance Flamme de {self.nom} n'est pas très efficace.{RESET} \n{pokemon.nom} perd {degats} points de vie!!")
            pokemon.sante -= degats

class PokemonPlante(Pokemon):
    def __init__(self, nom):
        super().__init__(nom)
        self.cat = "plant"

    def attaquePlante(self, pokemon):
        if pokemon.cat == "water":
            print(f"{GREEN}{self.nom} envoie Tranche Herbe !! Les dégâts sont multipliés par 2.{RESET} \n{pokemon.nom} perd {degats * 2} points de vie!!")
            pokemon.sante -= degats * 2
        else:
            print(f"{GREEN}L'attaque Tranche Herbe de {self.nom} n'est pas très efficace.{RESET} \n{pokemon.nom} perd {degats} points de vie!!")
            pokemon.sante -= degats


class PokemonEau(Pokemon):
    def __init__(self, nom):
        super().__init__(nom)
        self.cat = "water"

    def attaqueEau(self, pokemon):
        if pokemon.cat == "feu":
            print(f"{BLUE}{self.nom} envoie Hydro Canon !! Les dégâts sont multipliés par 2.{RESET} \n{pokemon.nom} perd {degats * 2} points de vie!!")
            pokemon.sante -= degats * 2
        else:
            print(f"{BLUE}L'attaque Hydro Canon de {self.nom} n'est pas très efficace.{RESET} \n{pokemon.nom} perd {degats} points de vie!!")
            pokemon.sante -= degats