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

        self.__pokemons: np.ndarray = np.array([
            #   Name        Type           Health   Power
            ('Charizard',  'Fire',           80,     80),  # Fire
            ('Arcanine',   'Fire',           90,     95),  # Fire
            ('Pikachu',    'Electric',       50,     75),  # Electric
            ('Jolteon',    'Electric',       70,     90),  # Electric
            ('Squirtle',   'Water',          50,     70),  # Water
            ('Vaporeon',   'Water',         100,     70),  # Water
            ('Bulbasaur',  'Grass',          50,     85),  # Grass
            ('Leafeon',    'Grass',          70,    100),  # Grass
            ('Eevee',      'Normal',         50,     80),  # Normal
            ('Snorlax',    'Normal',        100,     90),  # Normal
            ('Glaceon',    'Ice',            70,     90),  # Ice
            ('Froslass',   'Ice',            80,     85),  # Ice
        ], dtype=self.__pokemon_dtype)
        
        self.__elemental_counters = {
            'Fire': {
                'weak_to': ['Water'], 
                'strong_against': ['Grass', 'Ice']
            },
            'Water': {
                'weak_to': ['Electric', 'Grass'], 
                'strong_against': ['Fire', 'Ice']
            },
            'Electric': {
                'weak_to': [],  # Electric has no weaknesses in current roster
                'strong_against': ['Water']
            },
            'Grass': {
                'weak_to': ['Fire', 'Ice'], 
                'strong_against': ['Water']
            },
            'Normal': {
                'weak_to': [],
                'strong_against': []
            },
            'Ice': {
                'weak_to': ['Fire', 'Water'], 
                'strong_against': ['Grass']
            }
        }

    def get(self) -> list:
        return self.__pokemons

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
    
    # 🟧 in progress
    def is_element_countered(self, attacker_type: str, defender_type: str) -> str:
        is_strong_to = self.__elemental_counters.get(attacker_type, {}).get('strong_against', [])
        is_weak_to = self.__elemental_counters.get(attacker_type, {}).get('weak_to', [])
        
        if defender_type in is_strong_to:
            return "opponent countered"
        elif defender_type in is_weak_to:
            return "player countered"
        else:
            return "neutral"
        

# 🐞Debugging
if __name__ == "__main__":
    import main
    main.Gameplay()