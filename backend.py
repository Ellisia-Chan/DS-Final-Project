# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 🐞Debugging

from Data_Struc.LinkedList import Linked_List
from Data_Struc.Queue import Queue
from Data_Struc.stack import Stack
from Data_Struc.PokemonArray import Pokemon_Array

import random
# 🟧 in progress
class Backend:
    # 🟧 in progress
    def __init__(self, frontend_instance) -> None:
        self.frontend = frontend_instance
        
        # Player 1
        self.player1_pokemons: Linked_List = Linked_List()
        self.player1_pokemon_queue: Queue = Queue()
        self.player1_pokemon_stack: Stack = Stack()
        
        self.player1_current_battle_pokemon: list = []
        self.player1_temporary_power: list = []
        
        # Player 2
        self.player2_pokemons: Linked_List = Linked_List()
        self.player2_pokemon_queue: Queue = Queue()
        self.player2_pokemon_stack: Stack = Stack()
        
        self.player2_current_battle_pokemon: list = []
        
        # Pokemon Array
        self.pokemon_array: Pokemon_Array = Pokemon_Array()
        
    # ✅ working
    # This method allows the user to select 3 pokemons from the pokemon array
    # and adds them to the player's pokemon linked list. The pokemon is then removed
    # from the pokemon array. This is done for both player 1 and player 2.
    def select_pokemon_list(self) -> None:
        index: int = 0
        while index < 2:
            self.frontend.display_pokemon_array()  # Display available Pokémon
            try:
                # Determine the current player
                player_str: str = "Player 1" if index == 0 else "Player 2"
                player_pokemons: Linked_List = self.player1_pokemons if index == 0 else self.player2_pokemons

                # Get input from the user
                choices_raw = self.frontend.prompt_player_selection(player_str)
                choices: list = list(map(int, choices_raw.split()))

                # Validate selection length
                if len(choices) != 3:
                    self.frontend.show_error_message("You must select exactly 3 Pokémon!")
                    continue

                # Check for duplicate choices
                if len(set(choices)) != len(choices):
                    self.frontend.show_error_message("Duplicate Pokémon selections are not allowed.")
                    continue

                # Validate indices and add selected Pokémon to the player's list
                if all(1 <= choice <= self.pokemon_array.size() for choice in choices):
                    for choice in choices:
                        player_pokemons.insert_at_end(self.pokemon_array.select_pokemon(choice))
                    self.pokemon_array.remove_pokemon(choices)
                    index += 1
                else:
                    self.frontend.show_error_message("One or more indices are invalid. Please try again.")

                # Display selected Pokémon
                self.frontend.show_selected_pokemon(player_pokemons.get_linked_list())

            except (ValueError, IndexError):
                self.frontend.show_error_message("Please enter valid numeric indices separated by spaces.")
    
    # ✅ working
    def select_pokemon_queue(self) -> None:
        
        index: int = 0
        while index < 2:
            try:
                # Determine the current player's data
                player_str: str = "Player 1" if index == 0 else "Player 2"
                player_pokemons: Linked_List = self.player1_pokemons if index == 0 else self.player2_pokemons
                player_queue: Queue = self.player1_pokemon_queue if index == 0 else self.player2_pokemon_queue

                # Display the available Pokémon for the current player
                self.frontend.display_player_pokemon_queue_table(player_pokemons.get_linked_list(), player_str, player_queue.get_queue())

                # Prompt player to make their selections
                choices_raw = self.frontend.prompt_player_queue_selection()
                queue_choice: list = list(map(int, choices_raw.split()))

                # Validate the input: ensure exactly 3 Pokémon are selected
                if len(queue_choice) != 3:
                    self.frontend.show_error_message("You must select exactly 3 Pokémon for queue")
                    continue

                # Check for duplicate selections
                if len(set(queue_choice)) != len(queue_choice):
                    self.frontend.show_error_message("Duplicate Pokémon selections are not allowed.")
                    continue

                # Check that all chosen indices are valid
                if all(1 <= choice <= player_pokemons.size() for choice in queue_choice):
                    for choice in queue_choice:
                        # Add the selected Pokémon to the player's queue
                        player_queue.enqueue(player_pokemons.get_node(choice))
                    index += 1
                else:
                    self.frontend.show_error_message("One or more indices are invalid. Please try again.")
                    continue

                # Update the frontend with the selected Pokémon
                self.frontend.display_player_pokemon_queue_table(player_pokemons.get_linked_list(), player_str, player_queue.get_queue())
                self.frontend.wait_for_timer(2)
                
            except (ValueError, IndexError):
                # Handle invalid input gracefully
                self.frontend.show_error_message("Please enter valid numeric indices separated by spaces.")

    # 🟧 in progress
    def random_effects_selection(self) -> None:
        index: int = 0
        while index < 2:
            try:
                player_str: str = "Player 1" if index == 0 else "Player 2"
                player_queue: Queue = self.player1_pokemon_queue if index == 0 else self.player2_pokemon_queue
                player_stack: Stack = self.player1_pokemon_stack if index == 0 else self.player2_pokemon_stack
                
                self.frontend.random_effects_display(player_str, player_queue.front())
                self.random_effect_generator(player_stack)
                self.frontend.display_pokemon_stack_effect(player_str, player_queue.front(), player_stack.get())
                
                index += 1
                            
            except (ValueError, IndexError):
                self.frontend.show_error_message("Please enter valid numeric indices separated by spaces.")
                
    # ✅ working
    def random_effect_generator(self, player_stack: Stack) -> None:
        effects_list: list = ["Power UP", "Poison"]
        for _ in range(3):
            effect: str = random.choice(effects_list)
            player_stack.push(effect)
    
    def random_effectiveness_generator(self) -> float:
        effect_perc: list = [0.30, 0.20, 0.10]
        return random.choice(effect_perc)
    
    def battle_calculation(self) -> None:
        self.frontend.display_battle_start("white", "white", self.player1_pokemon_queue.front(), self.player2_pokemon_queue.front(), 0)
        
        self.player1_current_battle_pokemon.append(self.player1_pokemon_queue.dequeue())
        self.player2_current_battle_pokemon.append(self.player2_pokemon_queue.dequeue())
        
        print(self.pokemon_array.is_element_countered(self.player1_current_battle_pokemon[0][1], self.player2_current_battle_pokemon[0][1]))
        print(self.pokemon_array.is_element_countered(self.player2_current_battle_pokemon[0][1], self.player1_current_battle_pokemon[0][1]))

# 🐞Debugging
if __name__ == "__main__":
    import main
    main.Gameplay()
