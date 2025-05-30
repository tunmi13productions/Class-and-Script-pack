# Example usage
# Press and hold Space to continuously hear the windows ding sound.
import pygame
import winsound
from keyhold import key_hold

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Key Hold Test")
    clock = pygame.time.Clock()
    
    # Create key hold instance for SPACE key
    # Initial delay: 500ms, Repeat interval: 100ms
    space_hold = key_hold(pygame.K_SPACE, 500, 100)
    
    counter = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get current key states
        keys = pygame.key.get_pressed()
        
        # Check key hold states
        if space_hold.pressing(keys):
            counter += 1
            print(f"Space triggered! Count: {counter}")
            winsound.MessageBeep(winsound.MB_OK)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()