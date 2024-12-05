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
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # ✅ working
    def show_error_message(self, message: str) -> None:
        error_message = Text(message, style="red")
        self.console.print(error_message)
        time.sleep(1.5)
    
    # ✅ working
    # shows selected pokemon when selecting
    def show_selected_pokemon(self, pokemon: list) -> None:
        self.console.print(Align.center(f"Selected Pokemon: [green]{pokemon[0][0]}, {pokemon[1][0]}, {pokemon[2][0]}[/green]"), style="white")
        time.sleep(2)
        
    # ✅ Working
    def wait_for_start(self) -> None:
        user_input = input().strip().lower()

        if user_input == 'q':
            self.console.print("[bold red]Game exited. Goodbye![/bold red]", style="white")
            sys.exit()  # Quit the program
        else:
            self.console.print("[bold green]Game starting...[/bold green]", style="white")
    
    #✅ Working
    def print_panel(self, message, title, style, width_fraction=2):
            # Helper function to create and print a styled panel
            console_width = self.console.size.width // width_fraction
            aligned_message = Align.center(message)
            panel = Panel(
                aligned_message,
                title=title,
                style=style,
                border_style=style,
                width=console_width,
                padding=(1, 1)
            )
            self.console.print(panel, justify="left")
     
    #✅ Working
    def program_intro(self) -> None:
        self.clear_screen()

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
        self.console.print(Align.center("[yellow]🛈[/yellow]: [bold yellow]✨Choose your Pokemon✨:[/bold yellow] [green]3 each player![/green]\n[yellow]🛈[/yellow]: Choose your pokemon [bold yellow]queue order![/bold yellow]", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: 🧙 exchange luck with a [purple]random effect![/purple] [bold green]💚 potion[/bold green] or [bold red]💔 poison[/bold red].\n[yellow]🛈[/yellow]:[italic]After every battle, ⚔️ pokemon lose [bold red]-5 Health💔[/bold red] due to [red]fatigue[/red][/italic].", vertical="middle"), style="white")
        
        # Print final panel to prompt user to start or quit
        self.console.print(
            Panel(
                Align.center("[bold green]PRESS ENTER TO START[/bold green]", vertical="middle"),
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
        self.clear_screen()

        self.console.print(Align.center("\n[green]Choose [bold]3 pokemons![/bold][/green]", vertical="middle"), style="white")
        self.console.print(Align.center("Selected pokemons will be [red]removed from the pokemon list![/red]\n", vertical="middle"), style="white")
        

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
        self.console.print(Align.center(table))
    
    # ✅ working
    def display_player_pokemons(self, player_linked_list, player_str: int) -> None:
        self.clear_screen()
        
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

    # ✅ working
    def display_players_pokemon_queue(self, player1_queue: list, player2_queue: list) -> None:
        self.clear_screen()
        # Get console width
        total_width = self.console.size.width

        # Calculate individual section widths
        left_width = (7 * total_width) // 16
        middle_width = total_width // 8
        right_width = (7 * total_width) // 16

        # Take elements from the queues for each row
        row1_left = player1_queue[0][0] if player1_queue else "Player 1 Pokemon Queue #1"
        row1_right = player2_queue[0][0] if player2_queue else "Player 2 Pokemon Queue #1"

        row2_left = player1_queue[1][0] if player1_queue else "Player 1 Pokemon Queue #2"
        row2_right = player2_queue[1][0] if player2_queue else "Player 2 Pokemon Queue #2"

        row3_left = player1_queue[2][0] if player1_queue else "Player 1 Pokemon Queue #3"
        row3_right = player2_queue[2][0] if player2_queue else "Player 2 Pokemon Queue #3"

        # Create aligned messages for each panel in all rows
        left_aligned_message1 = Align.center(row1_left)
        middle_aligned_message1 = Align.center("VS")
        right_aligned_message1 = Align.center(row1_right)

        left_aligned_message2 = Align.center(row2_left)
        middle_aligned_message2 = Align.center("VS")
        right_aligned_message2 = Align.center(row2_right)

        left_aligned_message3 = Align.center(row3_left)
        middle_aligned_message3 = Align.center("VS")
        right_aligned_message3 = Align.center(row3_right)

        # Create panels for all three rows
        panel1_left = Panel(
            left_aligned_message1,
            title="Player 1",
            style="green",
            border_style="green",
            width=left_width,
            padding=(1, 1),
            box=HEAVY,
        )
        panel1_middle = Panel(
            middle_aligned_message1,
            style="yellow",
            border_style="yellow",
            width=middle_width,
            padding=(1, 1),
            box=HEAVY,
        )
        panel1_right = Panel(
            right_aligned_message1,
            title="Player 2",
            style="red",
            border_style="red",
            width=right_width,
            padding=(1, 1),
            box=HEAVY,
        )

        panel2_left = Panel(
            left_aligned_message2,
            title="Player 1",
            style="yellow",
            border_style="yellow",
            width=left_width,
            padding=(1, 1),
            box=HEAVY,
        )
        panel2_middle = Panel(
            middle_aligned_message2,
            style="yellow",
            border_style="yellow",
            width=middle_width,
            padding=(1, 1),
            box=HEAVY,
        )
        panel2_right = Panel(
            right_aligned_message2,
            title="Player 2",
            style="green",
            border_style="green",
            width=right_width,
            padding=(1, 1),
            box=HEAVY,
        )

        panel3_left = Panel(
            left_aligned_message3,
            title="Player 1",
            style="red",
            border_style="red",
            width=left_width,
            padding=(1, 1),
            box=HEAVY,
        )
        panel3_middle = Panel(
            middle_aligned_message3,
            style="yellow",
            border_style="yellow",
            width=middle_width,
            padding=(1, 1),
            box=HEAVY,
        )
        panel3_right = Panel(
            right_aligned_message3,
            title="Player 2",
            style="blue",
            border_style="blue",
            width=right_width,
            padding=(1, 1),
            box=HEAVY,
        )

        # Create a table to align the panels side by side for all rows
        table = Table.grid(padding=1)
        table.add_column(justify="center", width=left_width)
        table.add_column(justify="center", width=middle_width)
        table.add_column(justify="center", width=right_width)
        
        # Add rows to the table
        table.add_row(panel1_left, panel1_middle, panel1_right)
        table.add_row(panel2_left, panel2_middle, panel2_right)
        table.add_row(panel3_left, panel3_middle, panel3_right)
        
        self.console.print(Panel(Align.center("[bold blue]Pokemon Battle Queue[/bold blue]",
            vertical="middle"), style="white", border_style="blue", box=HEAVY, padding=(1, 1)))

        # Print the table with all three rows
        self.console.print(table)
        self.console.input(Panel(Align.center("[bold green]PRESS ENTER TO CONTINUE To BATTLE[/bold green]", vertical="middle"), style="white", border_style="yellow", box=HEAVY))
    
    # 🟧 in progress
    def random_effects_display(self, player_name: str, pokemon_name: str) -> None:
        self.clear_screen()
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
        try:
            self.clear_screen()
            with self.console.status("[bold green]Processing...", spinner=spinner_type) as status:
                sleep(seconds)
        except Exception as e:
            self.console.print(f"[red]Error in spinner animation: {e}[/red]")

    # ✅ working
    def progress_bar_animation(self, seconds: int):
        try:
            self.clear_screen()
            total_steps = 100
            step_duration = seconds / total_steps

            with Progress(
                TextColumn("[bold blue]Battle ready:[/bold blue]"),
                BarColumn(bar_width=60),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            ) as progress:
                task = progress.add_task("Battle ready...", total=total_steps)

                for _ in range(total_steps):
                    sleep(step_duration)
                    progress.update(task, advance=1)
        except Exception as e:
            self.console.print(f"[red]Error in progress bar animation: {e}[/red]")

    # ✅ working
    def prompt_player_selection(self, player: str) -> str:
        self.console.print(Align.center(f"[bold yellow]✨ {player} ✨[/bold yellow]", vertical="middle"), style="white")

        self.console.print(
            Panel(
                Align.center("[cyan]Enter 3 Pokémon by entering their indices (space-separated):[/cyan]", vertical="middle"),
                style="white",
                border_style="yellow",
                box=HEAVY
            )
        )

        return input("> ").strip()

# ================================================================================
#                               Backend Core Method Calls
# ================================================================================
        
    # ✅ working
    def pokemon_selection(self) -> None:
        self.backend.select_pokemon_list()
    
    # ✅ working
    def pokemon_queue_selection(self) -> None:
        self.backend.select_pokemon_queue()
        
    def pokemon_rand_effects_selection(self) -> None:
        self.backend.random_effects_selection()
        
if __name__ == "__main__":
    import main
    main.Gameplay()