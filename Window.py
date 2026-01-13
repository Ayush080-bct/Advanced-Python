import pygame
import numpy as np
from Wintgeration import integrate

pygame.init()
screen = pygame.display.set_mode((650, 450))
pygame.display.set_caption("Integration Calculator")
font = pygame.font.SysFont(None, 30)

# DISPLAY TEXT ↓                    # INTERNAL VARIABLE KEY ↓
input_labels = ["function", "a (lower limit)", "b (upper limit)"]
input_keys   = ["function", "a", "b"]

values = {"function": "", "a": "", "b": ""}
active_index = 0
result = ""
MAX_CHARS = 20

button_rect = pygame.Rect(200, 300, 200, 50)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                try:
                    eqn = values["function"]
                    a = float(values["a"])
                    b = float(values["b"])
                    result = str(integrate(eqn, a, b))
                except Exception as e:
                    result = f"Error: {e}"
            else:
                y = 50
                for i in range(len(input_keys)):
                    if pygame.Rect(50, y, 500, 30).collidepoint(event.pos):
                        active_index = i
                    y += 50

        elif event.type == pygame.KEYDOWN:
            key = input_keys[active_index]

            if event.key == pygame.K_RETURN:
                if active_index < len(input_keys) - 1:
                    active_index += 1
                continue

            if event.key == pygame.K_BACKSPACE:
                values[key] = values[key][:-1]
            else:
                if len(values[key]) < MAX_CHARS:
                    values[key] += event.unicode

                if len(values[key]) >= MAX_CHARS and active_index < len(input_keys) - 1:
                    active_index += 1

    # Draw input boxes
    y = 50
    for i in range(len(input_keys)):
        pygame.draw.rect(screen, (0, 0, 0), (50, y, 500, 30), 2)
        text = values[input_keys[i]]

        if i == active_index and pygame.time.get_ticks() % 1000 < 500:
            text += "|"

        rendered = font.render(f"{input_labels[i]}: {text}", True, (0, 0, 0))
        screen.blit(rendered, (55, y + 5))
        y += 50

   
    screen.blit(font.render("Compute Integral", True, (0, 0, 0)), (button_rect.x +30, button_rect.y + 15))

    screen.blit(font.render("Result: " + result, True, (0, 0, 0)), (50, 370))

    pygame.display.update()

pygame.quit()
