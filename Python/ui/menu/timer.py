#Similar to the timer that uses the time module, but this instead uses pygame. This is useful if you want to use a clock that is part of Pygame, rather than time.
import pygame
pygame.init()

class Timer:
    """A timer class, to track time measured in milliseconds"""

    def __init__(self):
        self.inittime = pygame.time.get_ticks()
        self.paused = 0

    @property
    def elapsed(self):
        """Returns the exact elapsed time since this timer was created or last restarted."""
        if self.paused != 0:
            return self.paused
        else:
            return pygame.time.get_ticks() - self.inittime

    @elapsed.setter
    def elapsed(self, amount):
        """Forces the timer to a specific time."""
        if self.paused == 0:
            self.inittime = pygame.time.get_ticks() - amount
        else:
            self.paused = amount

    def restart(self):
        """Restarts the timer, and sets its elapsed time to 0."""
        self.__init__()

    def pause(self):
        """Pauses the timer at a certain position."""
        self.paused = pygame.time.get_ticks() - self.inittime

    def resume(self):
        """Resumes the timer after being paused."""
        self.inittime = pygame.time.get_ticks() - self.paused
        self.paused = 0
