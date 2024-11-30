# 🟧 in progress
# ✅ working
# ⚠️ Untested

from LinkedList import Linked_List
from PokemonArray import Pokemon_Array


# 🟧 in progress
class Backend:
    # 🟧 in progress
    def __init__(self) -> None:
        self.player1_pokemons = Linked_List()
        self.player2_pokemons = Linked_List()
        self.pokemon_array = Pokemon_Array()

    # 🟧 in progress | note: Linked list in progress
    def select_pokemon(self, player: Linked_List, player_num_str: str) -> None:
        # Display the available Pokémon
        self.pokemon_array.show_pokemons()

        try:
            # Prompt the player to select a Pokémon by its index
            player_choice = int(input(f"{player_num_str}, enter the index of the Pokémon you want to select: "))

            # Get the selected Pokémon and remove it from the array
            selected_pokemon = self.pokemon_array.select_and_remove_pokemon(player_choice)

            # Add the chosen Pokémon to the player's linked list
            if selected_pokemon:
                player.insert_at_end(selected_pokemon[0])  # Use the name of the Pokémon
                print(f"{player_num_str}'s Pokémon: ", player.print_linked_list())
            else:
                print("Invalid selection. Try again.")
 
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid index.")


if __name__ == "__main__":
    backend = Backend()
    print("Pick your pokemon.\n")

    backend.select_pokemon(backend.player1_pokemons, "Player 1")
    print( backend.pokemon_array.show_pokemons()) #backend.pokemon_array









