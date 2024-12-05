from time import sleep
from rich.console import Console
from PIL import Image

def print_image(image_path: str, width: int = 50):
    console = Console()

    # Load the image
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        console.print(f"[bold red]Error: File '{image_path}' not found.[/]")
        return

    # Resize the image
    img = img.resize((width, int(img.height * (width / img.width) * 0.55)))
    img = img.convert("RGB")  # Ensure it's RGB format

    # Convert pixels to ANSI escape codes
    pixels = img.load()
    for y in range(img.height):
        row = []
        for x in range(img.width):
            r, g, b = pixels[x, y]
            row.append(f"\x1b[48;2;{r};{g};{b}m ")  # ANSI code for background
        console.print("".join(row) + "\x1b[0m")  # Reset formatting

# Test the function
print_image("./picture.jpg", width=50)
