import pygame # type: ignore
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state
from logger import log_event
import sys

def main():
    # Notify game starting to console with pygame version and game screen properties
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # Initialize pygame 
    pygame.init()

    # Global initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    

    # GAME LOOP START

    while True:

        dt = clock.tick(60) / 1000
        print(dt)
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill('black')
        updatable.update(dt) 

        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            if (player.collides_with(asteroid)):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        
        pygame.display.flip()

        
        


if __name__ == "__main__":
    main()
