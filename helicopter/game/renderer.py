"""
renderer: all pygame drawing lives here, kept separate from game logic.
"""

import pygame


WIDTH, HEIGHT = 700, 500
WINDOW_SIZE = (WIDTH, HEIGHT)

COLOR_BG = (140, 200, 230)
COLOR_HELI = (60, 60, 70)
COLOR_OBSTACLE = (70, 150, 80)
COLOR_TEXT = (20, 20, 20)
COLOR_SHIELD = (50, 150, 255)


def draw_scene(
    surface,
    helicopter,
    obstacles,
    distance,
    game_over,
    shield_active,
    font,
):
    surface.fill(COLOR_BG)

    for obstacle in obstacles:
        pygame.draw.rect(
            surface,
            COLOR_OBSTACLE,
            obstacle.get_top_rect(),
        )

        pygame.draw.rect(
            surface,
            COLOR_OBSTACLE,
            obstacle.get_bottom_rect(),
        )

    # Draw shield behind the helicopter when active.
    if shield_active:
        pygame.draw.circle(
            surface,
            COLOR_SHIELD,
            helicopter.get_rect().center,
            max(helicopter.get_rect().width, helicopter.get_rect().height),
            4,
        )

    pygame.draw.rect(
        surface,
        COLOR_HELI,
        helicopter.get_rect(),
        border_radius=4,
    )

    draw_text(
        surface,
        font,
        f"Distance: {int(distance)}",
        (20, 20),
    )

    if shield_active:
        draw_text(
            surface,
            font,
            "SHIELD ACTIVE",
            (20, 50),
            COLOR_SHIELD,
        )

    if game_over:
        draw_banner(
            surface,
            font,
            f"GAME OVER - Distance: {int(distance)}",
        )


def draw_text(surface, font, text, pos, color=COLOR_TEXT):
    surface.blit(font.render(text, True, color), pos)


def draw_banner(surface, font, text):
    surf = font.render(text, True, (180, 40, 40))
    rect = surf.get_rect(
        center=(
            surface.get_width() // 2,
            surface.get_height() // 2,
        )
    )
    surface.blit(surf, rect)