# 🟧 in progress
# ✅ working
# ⚠️ Untested

from backend import Backend

import sys, os, time

from rich.text import Text
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.box import HEAVY


class Frontend:
    # 🟧 in progress
    def __init__(self) -> None:
        self.backend = Backend(self)
        self.console = Console()
        
    # ✅ working
    def show_error_message(self, message: str) -> None:
        error_message = Text(message, style="red")
        self.console.print(error_message)
        time.sleep(1)
        
    # ✅ Working
    def wait_for_start(self) -> None:
        user_input = input().strip().lower()

        if user_input == 'q':
            self.console.print("[bold red]Game exited. Goodbye![/bold red]", style="white")
            sys.exit()  # Quit the program
        else:
            self.console.print("[bold green]Game starting...[/bold green]", style="white")
     
    # 🟧 in progress
    def program_intro(self) -> None:
        os.system('cls')

        message = "🏆 Winner: [green]+5 Health💚, +5 Power[/green]\n🔥 Loser: [red]-10 Health💔, +3 Power[/red]"

        # Print the panel with centered alignment
        self.console.print(Panel(Align.center("[bold blue]Pokemon Battle![/bold blue]", vertical="middle"), style="white", border_style="blue", box=HEAVY))
        self.console.print(Align.center("By: Sherwin P.Limosnero\n\n", vertical="middle"), style="white")
        

        self.console.print(Align.center("[yellow]🛈[/yellow]: After each selection, 👼 blesses your [green]pokemon[/green] with a [bold yellow]random value[/bold yellow].", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: 🧙 can exchange your [bold yellow]✨blessing✨[/bold yellow] for a [purple]random effect[/purple].", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: [purple]random effect[/purple] could be [bold green]💚 potion[/bold green] or [bold red]💔 poison[/bold red].", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: [italic]After every battle, ⚔️ pokemon lose [bold red]-2 Health💔[/bold red] due to [red]fatigue[/red][/italic].", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: To finish the battle, both players must use all their pokemons.", vertical="middle"), style="white")
        self.console.print(Align.center(message, vertical="middle"), style="white")
        
        self.console.print(Panel(Align.center("[bold green]PRESS ENTER TO START[/bold green] or [bold red]type 'q' to quit[/bold red]", vertical="middle"), style="white", border_style="yellow", box=HEAVY))
        # Wait for user input to continue or quit
        self.wait_for_start()
        
    # ✅ Working
    # This method displays the Pokemon array from the backend using a rich table.
    # It shows the available Pokemon for selection and prints the table center-aligned.
    def display_pokemon_array(self) -> None:
        os.system('cls')
        
        # Display the Pokemon array from backend using a rich table
        # Create a rich table with a heavy border
        self.console.print("\n\n\t\t[green]Choose [bold]3 pokemons![/bold][/green] \n\t   Selected pokemons will be \n\t[red]removed from the pokemon list array![/red]")
        table = Table(border_style="bold white", box=HEAVY, title="Available Pokemon")

        # Add columns for the Pokemon attributes
        table.add_column("Index", justify="center")
        table.add_column("Name", justify="center")
        table.add_column("Type", justify="center")
        table.add_column("Health", justify="center")
        table.add_column("Power", justify="center")

        # Populate the table with Pokemon data from backend
        for idx, pokemon in enumerate(self.backend.pokemon_array.get()):
            table.add_row(
                str(idx+1),  # Index
                str(pokemon[0]),  # Name
                str(pokemon[1]),  # Type
                str(pokemon[2]),  # Health
                str(pokemon[3]),  # Power
            )

        # Print the table center-aligned
        self.console.print(Align.left(table))
    
    # 🟧 in progress
    def display_player_pokemons(self, player_linked_list, player_str: int) -> None:
        os.system('cls')
        
        self.console.print("\n\n")
        table = Table(border_style="bold white", box=HEAVY, title=f"{player_str} Pokemon Queue")
        
        # Add columns for the Pokemon attributes
        table.add_column("Index", justify="center")
        table.add_column("Name", justify="center")
        table.add_column("Type", justify="center")
        table.add_column("Health", justify="center")
        table.add_column("Power", justify="center")

        # Populate the table with Pokemon data from backend
        for idx, pokemon in enumerate(player_linked_list.get_linked_list()):
            table.add_row(
                str(idx+1),  # Index
                str(pokemon[0]),  # Name
                str(pokemon[1]),  # Type
                str(pokemon[2]),  # Health
                str(pokemon[3]),  # Power
            )

        # Print the table center-aligned
        self.console.print(Align.left(table))

# ================================================================================
#                               Backend Core Method Calls
# ================================================================================
        
    # ✅ working
    def pokemon_selection(self) -> None:
        self.backend.select_pokemon_list()
    
    # 🟧 in progress
    def pokemon_queue_selection(self) -> None:
        self.backend.select_pokemon_queue()
        self.backend.show_player_queue()
        
if __name__ == "__main__":
    import main
    main.Gameplay()