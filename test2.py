from time import sleep
from rich.console import Console
from rich.progress import Progress, BarColumn, SpinnerColumn, TextColumn

# Create a Console instance
console = Console()

def spinner_animation(seconds: int, spinner_type: str = "dots"):
    """
    Displays a spinner animation for the given duration.

    Args:
        seconds (int): The duration for which the spinner runs.
        spinner_type (str): The type of spinner to use. Defaults to 'dots'.
    """
    with console.status("[bold green]Processing...", spinner=spinner_type) as status:
        sleep(seconds)
    console.print("[bold green]Task complete![/bold green]")

def progress_bar_animation(seconds: int):
    """
    Displays a long progress bar animation for the given duration.

    Args:
        seconds (int): The duration for which the progress bar runs.
    """
    total_steps = 100
    step_duration = seconds / total_steps  # Calculate time per step

    with Progress(
        TextColumn("[bold blue]Progress:[/bold blue]"),
        BarColumn(bar_width=60),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("Loading...", total=total_steps)

        for _ in range(total_steps):
            sleep(step_duration)  # Simulate work
            progress.update(task, advance=1)  # Update progress bar

    console.print("[bold green]Task complete![/bold green]")

# Example Usage
spinner_animation(3, spinner_type="aesthetic")  # Spinner animation for 3 seconds
progress_bar_animation(5)  # Progress bar animation for 5 seconds
