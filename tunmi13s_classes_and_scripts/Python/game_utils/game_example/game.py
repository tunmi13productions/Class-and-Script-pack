"""
Game example
This example assumes you have the following packages installed.
pygame
accessible_output2
This is just a simple game loop. It does not simulate any sort of real game!
This is also an attempt to make people veer away from audio game engines and use Pygame, which is a part of Python. Do keep in mind that some things in Pygame are not entirely accessible, so of course, you may have to make modifications.
In this example we will be using an event called pygame.KEYDOWN. This event checks if a key has been pressed.
Here is a list of other events with their respective descriptions.
pygame.KEYUP: Detect if a key has been released.
pygame.key.get_pressed(): Detects if a key is being held down. Use this if you are, say, holding down Shift/CTRL/ALT.
"""
#Imports
import pygame
from accessible_output2.outputs.auto import *
output = Auto()
#This is just a function that makes it easier to speak.
def speak(text,interrupt = False):
 output.speak(text,interrupt)
def game():
 #Before starting the game loop, we need to create a window, and also initiate Pygame.
 pygame.init()
 #If you need, you can make the window bigger, but this is the width we are using.
 win = pygame.display.set_mode((600,400))
 #Now we will set the caption of the window. Now that the display has been modified, this will also modify the title.
 pygame.display.set_caption("My game")
 #In order to keep the loop active, we need to keep the window active. Otherwise, it will freeze. We use Pygame's clock.
 clock = pygame.time.Clock()
 #We wil now say welcome to the user, and start the game loop.
 speak("Hello and welcome to my game! I mean it's not really a game but, hey!")
 #Initiate the loop.
 while True:
  #Another thing required to keep the window active is to also update the display. Otherwise, again, it will freeze.
  pygame.display.update()
  #Make the clock tick. If you are/were a BGT user, this is an alternative to wait.
  clock.tick(50)
  #This is how you handle keyboard events. Some people are probably used to key_pressed, key_down, etc. But in Pygame, here is how you would go about doing this.
  #First, get a list of events that are happening in Pygame.
  for event in pygame.event.get():
   #The event type we are looking for is when a key is pressed. This is known as KEYDOWN in Pygame.
   if event.type == pygame.KEYDOWN:
    #In this example, we're not actually going to check for if a specific key is pressed, besides the Escape key. But feel free to uncomment this following line if you wish so you can test out the different keys Pygame has. To get a list of key codes, refer to the document in this example folder.
    #if event.key == pygame.K_SPACE: speak("You just pressed the spacebar! Yay!")
    #Let's get any event when a key is pressed. This means we don't have to make an if statement of whether a certain key is pressed, we just have to speak a key that has been pressed, because we already specified we are looking for keydown events. We can get the label of the key in two different ways. using pygame.key.name(event.key) will actually announce the key name, and using pygame.key will actually report the character number in the ASCII table.
    speak(f"You just pressed {event.key}, which is {pygame.key.name(event.key)}!")
    #This is the code to exit the game.
    if event.key == pygame.K_ESCAPE:
     #We must quit Pygame and then break the loop.
     pygame.quit()
     break
#Now run the game by executing the game function.
game()