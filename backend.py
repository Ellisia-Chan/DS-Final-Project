# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 🐞Debugging

from LinkedList import Linked_List
from Queue import Queue
from stack import Stack
from PokemonArray import Pokemon_Array

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
    
    # ⚠️ Untested
    # This method allows the user to select 3 pokemons from their respective pokemon linked lists
    # and adds them to the player's pokemon queue. The pokemons are added in order of selection.
    # This is done for both player 1 and player 2.
    
    def select_pokemon_queue(self) -> None:
        # Dummy start
        self.frontend.display_players_pokemon_queue(
            self.player1_pokemon_queue.get_queue(),
            self.player2_pokemon_queue.get_queue(),
            "white",
            "white")
        
        index: int = 0
        while index < 2:
            try:
                player_str: str = "Player 1" if index == 0 else "Player 2"
                player_pokemons: Linked_List = self.player1_pokemons if index == 0 else self.player2_pokemons
                player_queue: Queue = self.player1_pokemon_queue if index == 0 else self.player2_pokemon_queue
                self.frontend.display_player_pokemons(player_pokemons, player_str)
                
                self.frontend.player_queue_insert(player_queue,player_str)
                # Get input from the user
                choices_raw = self.frontend.prompt_player_selection(player_str)
                queue_choice: list = list(map(int, choices_raw.split()))

                
                if len(queue_choice) != 3:
                    self.frontend.show_error_message("You must select exactly 3 Pokémon!")
                    continue
                
                # Check for duplicate choices
                if len(set(queue_choice)) != len(queue_choice):
                    self.frontend.show_error_message("Duplicate Pokémon selections are not allowed.")
                    continue

                if all(1 <= choice <= player_pokemons.size() for choice in queue_choice):
                    for choice in queue_choice:
                        player_queue.enqueue(player_pokemons.get_node(choice))
                    index += 1
                else:
                    self.frontend.show_error_message("One or more indices are invalid. Please try again.")
                
                self.frontend.player_queue_insert(queue_choice,player_str)
                # self.frontend.show_selected_pokemon(player_queue.get_queue())
            
            except (ValueError, IndexError):
                self.frontend.show_error_message("Please enter valid numeric indices separated by spaces.")
        
        # Main battle output
        self.frontend.display_players_pokemon_queue(
            self.player1_pokemon_queue.get_queue(),
            self.player2_pokemon_queue.get_queue(),
            "white",
            "white")
    
    # 🟧 in progress
    def random_effects_selection(self) -> None:
        index: int = 0
        while index < 2:
            try:
                player_str: str = "Player 1" if index == 0 else "Player 2"
                player_queue: Queue = self.player1_pokemon_queue if index == 0 else self.player2_pokemon_queue
                player_stack: Stack = self.player1_pokemon_stack if index == 0 else self.player2_pokemon_stack
                
                self.frontend.random_effects_display(player_str, player_queue.front())
                input()
                self.random_effect_generator(player_stack)
                self.frontend.display_pokemon_stack_effect(player_str, player_queue.front(), player_stack.get())
                input()
                
                index += 1
                            
            except (ValueError, IndexError):
                self.frontend.show_error_message("Please enter valid numeric indices separated by spaces.")
                
    # ✅ working
    def random_effect_generator(self, player_stack: Stack) -> None:
        effects_list: list = ["Power UP", "Poison"]
        for _ in range(3):
            effect: str = random.choice(effects_list)
            player_stack.push(effect)
            

# 🐞Debugging
if __name__ == "__main__":
    import main
    main.Gameplay()
