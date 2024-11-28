# 🟧 in progress
# ✅ working
# ⚠️ Untested



from Backend import Backend
class Frontend:
    def __init__(self) -> None:
        self.backend = Backend()

    # 🟧 in progress
    def run(self) -> None:
        while len(self.backend.player1_pokemons) < 3 and len(self.backend.player2_pokemons) < 3:
            
            self.backend.select_pokemon(self.backend.player1_pokemons, "Player 1")
            self.backend.select_pokemon(self.backend.player2_pokemons, "Player 2")