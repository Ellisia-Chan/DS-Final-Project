import Packages
Packages.InitializePackages()


class Gameplay:
    def __init__(self) -> None:
        pass

    # 🟧 in progress
    def run(self) -> None:
        while self.backend.player1_pokemons.size_of_linked_list() < 3 and self.backend.player2_pokemons.size_of_linked_list() < 3:
            
            self.backend.select_pokemon(self.backend.player1_pokemons, "Player 1")
            self.backend.select_pokemon(self.backend.player2_pokemons, "Player 2")

if __name__ == "__main__":
    Game = Gameplay
    Game.run()