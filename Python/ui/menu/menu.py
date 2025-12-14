from timer import Timer
import pyperclip
import pygame
from audio import p
from accessible_output2.outputs.auto import *

speech = Auto()
pygame.init()
clock = pygame.time.Clock()

def speak(text,interrupt = False):
	speech.speak(text,interrupt)

class menu:
    def __init__(self, *args, **kwargs):
        self.items = []
        self.intern_items = []
        self.mfadetimer = Timer()
        self.clicksound = kwargs.get("clicksound", "")
        self.escapesound = kwargs.get("escapesound", "")
        self.entersound = kwargs.get("entersound", "")
        self.wrap = kwargs.get("wrap", True)
        self.opensound = kwargs.get("opensound", "")
        self.edgesound = kwargs.get("edgesound", "")
        self.music = None
        self.itemsound = None
        self.leftright = kwargs.get("leftright", True)
        self.updown = kwargs.get("updown", True)
        self.homeend = kwargs.get("homeend", True)
        self.wrapsound = kwargs.get("wrapsound", "")
        self.clipcopy = kwargs.get("clipcopy", False)
        self.musicvol = kwargs.get("musicvol", -15)
        self.musicfile = kwargs.get("musicfile", "")
        self.r = -1
        self.callback = None
        self.callback_on_self = False

    def reset(self, reset_all=False):
        self.items.clear()
        self.intern_items.clear()
        if self.music:
            p.destroy_sound(self.music)
        if reset_all:
            self.__init__()

    def add_item(self, external_name, internal_name=""):
        if external_name == "":
            return
        self.items.append(external_name)
        if internal_name == "":
            internal_name = external_name
        self.intern_items.append(internal_name)

    def play_escape(self):
        if self.escapesound != "":
            p.play_stationary(self.escapesound)

    def play_open(self):
        if self.opensound != "":
            p.play_stationary(self.opensound)

    def play_click(self):
        if self.clicksound != "":
            p.play_stationary(self.clicksound)

    def play_edge(self):
        if self.edgesound != "":
            p.play_stationary(self.edgesound)

    def play_enter(self):
        if self.entersound != "":
            p.play_stationary(self.entersound)

    def play_wrap(self):
        if self.wrapsound != "":
            p.play_stationary(self.wrapsound)

    def get_focused_item(self):
        if self.r > len(self.items) - 1 or self.r < 0:
            return ""
        else:
            return self.items[self.r]

    def get_item_name(self, position):
        if position > len(self.items) - 1 or position < 0:
            return ""
        else:
            return self.intern_items[position]

    def announce_item(self, position):
        if position > len(self.items) - 1 or position < 0:
            return
        else:
            speak(self.items[self.r], True)

    def add_music(self, path, volume=-15):
        if path == "":
            if self.music:
                p.destroy_sound(self.music)
            self.musicfile = ""
        else:
            self.musicfile = path
            self.musicvol = volume

    def set_callback(self, callback):
        self.callback = callback

    def run(self, title, intr=False):
        pygame.event.get()
        if title:
            speak(title, intr)
        if len(self.items) == 0:
            return -1
        self.r = -1
        self.play_open()
        if self.musicfile != "":
            self.music = p.play_stationary_extended(
                self.musicfile, True, 0, 0, self.musicvol, 100
            )
        while True:
            pygame.display.update()
            clock.tick(60)
            if callable(self.callback):
                if self.callback_on_self:
                    self.callback(self)
                else:
                    self.callback()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.unicode:
                        char = event.unicode
                        first = 0
                        counter = self.r
                        for i in range(counter, len(self.items)):
                            if i == self.r:
                                continue
                            first_letter = self.items[i][:1]
                            if char.lower() == first_letter.lower():
                                counter = i
                                first = 1
                                break
                        if first == 0:
                            for i in range(0, len(self.items)):
                                if i == self.r:
                                    continue
                                first_letter = self.items[i][:1]
                                if char.lower() == first_letter.lower():
                                    counter = i
                                    first = 1
                                    break
                        if first == 1:
                            self.r = counter
                            self.play_click()
                            self.announce_item(self.r)
                    if event.key == pygame.K_UP and self.updown:
                        if self.r <= 0:
                            if self.wrap:
                                self.r = len(self.items) - 1
                                self.play_click()
                                self.play_wrap()
                            else:
                                self.r = 0
                                self.play_edge()
                        else:
                            self.play_click()
                            self.r -= 1
                        self.announce_item(self.r)
                    if event.key == pygame.K_DOWN and self.updown:
                        if self.r >= len(self.items) - 1:
                            if self.wrap:
                                self.r = 0
                                self.play_click()
                                self.play_wrap()
                            else:
                                self.r = len(self.items) - 1
                                self.play_edge()
                        else:
                            self.play_click()
                            self.r += 1
                        self.announce_item(self.r)
                    if event.key == pygame.K_LEFT and self.leftright:
                        if self.r <= 0:
                            if self.wrap:
                                self.r = len(self.items) - 1
                                self.play_click()
                                self.play_wrap()
                            else:
                                self.r = 0
                                self.play_edge()
                        else:
                            self.play_click()
                            self.r -= 1
                        self.announce_item(self.r)
                    if event.key == pygame.K_RIGHT and self.leftright:
                        if self.r >= len(self.items) - 1:
                            if self.wrap:
                                self.r = 0
                                self.play_click()
                                self.play_wrap()
                            else:
                                self.r = len(self.items) - 1
                                self.play_edge()
                        else:
                            self.play_click()
                            self.r += 1
                        self.announce_item(self.r)
                    if event.key == pygame.K_HOME and self.homeend:
                        self.play_click()
                        self.r = 0
                        self.announce_item(self.r)
                    if event.key == pygame.K_END and self.homeend:
                        self.play_click()
                        self.r = len(self.items) - 1
                        self.announce_item(self.r)
                    if (
                        event.key == pygame.K_RETURN
                        and self.r > -1
                        and self.r <= len(self.items) - 1
                    ):
                        self.play_enter()
                        return self.r
                    if event.key == pygame.K_ESCAPE:
                        self.play_escape()
                        return -1
        return -1

    def fade_music(self, fadetime):
        if self.music == None:
            return
        while True:
            pygame.display.update()
            clock.tick(60)
            if self.mfadetimer.elapsed > fadetime:
                self.mfadetimer.restart()
            if self.music.handle.volume > -50:
                self.music.handle.volume -= 1
            if self.music.handle.volume <= -50:
                break
        p.destroy_sound(self.music)
