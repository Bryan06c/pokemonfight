from modules.classes import Pokemon, PokemonEau, PokemonFeu, PokemonPlante
from modules.pokemonfight import fight, pokemon, i1, i2, i3





# Le jeu commence ici

print(f"""
Un combat se lance entre 2 dresseurs :

Joueur 1 invoque : {pokemon[i1].nom}
Joueur 2 invoque : {pokemon[i2].nom}
Joueur 3 invoque : {pokemon[i3].nom}
""")

fight()

