from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.box import HEAVY
from collections import deque

class BattlePanel:
    def __init__(self):
        self.console = Console()

    def pokemon_battle_panel(self, player1_queue, player2_queue):
        # Get console width
        total_width = self.console.size.width

        # Calculate individual section widths
        left_width = (7 * total_width) // 16
        middle_width = total_width // 8
        right_width = (7 * total_width) // 16

        # Take elements from the queues for each row
        row1_left = player1_queue.popleft() if player1_queue else "Player 1 Pokemon Queue #1"
        row1_right = player2_queue.popleft() if player2_queue else "Player 2 Pokemon Queue #1"

        row2_left = player1_queue.popleft() if player1_queue else "Player 1 Pokemon Queue #2"
        row2_right = player2_queue.popleft() if player2_queue else "Player 2 Pokemon Queue #2"

        row3_left = player1_queue.popleft() if player1_queue else "Player 1 Pokemon Queue #3"
        row3_right = player2_queue.popleft() if player2_queue else "Player 2 Pokemon Queue #3"

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
            title="Battle",
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
            title="Left Pokémon",
            style="yellow",
            border_style="yellow",
            width=left_width,
            padding=(1, 1),
            box=HEAVY,
        )
        panel2_middle = Panel(
            middle_aligned_message2,
            title="Battle",
            style="yellow",
            border_style="yellow",
            width=middle_width,
            padding=(1, 1),
            box=HEAVY,
        )
        panel2_right = Panel(
            right_aligned_message2,
            title="Right Pokémon",
            style="green",
            border_style="green",
            width=right_width,
            padding=(1, 1),
            box=HEAVY,
        )

        panel3_left = Panel(
            left_aligned_message3,
            title="Left Pokémon",
            style="red",
            border_style="red",
            width=left_width,
            padding=(1, 1),
            box=HEAVY,
        )
        panel3_middle = Panel(
            middle_aligned_message3,
            title="Battle",
            style="yellow",
            border_style="yellow",
            width=middle_width,
            padding=(1, 1),
            box=HEAVY,
        )
        panel3_right = Panel(
            right_aligned_message3,
            title="Right Pokémon",
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

        # Print the table with all three rows
        self.console.print(table)

# Example usage
if __name__ == "__main__":
    # Create queues for Player 1 and Player 2
    player1_queue = deque([]) # "Player 1 Stats", "Pikachu", "Charmander"
    player2_queue = deque([]) # "Player 2 Stats", "Bulbasaur", "Squirtle"

    panel = BattlePanel()
    panel.print_three_panel_from_queue(player1_queue, player2_queue)
