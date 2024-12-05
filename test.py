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

    def draw_ascii(self, file_name):
        try:
            # Open the file with UTF-8 encoding
            with open(file_name + ".txt", "r", encoding="utf-8") as file:
                return file.read()  # Return the content of the file
        except FileNotFoundError:
            return "[red]Error: ASCII art file not found.[/red]"
        except UnicodeDecodeError:
            return "[red]Error: Unable to decode ASCII art file.[/red]"

         
            
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')



    def display_players_pokemon_queue(self, player1_queue: list, player2_queue: list, style_color, title_color) -> None:
            self.clear_screen()
            # Get console width
            total_width = self.console.size.width

            # Calculate individual section widths
            left_width = (7 * total_width) // 16
            middle_width = total_width // 8
            right_width = (7 * total_width) // 16

            # Take elements from the queues for each row
            row1_left = player1_queue[0][0] if player1_queue else "?"
            row1_right = player2_queue[0][0] if player2_queue else "?"

            row2_left = player1_queue[1][0] if player1_queue else "?"
            row2_right = player2_queue[1][0] if player2_queue else "?"

            row3_left = player1_queue[2][0] if player1_queue else "?"
            row3_right = player2_queue[2][0] if player2_queue else "?"

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
                style=style_color,
                border_style=style_color,
                width=middle_width,
                padding=(1, 1),
                box=HEAVY,
            )
            panel1_right = Panel(
                right_aligned_message1,
                title="Player 2",
                style="green",
                border_style="green",
                width=right_width,
                padding=(1, 1),
                box=HEAVY,
            )

            panel2_left = Panel(
                left_aligned_message2,
                style="red",
                border_style="red",
                width=left_width,
                padding=(1, 1),
                box=HEAVY,
            )
            panel2_middle = Panel(
                middle_aligned_message2,
                style=style_color,
                border_style=style_color,
                width=middle_width,
                padding=(1, 1),
                box=HEAVY,
            )
            panel2_right = Panel(
                right_aligned_message2,
                style="red",
                border_style="red",
                width=right_width,
                padding=(1, 1),
                box=HEAVY,
            )

            panel3_left = Panel(
                left_aligned_message3,
                style="blue",
                border_style="blue",
                width=left_width,
                padding=(1, 1),
                box=HEAVY,
            )
            panel3_middle = Panel(
                middle_aligned_message3,
                style=style_color,
                border_style=style_color,
                width=middle_width,
                padding=(1, 1),
                box=HEAVY,
            )
            panel3_right = Panel(
                right_aligned_message3,
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
            

            # Pokemon title ASCII art
            ascii_art = self.draw_ascii("pokemon_title")  # Fetch ASCII content from file

            self.console.print(Panel(Align.center(f"[{title_color}]{ascii_art}[/{title_color}]",
                vertical="middle"), style=style_color, border_style=style_color, box=HEAVY, padding=(1, 1)))
            
            # Print the table with all three rows
            self.console.print(table)
            self.console.input(Panel(Align.center("[bold white]PRESS ENTER TO BATTLE START![/bold white]", vertical="middle"), style=style_color, border_style=style_color, box=HEAVY))
        








    # ⚠️ Untested
    def player_queue_insert(self, player_queue: list, player_number: str):
        self.clear_screen()

        # Get console width
        total_width = self.console.size.width

        # Calculate individual section widths
        left_width = (7 * total_width) // 16
        middle_width = total_width // 8
        right_width = (7 * total_width) // 16

        # Take elements from the queues for each row
        row1_left = player_queue[0][0] if player_queue else "?"
        row1_right = player_queue[0][0] if player_queue else "?"

        row2_left = player_queue[1][0] if player_queue else "?"
        row2_right = player_queue[1][0] if player_queue else "?"

        row3_left = player_queue[2][0] if player_queue else "?"
        row3_right = player_queue[2][0] if player_queue else "?"

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
        




        self.console.print(Panel(Align.center(f"[bold white]{player_number}[/bold white]",
                vertical="middle"), style="yellow", border_style="yellow", box=HEAVY, padding=(1, 1)))
        
        # Print the table with all three rows
        self.console.print(table)




if __name__ == "__main__":
     f = Frontend()
    #  f.display_players_pokemon_queue([],[],"white","white")
     f.player_queue_insert([["Pikachu"], ["Charizard"], ["Bulbasaur"]], "Player 2")

