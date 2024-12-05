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
        
        # ✅ working
        # player pokemon array selection loop
        self.frontend.pokemon_selection()
<<<<<<< Updated upstream
        
        # player pokemon queue for battle
        self.frontend.pokemon_queue_selection()
=======

        self.frontend.spinner_animation(3, spinner_type="aesthetic")

        # ✅ working
        # player pokemon queue for battle
        self.frontend.pokemon_queue_selection()
        
        self.frontend.spinner_animation(3, spinner_type="aesthetic")


        # 🟧 in progress
        # player selection for blessings (power-ups/poison)
        self.frontend.pokemon_rand_effects_selection()
>>>>>>> Stashed changes

        self.frontend.progress_bar_animation(5)

if __name__ == "__main__":
    Gameplay()