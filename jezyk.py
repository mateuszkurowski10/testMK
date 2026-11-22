import subprocess
import sys

try:
    import pygame
except ImportError:
    print("🦔 Budzenie jeży...")
    subprocess.check_call([
        sys.executable,
        "-m", "pip",
        "install", "pygame-ce"
    ])
    import pygame

import random
import math
pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JEŻOWY CHAOS 3000 🦔")

clock = pygame.time.Clock()

jeze = []

for i in range(20):
    jeze.append({
        "x": random.randint(50, WIDTH-50),
        "y": random.randint(50, HEIGHT-50),
        "dx": random.uniform(-5, 5),
        "dy": random.uniform(-5, 5),
        "size": random.randint(15, 35),
        "angle": random.randint(0, 360),
        "color": [random.randint(50, 255) for _ in range(3)]
    })

font = pygame.font.SysFont("comicsansms", 35)

running = True
t = 0

while running:
    clock.tick(60)
    t += 0.05

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((
        int(100 + 100 * math.sin(t)),
        int(50 + 50 * math.cos(t)),
        130
    ))

    for j in jeze:
        j["x"] += j["dx"]
        j["y"] += j["dy"]
        j["angle"] += 8

        if j["x"] < 20 or j["x"] > WIDTH-20:
            j["dx"] *= -1
        if j["y"] < 20 or j["y"] > HEIGHT-20:
            j["dy"] *= -1

        j["color"] = [
            int(127 + 127 * math.sin(t + j["x"])),
            int(127 + 127 * math.sin(t + j["y"])),
            int(127 + 127 * math.cos(t))
        ]

        x = int(j["x"])
        y = int(j["y"])
        s = j["size"]

        # KOLCE
        for i in range(12):
            angle = math.radians(i * 30 + j["angle"])
            ex = x + math.cos(angle) * s
            ey = y + math.sin(angle) * s

            pygame.draw.line(
                screen, (30, 20, 10),
                (x, y), (ex, ey), 4
            )

        # CIAŁO
        pygame.draw.circle(
            screen, j["color"], (x, y), s
        )

        # PYSZCZEK
        pygame.draw.circle(
            screen, (230, 180, 140),
            (x + s//2, y), s//2
        )

        # OKO
        pygame.draw.circle(
            screen, (0, 0, 0),
            (x + s//2, y - 5), 3
        )

    text = font.render(
        "JEŻOWY CHAOS 🦔",
        True, (255, 255, 255)
    )
    screen.blit(text, (270, 20))

    pygame.display.flip()


pygame.quit()