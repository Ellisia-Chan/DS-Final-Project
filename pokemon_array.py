import numpy as np

class Pokemon_Array:
    def __init__(self):
        self.__pokemon_dtype: np.dtype = np.dtype([
            ("Name", "U20"),
            ("Type", "U20"),
            ("Health", "i4"),
            ("Power", "i4")
        ])
        
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
    
    def show_pokemons(self) -> list:
        for pokemon in self.__pokemons:
            print(pokemon)

if __name__ == "__main__":
    pokemon_array = Pokemon_Array()
    pokemon_array.show_pokemons()
    