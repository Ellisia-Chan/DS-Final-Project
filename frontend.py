# 🟧 in progress
# ✅ working
# ⚠️ Untested

from backend import Backend


class Frontend:
    def __init__(self) -> None:
        self.backend = Backend(self)

    def program_intro(self) -> None:
        print("Welcome to the Pokemon Battle Game! \n")
        
    def pokemon_selection(self) -> None:
        self.backend.pokemon_array.show_pokemons()
        self.backend.select_pokemon_list()
        self.backend.show_selected_pokemons()
        
    def show_error_message(self, message: str) -> None:
        print(message)