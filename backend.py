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
        
        # Battle Variables
        self.battle_round: int = 0
        self.pokemon_items: list = ["Power Up", "Poison"]
        
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
                player_queue: Queue = self.player1_pokemon_queue if index == 0 else self.player2_pokemon_queue

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
                    continue

                queued_linked_list = player_pokemons.get_linked_list()
                for pokemon in queued_linked_list:
                    player_queue.enqueue(pokemon)
                    
                # Display selected Pokémon    
                self.frontend.show_selected_pokemon(player_pokemons.get_linked_list())

            except (ValueError, IndexError):
                self.frontend.show_error_message("Please enter valid numeric indices separated by spaces.")
                continue
                
    # 🟧 in progress
    def effects_selection(self) -> None:
        index: int = 0
        while index < 2:
            try:
                player_str: str = "Player 1" if index == 0 else "Player 2"
                player_queue: Queue = self.player1_pokemon_queue if index == 0 else self.player2_pokemon_queue
                player_stack: Stack = self.player1_pokemon_stack if index == 0 else self.player2_pokemon_stack
                
                self.frontend.display_pokemon_item_table(player_queue.get_queue(), player_str, player_stack.get())
                
                choices_raw = self.frontend.prompt_player_item_selection()
                choices: list = list(map(int, choices_raw.split()))
                
                # Validate selection length
                if len(choices) != 3:
                    self.frontend.show_error_message("You must select exactly 3 items designated to 3 pokemons!")
                    continue
                
                # Validate indices and add selected Pokémon to the player's list
                if all(choice in {1, 2} for choice in choices):
                    for choice in reversed(choices):
                        if choice == 1:
                            player_stack.push("Power Up")
                        elif choice == 2:
                            player_stack.push("Poison")
                        else:
                            pass
                    index += 1
                else:
                    self.frontend.show_error_message("One or more indices are invalid. Please try again.")
                    continue    
                    
                self.frontend.display_pokemon_item_table(player_queue.get_queue(), player_str, player_stack.get_reverse())
                input("> Press Enter to Continue")
            except (ValueError, IndexError):
                self.frontend.show_error_message("Please enter valid numeric indices separated by spaces.")
                continue
    
    # 🟧 in progress
    def battle_queue_start(self) -> None:
        while self.battle_round < 2:
            try:
                self.battle_round += 1
                
                player1_pokemon = self.player1_pokemon_queue.dequeue()
                player1_item_effect  = self.player1_pokemon_stack.pop()
                player2_pokemon= self.player2_pokemon_queue.dequeue()
                player2_item_effect = self.player2_pokemon_stack.pop()
                
                player1_base_power = player1_pokemon[3]
                player2_base_power = player2_pokemon[3]
                                
                player1_counter_str = self.pokemon_array.is_element_countered(player1_pokemon[1], player2_pokemon[1])
                player2_counter_str = self.pokemon_array.is_element_countered(player2_pokemon[1], player1_pokemon[1])
                
                player1_power_multiplier = self.element_counter_calc(player1_counter_str)
                player2_power_multiplier = self.element_counter_calc(player2_counter_str)
                
                # Calculate power from element counter
                if player1_counter_str == "opponent countered":
                    player1_updated_power = round(player1_base_power + (player1_base_power * player1_power_multiplier))
                elif player1_counter_str == "player countered":
                    player1_updated_power = round(player1_base_power - (player1_base_power * player1_power_multiplier))
                else:
                    player1_updated_power = player1_base_power
                
                if player2_counter_str == "opponent countered":
                    player2_updated_power = round(player2_base_power + (player2_base_power * player2_power_multiplier))
                elif player2_counter_str == "player countered":
                    player2_updated_power = round(player2_base_power - (player2_base_power * player2_power_multiplier))
                else:
                    player2_updated_power = player2_base_power
                
                self.frontend.display_battle_start("yellow", "white", player1_pokemon, player2_pokemon, self.battle_round)
                self.frontend.display_battle_calc("yellow", player1_pokemon, player2_pokemon, self.battle_round, player1_counter_str, player2_counter_str, player1_item_effect, player2_item_effect, player1_updated_power, player2_updated_power)
                
            except (ValueError, IndexError):
                self.frontend.show_error_message("battle queue start error")
                continue
    
    # 🟧 in progress
    def battle_winner(self, player1_power, player2_power) -> str:
        if player1_power > player2_power:
            return "Player 1"
        elif player1_power < player2_power:
            return "Player 2"
        else:
            return "Draw"
                       
    # 🟧 in progress
    def random_effectiveness_generator(self) -> float:
        effect_perc: list = [0.30, 0.20, 0.10]
        return random.choice(effect_perc)
    
    # 🟧 in progress
    def element_counter_calc(self, counter_str: str) -> float:
        if counter_str == "opponent countered":
            return 0.10
        elif counter_str == "player countered":
            return 0.15
        else:
            return 0

# 🐞Debugging
if __name__ == "__main__":
    import main
    main.Gameplay()
