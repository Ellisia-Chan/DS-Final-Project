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
        input("Press enter to continue...")
        
        # 🟧 in progress
        # player pokemon array selection loop
        self.frontend.pokemon_selection()

if __name__ == "__main__":
    Gameplay()