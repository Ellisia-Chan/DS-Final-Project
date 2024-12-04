# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 💬 may message ako

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
    
    # ✅ working
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
    def display_players_pokemon_queue(self, player1_queue: list, player2_queue: list) -> None:
        os.system('cls')
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
            title="Battle 1",
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
            title="Battle 2",
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
            title="Battle 3",
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

 
# ================================================================================
#                               Backend Core Method Calls
# ================================================================================
        
    # ✅ working
    def pokemon_selection(self) -> None:
        self.backend.select_pokemon_list()
    
    # ✅ working
    def pokemon_queue_selection(self) -> None:
        self.backend.select_pokemon_queue()
        
if __name__ == "__main__":
    import main
    main.Gameplay()