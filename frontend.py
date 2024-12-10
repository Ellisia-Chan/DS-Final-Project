# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 💬 may message ako
# ❗❗❗ Warning

from backend import Backend

import sys, time
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
        
    # =============================================================
    #                      Helper Functions
    # =============================================================
    # ✅ working
    def clear_screen(self):
        print("\033c", end="")

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
        
    def wait_for_timer(self, seconds: float) -> None:
        time.sleep(seconds)
    
    #✅ Working
    def print_panel(self, message, title, style, width_fraction=2, panel_align="left"):
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
            self.console.print(panel, justify = panel_align)
    
    #✅ Working
    # Function to read ASCII art from a file
    def draw_ascii(self, file_name):
        try:
            # Open the file with UTF-8 encoding
            with open(file_name + ".txt", "r", encoding="utf-8") as file:
                return file.read()  # Return the content of the file
        except FileNotFoundError:
            return "[red]Error: ASCII art file not found.[/red]"
        except UnicodeDecodeError:
            return "[red]Error: Unable to decode ASCII art file.[/red]"
    
    # ✅ working
    def spinner_animation(self, seconds: float, spinner_type: str = "dots", message: str = ""):
        try:
            self.clear_screen()
            with self.console.status(f"[bold green]{message}", spinner=spinner_type) as status:
                sleep(seconds)
        except Exception as e:
            self.console.print(f"[red]Error in spinner animation: {e}[/red]")

    # ✅ working
    def progress_bar_animation(self, seconds: float):
        try:
            self.clear_screen()
            total_steps = 100
            step_duration = seconds / total_steps

            with Progress(
                TextColumn("[bold blue]Preparing battle:[/bold blue]"),
                BarColumn(bar_width=60),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            ) as progress:
                task = progress.add_task("Battle ready...", total=total_steps)

                for _ in range(total_steps):
                    sleep(step_duration)
                    progress.update(task, advance=1)
        except Exception as e:
            self.console.print(f"[red]Error in progress bar animation: {e}[/red]")

# ======================================================================================
#                            Frontend Program Flow Methods
# ======================================================================================   
    #✅ Working
    def program_intro(self) -> None:
        self.clear_screen()

        # Pokemon title ASCII art
        ascii_art = self.draw_ascii("pokemon_title")  # Fetch ASCII content from file

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
        self.console.print(Align.center("[yellow]🛈[/yellow]: [bold yellow]✨ Choose your Pokemon ✨:[/bold yellow] [green]3 each player![/green]\n[yellow]🛈[/yellow]: Choose your pokemon [bold yellow]queue order![/bold yellow]", vertical="middle"), style="white")
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
        print()
            
    # ✅ working
    def display_pokemon_item_table(self, player_queue: list, player_str: str, player_stack: list) -> None:
        self.clear_screen()

        # Get console width
        total_width = self.console.size.width

        # Calculate individual section widths
        left_width = (7 * total_width) // 16
        middle_width = total_width // 8
        right_width = (7 * total_width) // 16

        # Take elements from the queues for each row
        row1_left = player_queue[0][0] if player_queue else "?"
        row1_right = player_stack[0][0] if player_stack else "?"

        row2_left = player_queue[1][0] if player_queue else "?"
        row2_right = player_stack[1][0] if player_stack else "?"

        row3_left = player_queue[2][0] if player_queue else "?"
        row3_right = player_stack[2][0] if player_stack else "?"

        # Create aligned messages for each panel in all rows
        left_aligned_message1 = Align.center(row1_left)
        middle_aligned_message1 = Align.center("→")
        right_aligned_message1 = Align.center(row1_right)

        left_aligned_message2 = Align.center(row2_left)
        middle_aligned_message2 = Align.center("→")
        right_aligned_message2 = Align.center(row2_right)

        left_aligned_message3 = Align.center(row3_left)
        middle_aligned_message3 = Align.center("→")
        right_aligned_message3 = Align.center(row3_right)

        # Create panels for all three rows
        panel1_left = Panel(
            left_aligned_message1,
            title="1",
            style="white",
            width=left_width,
            padding=(1, 1),
            box=HEAVY

        )
        panel1_middle = Panel(
            middle_aligned_message1,
            style="white",
            border_style="white",
            width=middle_width,
            padding=(1, 1),
            box=HEAVY
        )
        panel1_right = Panel(
            right_aligned_message1,
            title="Queue 1",
            style="green",
            border_style="green",
            width=right_width,
            padding=(1, 1),
            box=HEAVY,
        )

        panel2_left = Panel(
            left_aligned_message2,
            title="2",
            style="white",
            width=left_width,
            padding=(1, 1),
            box=HEAVY
        )
        panel2_middle = Panel(
            middle_aligned_message2,
            style='white',
            width=middle_width,
            padding=(1, 1),
            box=HEAVY
        )
        panel2_right = Panel(
            right_aligned_message2,
            title="Queue 2",
            style="red",
            border_style="red",
            width=right_width,
            padding=(1, 1),
            box=HEAVY,
        )

        panel3_left = Panel(
            left_aligned_message3,
            title="3",
            style="white",
            width=left_width,
            padding=(1, 1),
            box=HEAVY
        )
        panel3_middle = Panel(
            middle_aligned_message3,
            style='white',
            width=middle_width,
            padding=(1, 1),
            box=HEAVY
        )
        panel3_right = Panel(
            right_aligned_message3,
            title="Queue 3",
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
        
        self.console.print(Panel(Align.center("[bold white]Pokemon Battle Queue Selection[/bold white]"), box=HEAVY, padding=(1, 1), style="red", border_style="red"))
        self.console.print(Panel(Align.center(f"[bold white]{player_str}[/bold white]",
                vertical="middle"), style="yellow", border_style="yellow", box=HEAVY))
        
        # Player pokemon details
        table_pokemon_atts = Table(border_style="bold white", box=HEAVY)
        # Add columns for the Pokemon attributes
        table_pokemon_atts.add_column("Name", justify="center")
        table_pokemon_atts.add_column("Type", justify="center")
        table_pokemon_atts.add_column("Health", justify="center")
        table_pokemon_atts.add_column("Power", justify="center")

        # Populate the table with Pokemon data from backend
        for idx, pokemon in enumerate(player_queue):
            table_pokemon_atts.add_row(
                str(pokemon[0]),  # Name
                str(pokemon[1]),  # Type
                str(pokemon[2]),  # Health
                str(pokemon[3]),  # Power
            )
        # Print the table center-aligned
        self.console.print(Align.center(table_pokemon_atts))
        print()
        
        # Print the table with all three rows
        self.console.print(table)
    
    # 🟧 in progress  
    def display_battle_start(self, style_color: str, title_color: str, player1_pokemon: list, player2_pokemon: list, battle_index: int) -> None:
            self.clear_screen()
            # Get console width
            total_width = self.console.size.width

            # Calculate individual section widths
            left_width = (7 * total_width) // 16
            middle_width = total_width // 8
            right_width = (7 * total_width) // 16

            # Take elements from the queues for each row
            row1_left, row1_right = player1_pokemon[0][0], player2_pokemon[0][0]
            
            # Create aligned messages for each panel in all rows
            left_aligned_message1 = Align.center(row1_left)
            middle_aligned_message1 = Align.center("VS")
            right_aligned_message1 = Align.center(row1_right)
            
            # Create panels for all three rows
            panel1_left = Panel(
                left_aligned_message1,
                title="Player 1",
                style="white",
                border_style="green",
                width=left_width,
                padding=(1, 1),
                box=HEAVY,
            )
            panel1_middle = Panel(
                middle_aligned_message1,
                style=style_color,
                border_style=style_color,
                width=middle_width,
                padding=(1, 1),
                box=HEAVY,
            )
            panel1_right = Panel(
                right_aligned_message1,
                title="Player 2",
                style="white",
                border_style="green",
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
            
            # Pokemon title ASCII art
            ascii_art = self.draw_ascii("pokemon_title")  # Fetch ASCII content from file

            self.console.print(Panel(Align.center(f"[{title_color}]{ascii_art}[/{title_color}]",
                vertical="middle"), style=style_color, border_style=style_color, box=HEAVY, padding=(1, 1)))
            self.print_panel(f"[bold white]Battle {battle_index}[/bold white]", "", "blue", panel_align="center",  width_fraction=1)
            # Print the table with all three rows
            self.console.print(table)
            self.console.input(Panel(Align.center("[bold white]PRESS ENTER TO BATTLE START![/bold white]", vertical="middle"), style=style_color, border_style=style_color, box=HEAVY))
        
    # ============================================================================
    #                         PLAYER SELECTION METHODS
    # ============================================================================    
    # ✅ working
    def prompt_player_selection(self, player: str) -> str:
        self.console.print(Align.center(f"[bold yellow]✨ {player} ✨[/bold yellow]", vertical="middle"), style="white")

        self.console.print(
            Panel(
                Align.center("[cyan]Enter 3 Pokémon in order for battle use by entering their indices (space-separated):[/cyan]", vertical="middle"),
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

    # 🟧 in progress
    def pokemon_effects_selection(self) -> None:
        self.backend.effects_selection()
        
        
if __name__ == "__main__":
    import main
    main.Gameplay()
    # f = Frontend()
    # f.pokemon_queue_selection()