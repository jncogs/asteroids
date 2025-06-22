import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_score = 0
    pygame.display.set_caption(f"Player Score: {player_score}")

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    print("Starting Asteroids!")

    while player.quit != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for a in asteroids:
            for shot in shots:
                if a.collision(shot):
                    player_score += a.score()
                    a.split()
                    shot.kill()
                    pygame.display.set_caption(f"Player Score: {player_score}")
            if a.collision(player):
                print("Game over!")
                print(f"Final Score: {player_score}")
                sys.exit()

        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
    print("Quitter!")
    print(f"Final Score: {player_score}")

if __name__ == "__main__":
    main()