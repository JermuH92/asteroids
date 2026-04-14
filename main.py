import pygame # type: ignore
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from logger import log_state

def main():
    # Notify game starting to console with pygame version and game screen properties
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # Initialize pygame 
    pygame.init()

    # Global settings
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # GAME LOOP START

    while True:

        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill('black') 
        player.draw(screen)
        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
