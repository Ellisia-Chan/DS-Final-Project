# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 🐞Debugging

import numpy as np

class Pokemon_Array:
    # ✅ working
    # This method initialize the Pokemon_Array class
    # It creates a numpy data type to hold the data of the pokemon
    # The data type contains the name, type, health and power of the pokemon
    def __init__(self):
        self.__pokemon_dtype: np.dtype = np.dtype([
            ("Name", "U20"),
            ("Type", "U20"),
            ("Health", "i4"),
            ("Power", "i4")
        ])

        # ✅ working
        self.__pokemons: np.ndarray = np.array([
            #   Name        Type           Health   Power
            ('Charizard',  'Fire',           78,     84),  # Fire
            ('Arcanine',   'Fire',           90,     95),  # Fire
            ('Pikachu',    'Electric',       35,     55),  # Electric
            ('Jolteon',    'Electric',       65,    110),  # Electric
            ('Squirtle',   'Water',          44,     48),  # Water
            ('Vaporeon',   'Water',         130,     65),  # Water
            ('Bulbasaur',  'Grass',          45,     49),  # Grass
            ('Leafeon',    'Grass',          65,    110),  # Grass
            ('Eevee',      'Normal',         55,     55),  # Normal
            ('Snorlax',    'Normal',        160,    110),  # Normal
            ('Tauros',     'Normal',         75,    100),  # Normal
            ('Flareon',    'Fire',           65,    130),  # Fire
        ], dtype=self.__pokemon_dtype)

    # Show pokemon list with numbers (index)
    # This method prints the list of pokemons with their index to the console
    def show_pokemons(self):
        for idx, pokemon in enumerate(self.__pokemons):
            print(f"{idx + 1}: {pokemon}")

    # ✅ working
    # Select a pokemon by its index and remove it from the list
    # This method takes an index of a pokemon and remove it from the list
    # It returns the pokemon that was removed or None if the index is invalid
    def select_pokemon(self, index: int) -> list:
        index -= 1
        if index >= 0 and index < len(self.__pokemons):
            selected_pokemon = [str(x) if isinstance(x, np.str_) else int(x) for x in self.__pokemons[index]]
            return selected_pokemon
        else:
            print("Pokemon_Array: Invalid index!")
            return None
    
    def remove_pokemon(self, index_list: list) -> None:
        for index in sorted(index_list, reverse=True):
            self.__pokemons = np.delete(self.__pokemons, index - 1)
        
    # ✅ working
    # returns the size of the pokemon array
    def size(self) -> int:
        return len(self.__pokemons)

# 🐞Debugging
if __name__ == "__main__":
    import main
    main.Gameplay()
#     pokemon_array = Pokemon_Array()
#     pokemon_array.show_pokemons()

#     print("\n\n\nTest\n\n")
#     selected_pokemon_1 = pokemon_array.select_and_remove_pokemon(13)
#     print("\nTest\n\n")
#     pokemon_array.show_pokemons()
#     selected_pokemon_2 = pokemon_array.select_and_remove_pokemon(1)
    
#     print("\nTest\n\n")
#     print(selected_pokemon_1)
#     print(selected_pokemon_2)