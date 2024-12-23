# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 💬 may message ako
# ❗❗❗ Warning

from backend import Backend

import sys, time, os, platform
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
        # Detect the operating system
        os_name = platform.system()

        if os_name == "Windows":
            # Clear screen for Windows (including PowerShell)
            os.system("cls")
        else:
            # Clear screen for Unix-like systems (Linux, macOS)
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
            self.console.print("[red]Game exited. Goodbye![/red]", style="white")
            sys.exit()  # Quit the program
        else:
            self.console.print("[green]Game starting...[/green]", style="white")
        
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
    def pokemon_title(self, color):
        # Pokemon title ASCII art
        ascii_art = self.draw_ascii("pokemon_title")  # Fetch ASCII content from file

        # Print the panel with centered alignment for ASCII art
        self.console.print(
            Panel(
                Align.center(f"[{color}]{ascii_art}[/{color}]", vertical="middle"),
                style="white",
                border_style=color,
                box=HEAVY
            )
        )

    def message_board_progress_bar(self, message, color):
        # Display a message in a styled panel
        self.clear_screen()
        # top watermark
        self.pokemon_title("blue")

        self.console.print(
            Panel(
                Align.center(f"[{color}]{message}[/{color}]\n{self.progress_bar_animation(3)}", vertical="middle"),
                style="white",
                border_style=color,
                box=HEAVY,
                padding=(3, 3)
            )
        )
        time.sleep(2)


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
            with self.console.status(f"[green]{message}[/green]", spinner=spinner_type) as status:
                sleep(seconds)
        except Exception as e:
            self.console.print(f"[red]Error in spinner animation: {e}[/red]")

    

# ======================================================================================
#                            Frontend Program Flow Methods
# ======================================================================================   
    def press_enter(self, message):
        self.console.print(
            Align.center(
                Panel(
                    f"[green]{message}[/green]",
                    style="white",
                    border_style="yellow",
                    box=HEAVY,
                    expand=False  # Fits the content exactly
                ),
                vertical="middle"  # Centers the entire panel verticall
            )
        )


        
    
    #✅ Working
    def program_intro(self) -> None:
        self.clear_screen()

        # top watermark
        self.pokemon_title("white")

        # Additional Information and Messages
        self.console.print(Align.center("[yellow]🛈[/yellow]:✨ Each player must [green]choose 3 Pokemon[/green]✨", vertical="middle"), style="white")
        self.console.print(Align.center("Equip your pokemon with a [purple]Item effects![/purple]", vertical="middle"), style="white")
        self.console.print(Align.center("[bold][green]💚 potion to increase power! [/green] or [red]💔 poison to decrease opponent's power![red][/bold].", vertical="middle"), style="white")
        self.console.print(Align.center("\n\n[yellow]🛈[/yellow]: After every battle, ⚔️ pokemon lose [red]-5 Health💔 due to fatigue [/red]", vertical="middle"), style="white")

        # Print final panel to prompt user to start or quit
        self.press_enter("Press enter to start")

        # Wait for user input to continue or quit
        self.wait_for_start()


    # ✅ Working
    # This method displays the Pokemon array from the backend using a rich table.
    # It shows the available Pokemon for selection and prints the table center-aligned.
    def display_pokemon_array(self) -> None:
        self.clear_screen()

        # top watermark
        self.pokemon_title("green")
        
        self.console.print(Align.center("\n[green]Choose 3 pokemons![/green]", vertical="middle"), style="white")
        self.console.print(Align.center("Selected pokemons will be [red]removed from the pokemon list![/red]", vertical="middle"), style="white")
        
        table = Table(border_style="white", box=HEAVY, title="Available Pokemon")
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
        row1_right = player_stack[0] if player_stack else "?"

        row2_left = player_queue[1][0] if player_queue else "?"
        row2_right = player_stack[1] if player_stack else "?"

        row3_left = player_queue[2][0] if player_queue else "?"
        row3_right = player_stack[2] if player_stack else "?"

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
            title="Pokemon 1",
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
            title="Queue 1 item",
            style="green",
            border_style="green",
            width=right_width,
            padding=(1, 1),
            box=HEAVY,
        )

        panel2_left = Panel(
            left_aligned_message2,
            title="Pokemon 2",
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
            title="Queue 2 item",
            style="red",
            border_style="red",
            width=right_width,
            padding=(1, 1),
            box=HEAVY,
        )

        panel3_left = Panel(
            left_aligned_message3,
            title="Pokemon 3",
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
            title="Queue 3 item",
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
        
        # top watermark
        self.pokemon_title("yellow")
        
        self.console.print(Panel(Align.center(f"[bold]🎇 {player_str} 🎇 Pokemon Item Selection[/bold]"), box=HEAVY, style="red", border_style="red"))
        
        # Player pokemon details
        table_pokemon_atts = Table(border_style="white", box=HEAVY)
        # Add columns for the Pokemon attributes
        table_pokemon_atts.add_column("Index", justify="center")
        table_pokemon_atts.add_column("Name", justify="center")
        table_pokemon_atts.add_column("Power Effects(Random)", justify="center")

        # Populate the table with Pokemon data from backend
        for idx, item in enumerate(self.backend.pokemon_items):
            if item == "Power Up":
                effect_str = "+30%, +20%, +10%"
            else:
                effect_str = "-30%, -20%, -10%"
                
            table_pokemon_atts.add_row(
                str(idx+1),  # Index
                str(item),  # Name
                str(effect_str)
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
            row1_left, row1_right = player1_pokemon[0], player2_pokemon[0]
            
            # Create aligned messages for each panel in all rows
            left_aligned_message1 = Align.center(row1_left)
            middle_aligned_message1 = Align.center("VS")
            right_aligned_message1 = Align.center(row1_right)
            
            panel1_left = Panel(
                left_aligned_message1,
                title="Player 1",
                style="white",
                border_style="green",
                width=left_width,
                box=HEAVY,
            )       
            panel1_middle = Panel(
                middle_aligned_message1,
                style=style_color,
                border_style=style_color,
                width=middle_width,
                box=HEAVY,
            )
            panel1_right = Panel(
                right_aligned_message1,
                title="Player 2",
                style="white",
                border_style="green",
                width=right_width,
                box=HEAVY,
            )
    
            # Create a table to align the panels side by side for all rows
            table = Table.grid()
            table.add_column(justify="center", width=left_width)
            table.add_column(justify="center", width=middle_width)
            table.add_column(justify="center", width=right_width)
            
            # Add rows to the table
            table.add_row(panel1_left, panel1_middle, panel1_right)
            
            # top watermark
            self.pokemon_title("red")

            self.print_panel(f"Battle {battle_index}", "", "blue", width_fraction=1, panel_align="center")
            
            # Print the table
            self.console.print(Align.center(table))
            time.sleep(1)

            self.console.input(Panel(Align.center("[bold yellow]PRESS ENTER TO BATTLE START![/bold yellow]", vertical="middle"), style=style_color, border_style=style_color, box=HEAVY))
    
    def display_battle_calc(self, style_color: str, player1_pokemon: list, player2_pokemon: list, battle_index: int,
                        player1_counter_str: str, player2_counter_str: str, player1_stack: list, player2_stack: list,
                        player1_element_power: int, player2_element_power: int, player1_power_effect: int, player2_power_effect: int,
                        player1_poison_effect: int, player2_poison_effect: int, player1_final_power: int, player2_final_power: int, battle_winner: str) -> None:
            self.clear_screen()

            item_color = {"Power Up" : "green",
                          "Poison" : "red",
                
            }

            # Get player stack item change color panel
            player1_item = player1_stack[0] if player1_stack else None
            player1_item_color = item_color.get(player1_item, "white")

            player2_item = player2_stack[0] if player2_stack else None
            player2_item_color = item_color.get(player2_item, "white")
            
            player1_item_color = player1_item_color or "white"
            player2_item_color = player2_item_color or "white"



            element_colors = {
                "Fire": "red",
                "Electric": "yellow",
                "Water": "blue",
                "Grass": "green",
                "Normal": "white",
                "Ice": "cyan",
            }
            
            # Get pokemon type change color panel
            player1_type = player1_pokemon[1]
            player1_element_color = element_colors.get(player1_type, "default")

            player2_type = player2_pokemon[1]
            player2_element_color = element_colors.get(player2_type, "default")

            # Get console width
            total_width = self.console.size.width

            # Calculate individual section widths
            left_width = (7 * total_width) // 16
            middle_width = total_width // 8
            right_width = (7 * total_width) // 16

            # Take elements from the queues for each row
            row1_left, row1_right = player1_pokemon[0], player2_pokemon[0]

            # Create aligned messages for each panel in all rows
            left_aligned_message1 = Align.center(row1_left)
            middle_aligned_message1 = Align.center("VS")
            right_aligned_message1 = Align.center(row1_right)

            # String Formatting for element counter multiplier display
            if player1_counter_str == "neutral" and player2_counter_str == "neutral":
                counter_str = "None"
                player1_element_perc = "+ 0%"
                player2_element_perc = "+ 0%"
            elif player1_counter_str == "opponent countered" and player2_counter_str == "player countered":
                counter_str = ">"
                player1_element_perc = "+ 10%"
                player2_element_perc = "- 15%"
            elif player1_counter_str == "player countered" and player2_counter_str == "opponent countered":
                counter_str = "<"
                player1_element_perc = "- 15%"
                player2_element_perc = "+ 10%"
            else:
                counter_str = "?"
                player1_element_perc = "+ 0%"
                player2_element_perc = "+ 0%"

            # String Formatting for item effectiveness display
            player1_item_effectiveness = "Unknown"
            player2_item_effectiveness = "Unknown"

            if len(player1_stack) > 1:
                if player1_stack[1] == 0.1:
                    player1_item_effectiveness = "10%"
                elif player1_stack[1] == 0.2:
                    player1_item_effectiveness = "20%"
                elif player1_stack[1] == 0.3:
                    player1_item_effectiveness = "30%"

            if len(player2_stack) > 1:
                if player2_stack[1] == 0.1:
                    player2_item_effectiveness = "10%"
                elif player2_stack[1] == 0.2:
                    player2_item_effectiveness = "20%"
                elif player2_stack[1] == 0.3:
                    player2_item_effectiveness = "30%"

            # String Formatting for Power Up
            if player1_stack and player1_stack[0] == "Power Up":
                player1_power_up_str = f"[white]{player1_element_power}[/white] + [purple]{player1_item_effectiveness}[/purple] = [green]{player1_power_effect}[/green]"
            else:
                player1_power_up_str = "None"

            if player2_stack and player2_stack[0] == "Power Up":
                player2_power_up_str = f"[white]{player1_element_power}[/white] + [purple]{player1_item_effectiveness}[/purple] = [green]{player1_power_effect}[/green]"
            else:
                player2_power_up_str = "None"

            # String Formatting for Poison
            if player1_stack and player1_stack[0] == "Poison":
                player2_poison_str = f"[white]{player2_power_effect}[/white] - [purple]{player1_item_effectiveness}[/purple] = [red]{player2_poison_effect}[/red]"
            else:
                player2_poison_str = "None"

            if player2_stack and player2_stack[0] == "Poison":
                player1_poison_str = f"[white]{player1_power_effect}[/white] - [purple]{player2_item_effectiveness}[/purple] = [red]{player1_poison_effect}[/red]"
            else:
                player1_poison_str = "None"
                
            if player1_final_power > player2_final_power:
                power_comp = ">"
                player1_comp_color = "yellow"
                player2_comp_color = "black"

            elif player1_final_power < player2_final_power:
                power_comp = "<"
                player1_comp_color = "black"
                player2_comp_color = "yellow"
            else:
                power_comp = "=="
                player1_comp_color = "white"
                player2_comp_color = "white"

            
            # Pokemon Name
            panel1_left = Panel(
                left_aligned_message1,
                title="Player 1",
                style="white",
                border_style=player1_element_color,
                width=left_width,
                box=HEAVY,
            )
            panel1_middle = Panel(
                "",
                style="black",
                border_style="black",
                width=middle_width,
            )
            panel1_right = Panel(
                right_aligned_message1,
                title="Player 2",
                style="white",
                border_style=player2_element_color,
                width=right_width,
                box=HEAVY,
            )
            
            # Health
            panel2_left = Panel(
                str(player1_pokemon[2]),
                title="Health",
                style="green",
                border_style="white",
                width=right_width,
            )
            panel2_middle = Panel(
                "",
                style="black",
                border_style="black",
                width=middle_width,

            )
            panel2_right = Panel(
                str(player2_pokemon[2]),
                title="Health",
                style="green",
                border_style="white",
                width=right_width,
            )
            
            # Element
            panel3_left = Panel(
                str(player1_pokemon[1]),
                title="Element",
                style=player1_element_color,
                border_style=player1_element_color,
                width=right_width,
                box=HEAVY,
            )
            
            panel3_middle = Panel(
                counter_str,
                title="Counter",
                style="yellow",
                border_style="white",
                width=middle_width,
                box=HEAVY,
            )
            panel3_right = Panel(
                str(player2_pokemon[1]),
                title="Element",
                style=player2_element_color,
                border_style=player2_element_color,
                width=right_width,
                box=HEAVY,
            )
            
            # Power Multiplier
            panel4_left = Panel(
                str(f"[green]{player1_element_perc}[/green]"),
                title="Element Multiplier",
                style="white",
                border_style="white",
                width=right_width,
            )
            panel4_middle = Panel(
                "",
                style="black",
                border_style="black",
                width=middle_width,

            )
            panel4_right = Panel(
                str(f"[green]{player2_element_perc}[/green]"),
                title="Element Multiplier",
                style="white",
                border_style="white",
                width=right_width,
            )
            
            # Base Power
            panel5_left = Panel(
                str(f"{player1_pokemon[3]} {player1_element_perc} = [{player1_item_color}]{player1_element_power}[/{player1_item_color}]"),
                title="Base Power",
                style="white",
                border_style="white",
                width=right_width,
                box=HEAVY,
            )
            panel5_middle = Panel(
                "",
                style="black",
                border_style="black",
                width=middle_width,
            )
            panel5_right = Panel(
                str(f"{player2_pokemon[3]} {player2_element_perc} = [{player2_item_color}]{player2_element_power}[/{player2_item_color}]"),
                title="Base Power",
                style="white",
                border_style="white",
                width=right_width,
                box=HEAVY,
            )

            
            # Item
            panel6_left = Panel(
                str(player1_stack[0]),
                title="Item",
                style=player1_item_color,
                border_style=player1_item_color,
                width=right_width,
            )
            panel6_middle = Panel(
                "",
                style="black",
                border_style="black",
                width=middle_width, 
            )
            panel6_right = Panel(
                str(player2_stack[0]),
                title="Item",
                style=player2_item_color,
                border_style=player2_item_color,
                width=right_width,
            )
            
            # Item
            panel7_left = Panel(
                f"{player1_item_effectiveness}",
                title=f"{player1_stack[0]} Random Effectiveness",
                style="purple",
                border_style="purple",
                width=right_width,
            )
            panel7_middle = Panel(
                "",
                style="black",
                border_style="black",
                width=middle_width,
            )
            panel7_right = Panel(
                f"{player2_item_effectiveness}",
                title=f"{player2_stack[0]} Random Effectiveness",
                style="purple",
                border_style="purple",
                width=right_width,
            )
            
            # Power Up
            panel8_left = Panel(
                f"{player1_power_up_str}",
                title=f"Power Up",
                style="white",
                border_style="white",
                width=right_width,
            )
            panel8_middle = Panel(
                "",
                style="black",
                border_style="black",
                width=middle_width,

            )
            panel8_right = Panel(
                f"{player2_power_up_str}",
                title=f"Power Up",
                style="white",
                border_style="white",
                width=right_width,
            )
            
            # Poison
            panel9_left = Panel(
                f"{player1_poison_str}",
                title=f"Poison",
                style="red",
                border_style="white",
                width=right_width,
            )
            panel9_middle = Panel(
                "",
                style="black",
                border_style="black",
                width=middle_width,
            )
            panel9_right = Panel(
                f"{player2_poison_str}",
                title=f"Poison",
                style="red",
                border_style="white",
                width=right_width,
            )
            
            # Final Power
            panel10_left = Panel(
                f"{player1_final_power}",
                title=f"Final Power",
                style="white",
                border_style=player1_comp_color,
                width=right_width,
                box=HEAVY,
            )
            panel10_middle = Panel(
                f"{power_comp}",
                title="Power Comparison",
                style=style_color,
                border_style=style_color,
                width=middle_width,
                box=HEAVY,
            )
            panel10_right = Panel(
                f"{player2_final_power}",
                title=f"Final Power",
                style="white",
                border_style=player2_comp_color,
                width=right_width,
                box=HEAVY,
            )
            
            
            # Define the rows
            rows = [
                (panel1_left, panel1_middle, panel1_right),
                (panel2_left, panel2_middle, panel2_right),
                (panel3_left, panel3_middle, panel3_right),
                (panel4_left, panel4_middle, panel4_right),
                (panel5_left, panel5_middle, panel5_right),
                (panel6_left, panel6_middle, panel6_right),
                (panel7_left, panel7_middle, panel7_right),
                (panel8_left, panel8_middle, panel8_right),
                (panel9_left, panel9_middle, panel9_right),
                (panel10_left, panel10_middle, panel10_right),
            ]

            self.print_panel(f"[white]🔥 Battle {battle_index} 🔥[/white]", "", "blue",  width_fraction=1, panel_align="center")
            
            # Print each row with a delay
            for row in rows:
                # Create a new table for only the current row
                temp_table = Table.grid()
                temp_table.add_column(justify="center", width=left_width)
                temp_table.add_column(justify="center", width=middle_width)
                temp_table.add_column(justify="center", width=right_width)
                temp_table.add_row(*row)  # Add only the current row
                try:
                    self.console.print(temp_table)
                except Exception as e:
                    print(f"Error rendering table: {e}")
  # Print the table for this row
                time.sleep(1)  # Add a 1-second delay before printing the next row
                   
            battle_result_str = ""
            if battle_winner == "Player 1":
                battle_result_str = "🏆 Player 1 wins! 🏆"
            elif battle_winner == "Player 2":
                battle_result_str = "🏆 Player 2 wins! 🏆"
            else:
                battle_result_str = "🏆 Tie! 🏆"
                
            self.console.print(
            Align.center(
                Panel(
                    f"[yellow]{battle_result_str}[/yellow]",
                    style="white",
                    border_style="yellow",
                    box=HEAVY,
                ),
                vertical="middle"  # Centers the entire panel verticall
            )
        )
            self.console.input(Panel(Align.center("🔥 PRESS ENTER TO NEXT BATTLE QUEUE 🔥", vertical="middle"), style=style_color, border_style=style_color, box=HEAVY))
    
    def display_health_adjustment(self, player1_pokemon, player2_pokemon, player1_health: int, player2_health: int) -> None:
        self.clear_screen()

        element_colors = {
                "Fire": "red",
                "Electric": "yellow",
                "Water": "blue",
                "Grass": "green",
                "Normal": "white",
                "Ice": "cyan",
            }
            
        # Get pokemon type change color panel
        player1_type = player1_pokemon[1]
        player1_element_color = element_colors.get(player1_type, "default")

        player2_type = player2_pokemon[1]
        player2_element_color = element_colors.get(player2_type, "default")

        # Get console width
        total_width = self.console.size.width
        
        style_color = "blue"
        
        # Calculate individual section widths
        left_width = (7 * total_width) // 16
        right_width = (7 * total_width) // 16
        
        panel1_left = Panel(
            f"{player1_pokemon[0]}",
            title="Player 1",
            style="white",
            border_style=player1_element_color,
            width=left_width,
            box=HEAVY,
        )
        
        panel1_right = Panel(
            f"{player2_pokemon[0]}",
            title="Player 2",
            style="white",
            border_style=player2_element_color,
            width=right_width,
            box=HEAVY,
        )
        
        panel2_left = Panel(
            f"{player1_pokemon[2]} -> {player1_health}",
            title="HP",
            style="white",
            border_style="yellow",
            width=left_width,
            box=HEAVY,
        )
        
        panel2_right = Panel(
            f"{player2_pokemon[2]} -> {player2_health}",
            title="HP",
            style="white",
            border_style="green",
            width=right_width,
            box=HEAVY,
        )
        
        table = Table.grid()
        table.add_column(justify="center", width=left_width)
        table.add_column(justify="center", width=right_width)
        
        table.add_row(panel1_left, panel1_right)
        table.add_row(panel2_left, panel2_right)
        
        self.print_panel(
            f"Health Adjustment\n Due to Fatigue Pokemon loses 5 HP",
            "",
            "blue",
            width_fraction=1,
            panel_align="center"
        )

        
        # Print the table
        self.console.print(Align.center(table))
        print()
        
        self.console.input(Panel(Align.center("[bold]PRESS ENTER TO NEXT BATTLE QUEUE![/bold]", vertical="middle"), style=style_color, border_style=style_color, box=HEAVY))
    
    def Display_battle_summary(self, battle_summaries) -> None:
        self.clear_screen()

        

        table = Table(border_style="white", box=HEAVY, title="Battle Results")
        # Add columns for battle details
        table.add_column("Battle", justify="center")
        table.add_column("Player 1", justify="center")
        table.add_column("Player 1 Power", justify="center")
        table.add_column("Player 2", justify="center")
        table.add_column("Player 2 Power", justify="center")
        table.add_column("Winner", justify="center")

        # Populate the table with battle summary data
        for battle in battle_summaries:
            table.add_row(
                str(battle[0]),  # Battle number
                str(battle[1]),  # Player 1's Pokémon name
                str(battle[2]),  # Player 1's Pokémon power
                str(battle[3]),  # Player 2's Pokémon name
                str(battle[4]),  # Player 2's Pokémon power
                str(battle[5]),  # Winner
            )

        # top watermark
        self.pokemon_title("purple")
        
        # Print the table center-aligned
        self.console.print(Align.center(table))
    
    # ============================================================================
    #                         PLAYER SELECTION METHODS
    # ============================================================================    
    # ✅ working
    def prompt_player_selection(self, player: str) -> str:
        self.console.print(Align.center(f"[yellow]✨ {player} ✨[/yellow]", vertical="middle"), style="white")

        self.console.print(
            Panel(
                Align.center("[cyan]Enter 3 Pokémon in order for battle use by entering their indices (space-separated):[/cyan]", vertical="middle"),
                style="white",
                border_style="yellow",
                box=HEAVY
            )
        )
        return input("> ").strip()

    def prompt_player_item_selection(self) -> str:
        self.console.print(
            Panel(
                Align.center("[cyan]Enter the index of items you want to use per pokemon (space-separated):[/cyan]", vertical="middle"),
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
    def pokemon_effects_selection(self) -> None:
        self.backend.effects_selection()
    
    # ✅ working
    def pokemon_queue_battle_start(self) -> None:
        self.backend.battle_queue_start()
        
    def pokemon_battle_summary(self) -> None:
        self.Display_battle_summary(self.backend.battle_summaries)
        
        
if __name__ == "__main__":
    import main
    main.Gameplay()
    # f = Frontend()
    # f.pokemon_queue_selection()