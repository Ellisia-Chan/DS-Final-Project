# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 💬 may message ako

from backend import Backend

import sys, os, time
from time import sleep

from rich.box import HEAVY
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn


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
     
    #✅ Working
    def program_intro(self) -> None:
        os.system('cls')

        # Function to read ASCII art from a file
        def draw_ascii(file_name):
            try:
                # Open the file with UTF-8 encoding
                with open(file_name + ".txt", "r", encoding="utf-8") as file:
                    return file.read()  # Return the content of the file
            except FileNotFoundError:
                return "[red]Error: ASCII art file not found.[/red]"
            except UnicodeDecodeError:
                return "[red]Error: Unable to decode ASCII art file.[/red]"


        # Pokemon title ASCII art
        ascii_art = draw_ascii("pokemon_title")  # Fetch ASCII content from file

        # Print the panel with centered alignment for ASCII art
        self.console.print(
            Panel(
                Align.center(f"[blue]{ascii_art}[/blue]", vertical="middle"),
                style="white",
                border_style="blue",
                box=HEAVY
            )
        )

        # Additional Information and Messages
        self.console.print(Align.center("[yellow]🛈[/yellow]: [bold yellow]✨Choose your Pokemon✨:[/bold yellow] [green]3 each player![/green]\n", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: Choose your pokemon [bold yellow]queue order![/bold yellow]", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: 🧙 exchange luck with a [purple]random effect![/purple] [bold green]💚 potion[/bold green] or [bold red]💔 poison[/bold red].", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: [italic]After every battle, ⚔️ pokemon lose [bold red]-5 Health💔[/bold red] due to [red]fatigue[/red][/italic].", vertical="middle"), style="white")
        
        # Print final panel to prompt user to start or quit
        self.console.print(
            Panel(
                Align.center("[bold green]PRESS ENTER TO START[/bold green] or [bold red]type 'q' to quit[/bold red]", vertical="middle"),
                style="white",
                border_style="yellow",
                box=HEAVY
            )
        )

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

    
    # 🟧 in progress
    def random_effects_display(self, player_name: str, pokemon_name: str) -> None:
        os.system('cls')
        message: str = f"[bold white]\t\t  {player_name} Pokemon Random Effect stack[/bold white]\n{pokemon_name[0]} will receive a 3 random effect stack (Power-ups or Poisons)\n\n[red]Press enter to generate stack[/red]"
        
        self.print_panel(message, "Random Effects", "yellow")
    
    # 🟧 in progress  
    def display_pokemon_stack_effect(self, player_str: str, pokemon_name: str, pokemon_effect_stack: list) -> None:
        table = Table(border_style="bold white", box=HEAVY, title=f"{player_str} {pokemon_name[0]} Effect Stack")
        
        table.add_column("Index", justify="center", width=8)
        table.add_column("Effects", justify="center", width=20)
        
        for idx, effect in enumerate(reversed(pokemon_effect_stack)):
            table.add_row(
                str(idx+1),  # Index
                str(effect),  # Effect
            )
            
        self.console.print(Align.left(table))

    # ✅ working
    def spinner_animation(self, seconds: int, spinner_type: str = "dots"):
        os.system('cls')
        with self.console.status("[bold green]Processing...", spinner=spinner_type) as status:
            sleep(seconds)

    # ✅ working
    def progress_bar_animation(self, seconds: int):
        os.system('cls')
        total_steps = 100
        step_duration = seconds / total_steps  # Calculate time per step

        with Progress(
            TextColumn("[bold blue]Progress:[/bold blue]"),
            BarColumn(bar_width=60),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            task = progress.add_task("Battle ready...", total=total_steps)

            for _ in range(total_steps):
                sleep(step_duration)  # Simulate work
                progress.update(task, advance=1)  # Update progress bar


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