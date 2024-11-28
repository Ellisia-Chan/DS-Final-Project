# 🟧 in progress
# ✅ working
# ⚠️ Untested

import numpy as np

class Pokemon_Array:
    # ✅ working
    def __init__(self):
        self.__pokemon_dtype: np.dtype = np.dtype([
            ("Name", "U20"),
            ("Type", "U20"),
            ("Health", "i4"),
            ("Power", "i4")
        ])

        # ✅ working
        self.__pokemons: np.ndarray = np.array([
            #   Name          Type          Health   Power
            ('Pikachu',    'Electric',        35,     55),
            ('Charizard',  'Fire/Flying',     78,     84),
            ('Bulbasaur',  'Grass/Poison',    45,     49),
            ('Squirtle',   'Water',           44,     48),
            ('Jigglypuff', 'Fairy/Normal',    115,    45),
            ('Gengar',     'Ghost/Poison',    60,     65),
            ('Eevee',      'Normal',          55,     55),
            ('Snorlax',    'Normal',          160,   110),
            ('Machamp',    'Fighting',        90,    130),
            ('Dragonite',  'Dragon/Flying',   91,    134),
            ('Vaporeon',   'Water',           130,    65),
            ('Lucario',    'Fighting/Steel',  70,    110),
        ], dtype=self.__pokemon_dtype)
    
    # Show pokemon list with numbers (index)
    def show_pokemons(self):
        for idx, pokemon in enumerate(self.__pokemons):
            print(f"{idx}: {pokemon}")

    # ✅ working
    def select_and_remove_pokemon(self, index: int):
        if 0 <= index < len(self.__pokemons):
            selected_pokemon = self.__pokemons[index]
            self.__pokemons = np.delete(self.__pokemons, index)
            return selected_pokemon
        else:
            print("Invalid index!")
            return None

# if __name__ == "__main__":
#     pokemon_array = Pokemon_Array()
#     pokemon_array.show_pokemons()

#     print("\n\n\nTite\n\n")
#     pokemon_array.select_and_remove_pokemon(0)
#     pokemon_array.select_and_remove_pokemon(1)
#     print("\nTite\n\n")
#     pokemon_array.show_pokemons()