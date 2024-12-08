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
        # ✅ working
        # Intro animation and display
        self.frontend.program_intro()
        self.frontend.spinner_animation(2, spinner_type="aesthetic", message="Processing...")
        
        # ✅ working
        # player pokemon array selection loop
        self.frontend.pokemon_selection()
        self.frontend.progress_bar_animation(2)

        # ✅ working
        # Show the blank pokemons queue table for queue selection
        self.frontend.display_players_blank_pokemon_queue("white", "white")

        # ✅ working
        # player pokemon queue selection for battle order
        self.frontend.pokemon_queue_selection()
        self.frontend.spinner_animation(2, spinner_type="aesthetic", message="Processing Queue...")

        # 🟧 in progress
        # player selection for random effects(power-ups/poison)
        self.frontend.pokemon_rand_effects_selection()
        self.frontend.spinner_animation(2, spinner_type="aesthetic", message="Preparing battle...")

        # 🟧 in progress
        # battle start
        self.frontend.pokemon_queue_battle_start()

if __name__ == "__main__":
    Gameplay()