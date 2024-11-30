import pygame
pygame.init()

# Define screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drag & Snap Example")

# Define colors and fonts
WHITE = (255, 255, 255)
card_image = pygame.Surface((100, 150))  # Placeholder for card image
card_image.fill((200, 0, 0))  # Red card

card_rect = card_image.get_rect(center=(400, 300))  # Initial position

dragging = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if card_rect.collidepoint(event.pos):  # Check if card is clicked
                dragging = True
                offset = card_rect.topleft - event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            # Snap mechanics (just an example)
            if card_rect.left < 200:
                card_rect.topleft = (100, 100)  # Snap to a target position
            else:
                card_rect.topleft = (400, 300)  # Default position
        elif event.type == pygame.MOUSEMOTION and dragging:
            card_rect.topleft = event.pos + offset

    # Clear screen and redraw
    screen.fill(WHITE)
    screen.blit(card_image, card_rect)

    pygame.display.update()
    pygame.time.Clock().tick(60)  # Limit FPS to 60

pygame.quit()
