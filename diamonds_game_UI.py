import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 10}

# Load the card images and scale them down
cards = {f"{i}_of_{j}": pygame.transform.scale(pygame.image.load(f"cards/{i}_of_{j}.png"), (72, 96)) for i in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'] for j in ['hearts', 'clubs', 'diamonds']}

# Player Information
player_name = "Player 1"
player_points = 0
player_hand = [f"{i}_of_hearts" for i in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']]  # This should be dynamically updated

# Computer Information
computer_name = "Computer"
computer_points = 0
computer_hand = [f"{i}_of_clubs" for i in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']]  # This should be dynamically updated

# Diamond Card Auction Section
round_number = 1  # This should be dynamically updated
diamond_cards = [f"{i}_of_diamonds" for i in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']]
auction_card = random.choice(diamond_cards)  # Random diamond card

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            # Check if a card from the player's hand was clicked
            for i, card in enumerate(player_hand):
                if pygame.Rect(20 + i * 80, 60, 72, 96).collidepoint(pygame.mouse.get_pos()):
                    # Player bids with the clicked card
                    player_bid = card

                    # Computer bids with a random card
                    computer_bid = random.choice(computer_hand)

                    # Compare the bids and update the scores
                    if player_bid > computer_bid:
                        player_points += points[auction_card.split('_')[0]]  # Add the points from the diamond card
                    elif computer_bid > player_bid:
                        computer_points += points[auction_card.split('_')[0]]  # Add the points from the diamond card
                    else:  # If there's a tie
                        player_points += points[auction_card.split('_')[0]] // 2  # Divide the points from the diamond card equally
                        computer_points += points[auction_card.split('_')[0]] // 2  # Divide the points from the diamond card equally

                    # Remove the bid cards from the hands
                    player_hand.remove(player_bid)
                    computer_hand.remove(computer_bid)

                    round_number += 1
                    if round_number <= 13:  # If there are still rounds left
                        auction_card = random.choice(diamond_cards)
                    else:  # If all rounds have been played
                        if player_points > computer_points:
                            winner = player_name
                        elif computer_points > player_points:
                            winner = computer_name
                        else:
                            winner = "It's a tie!"

    # Fill the screen with a color
    screen.fill((255, 255, 255))

    # Display player information
    font = pygame.font.Font(None, 36)
    text = font.render(f"Name: {player_name} Points: {player_points}", True, (0, 0, 0))
    screen.blit(text, (20, 20))

    # Display player's hand
    for i, card in enumerate(player_hand):
        screen.blit(cards[card], (20 + i * 80, 60))  # Adjusted the spacing between cards

    # Display computer information
    text = font.render(f"Name: {computer_name} Points: {computer_points}", True, (0, 0, 0))
    screen.blit(text, (20, screen_height - 130))  # Display at the bottom of the screen

    # Display computer's hand
    for i, card in enumerate(computer_hand):
        screen.blit(cards[card], (20 + i * 80, screen_height - 100))  # Display at the bottom of the screen

    # Display Diamond Card Auction Section
    text = font.render(f"Round: {round_number}", True, (0, 0, 0))
    screen.blit(text, (screen_width // 2, screen_height // 2 - 20))  # Display in the middle of the screen
    if round_number <= 13:  # If there are still rounds left
        screen.blit(cards[auction_card], (screen_width // 2, screen_height // 2 + 20))  # Display in the middle of the screen
    else:  # If all rounds have been played
        text = font.render(f"The game has ended. {winner} wins!", True, (0, 0, 0))
        screen.blit(text, (screen_width // 2, screen_height // 2 + 20))  # Display in the middle of the screen

    # Update the display
    pygame.display.update()

pygame.quit()

