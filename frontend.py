# 🟧 in progress
# ✅ working
# ⚠️ Untested

from backend import Backend

class Frontend:
    def __init__(self) -> None:
        self.backend = Backend()

    # 🟧 in progress
    def run(self) -> None:
        while self.backend.player1_pokemons.size_of_linked_list() < 3 and self.backend.player2_pokemons.size_of_linked_list() < 3:
            
            self.backend.select_pokemon(self.backend.player1_pokemons, "Player 1")
            self.backend.select_pokemon(self.backend.player2_pokemons, "Player 2")


if __name__ == "__main__":
    frontend = Frontend()
    frontend.run()