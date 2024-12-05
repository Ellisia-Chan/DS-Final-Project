# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 🐞Debugging

import Packages
#Packages.InitializePackages()

from frontend import Frontend

class Gameplay:
    def __init__(self) -> None:
        self.frontend = Frontend()
        
        self.run()

    # 🟧 in progress
    def run(self) -> None:
        self.frontend.program_intro()
        self.frontend.spinner_animation(3, spinner_type="aesthetic")
        
        # ✅ working
        # player pokemon array selection loop
        self.frontend.pokemon_selection()
        self.frontend.progress_bar_animation(3)

        # ✅ working
        # Show the before moving pokemons to their proper queue
        self.frontend.display_players_pokemon_queue(
            self.player1_pokemon_queue.get_queue(),
            self.player2_pokemon_queue.get_queue(),
            "white",
            "white"
        )

        # ✅ working
        # player pokemon queue for battle
        self.frontend.pokemon_queue_selection()

        # ✅ working
        # Show the before moving pokemons to their proper queue
        self.frontend.display_players_pokemon_queue(
            self.player1_pokemon_queue.get_queue(),
            self.player2_pokemon_queue.get_queue(),
            "red",
            "yellow"
        )

        self.frontend.spinner_animation(3, spinner_type="aesthetic")


        # 🟧 in progress
        # player selection for blessings (power-ups/poison)
        self.frontend.pokemon_rand_effects_selection()

        # ✅ working
        # Show the before moving pokemons to their proper queue
        self.frontend.display_players_pokemon_queue(
            self.player1_pokemon_queue.get_queue(),
            self.player2_pokemon_queue.get_queue(),
            "yellow",
            "yellow"
        )

if __name__ == "__main__":
    Gameplay()