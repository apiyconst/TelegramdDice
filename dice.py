import pygame
import random
import imageio
from telegram import update

# Definitions for window size and FPS
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300
FPS = 30
# Colors
WHITE = (255, 255, 255)
# Dice images
dice_images = [
    pygame.image.load('dicetemplate/dice1.png'),
    pygame.image.load('dicetemplate/dice2.png'),
    pygame.image.load('dicetemplate/dice3.png'),
    pygame.image.load('dicetemplate/dice4.png'),
    pygame.image.load('dicetemplate/dice5.png'),
    pygame.image.load('dicetemplate/dice6.png')
]
# Initialize Pygame
pygame.init()
# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Dice Animation')
# Position and angle values for dice
dice_width = 83
dice_x = [WINDOW_WIDTH / 2 - dice_width, WINDOW_WIDTH / 2]
dice_angle = [0, 0]
# Game loop
running = True
clock = pygame.time.Clock()
rotate_speed = 20
rotate_done = [False, False]
dice_number = [1, 1]  # Initial value
# Settings for GIF file
gif_duration = 3000  # in milliseconds
frame_duration = 1000 // FPS  # in milliseconds
# Create GIF file using imageio
with imageio.get_writer("dice_roll.gif", mode="I", fps=FPS) as writer:
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                for i in range(2):
                    rotate_done[i] = False
                    dice_angle[i] = 0
        # Set FPS
        clock.tick(FPS)
        # Clear screen
        screen.fill(WHITE)
        # Choose a random number for the dice and rotate them
        for i in range(2):
            if not rotate_done[i]:
                # Choose a random number for the dice
                dice_number[i] = random.randint(1, 6)
                # Rotate the dice
                if dice_angle[i] < 360:
                    dice_angle[i] += rotate_speed
                else:
                    rotate_done[i] = True
            # Draw the rotated image of the dice on the screen
            rotated_image = pygame.transform.rotate(dice_images[dice_number[i] - 1], dice_angle[i])
            rect = rotated_image.get_rect()
            rect.center = (dice_x[i] + dice_width / 2, WINDOW_HEIGHT / 2)
            screen.blit(rotated_image, rect)
        # Update screen
        pygame.display.flip()
        # Take a screenshot of the screen and write it to the GIF file
        pygame_surface = pygame.display.get_surface()
        # Use transpose() to properly rotate the matrices
        screenshot = pygame.surfarray.array3d(pygame_surface).transpose([1, 0, 2])
        writer.append_data(screenshot)
        # Stop the loop if the duration of the animation is over
        if pygame.time.get_ticks() >= gif_duration:
            break
    # Release the writer
    writer.close()

    # Bot response
    with open(output_path, 'rb') as gif_file:
        update.message.reply_video(gif_file, timeout=100)
# Quit Pygame
pygame.quit()