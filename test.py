from rich.box import HEAVY

from rich.panel import Panel
from rich.table import Table
from rich.align import Align
import os
from rich.console import Console

class Frontend:
    # 🟧 in progress
    def __init__(self) -> None:
        self.console = Console()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

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
                title="Q1",
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
                title="Q1",
                style="green",
                border_style="green",
                width=right_width,
                padding=(1, 1),
                box=HEAVY,
            )

            panel2_left = Panel(
                left_aligned_message2,
                title="Q2",
                style="red",
                border_style="red",
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
                title="Q2",
                style="red",
                border_style="red",
                width=right_width,
                padding=(1, 1),
                box=HEAVY,
            )

            panel3_left = Panel(
                left_aligned_message3,
                title="Q3",
                style="blue",
                border_style="blue",
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
                title="Q3",
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
            
            self.console.print(Panel(Align.center("[bold white]Pokemon Battle Queue![/bold white]",
                vertical="middle"), style="yellow", border_style="yellow", box=HEAVY, padding=(1, 1)))

            # Print the table with all three rows
            self.console.print(table)
            self.console.input(Panel(Align.center("[bold white]PRESS ENTER TO CONTINUE To BATTLE[/bold white]", vertical="middle"), style="yellow", border_style="yellow", box=HEAVY))
        

if __name__ == "__main__":
     f = Frontend()
     f.display_players_pokemon_queue([],[])