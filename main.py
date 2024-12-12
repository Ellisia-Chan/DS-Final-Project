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
        
        # ✅ working
        # player pokemon array selection loop
        self.frontend.pokemon_selection()

        # ✅ working
        # player selection for random effects(power-ups/poison)
        self.frontend.pokemon_effects_selection()
        
        # ✅ working
        self.frontend.pokemon_queue_battle_start()
        
        # ✅ working
        self.frontend.pokemon_battle_summary()


if __name__ == "__main__":
    Gameplay()