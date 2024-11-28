# 🟧 in progress
# ✅ working
# ⚠️ Untested

from LinkedList import Linked_List
from PokemonArray import Pokemon_Array

class Backend:
    def __init__(self) -> None:
        self.player1_pokemons, self.player2_pokemons  = Linked_List()
        self.pokemon_array = Pokemon_Array()

    def select_pokemon(self, player, chosen_pokemon) -> None:
        # Add selected Pokémon to Player 1's linked list
        if chosen_pokemon:
            player.insert_at_end(chosen_pokemon)
        
        self.pokemon_array.select_and_remove_pokemon(chosen_pokemon)






