# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 🐞Debugging

from LinkedList import Linked_List
from PokemonArray import Pokemon_Array

# 🟧 in progress
class Backend:
    # 🟧 in progress
    def __init__(self, frontend_instance) -> None:
        self.frontend = frontend_instance
        self.player1_pokemons: Linked_List = Linked_List()
        self.player2_pokemons: Linked_List = Linked_List()
        self.pokemon_array: Pokemon_Array = Pokemon_Array()

    # 🟧 in progress | note: Linked list in progress
    def select_pokemon_list(self) -> None:
        index: int = 0
        while index < 2:
            self.pokemon_array.show_pokemons()
            try:
                player: str = "Player 1" if index == 0 else "Player 2"
                player_pokemons: Linked_List = self.player1_pokemons if index == 0 else self.player2_pokemons

                choices: list = list(map(int, input(f"{player}, select 3 Pokémon by entering their indices (space-separated): ").split()))

                if len(choices) != 3:
                    self.frontend.show_error_message("Backend: You must select exactly 3 Pokémon!")
                    continue

                if all(1 <= choice <= self.pokemon_array.size() for choice in choices):
                    for choice in choices:
                        player_pokemons.insert_at_end(self.pokemon_array.select_pokemon(choice))
                    self.pokemon_array.remove_pokemon(choices)
                    index += 1
                else:
                    self.frontend.show_error_message("Backend: One or more indices are invalid. Please try again.")

            except (ValueError, IndexError):
                self.frontend.show_error_message("Backend: Please enter valid numeric indices separated by spaces.")
            
    def show_selected_pokemons(self) -> None:
        self.player1_pokemons.print_linked_list()
        self.player2_pokemons.print_linked_list()

# 🐞Debugging
if __name__ == "__main__":
    backend = Backend()
    print("Pick your pokemon.\n")

    backend.select_pokemon_list(backend.player1_pokemons, "Player 1")
    print(backend.pokemon_array.show_pokemons()) #backend.pokemon_array
