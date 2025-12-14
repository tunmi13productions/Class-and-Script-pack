import string
import pyperclip
import pygame
from timer import Timer
from accessible_output2.outputs.auto import *

speech = Auto()
pygame.init()
clock = pygame.time.Clock()

WHITELIST_ALL = [i for i in string.printable if not i == "\r" or i == "\n"]
WHITELIST_LETTERS = [i for i in string.ascii_letters]
WHITELIST_DIGITS = [i for i in string.digits]
WHITELIST_HEXDIGITS = [i for i in string.hexdigits]
WHITELIST_NEGDIGITS = WHITELIST_DIGITS + ["-"]
WHITELIST_FLOATDIGITS = WHITELIST_DIGITS + ["."]
WHITELIST_NEGFLOATDIGITS = WHITELIST_FLOATDIGITS + ["-"]

spoken_symbols = {
    "`": "grave accent",
    "~": "tilda",
    "!": "exclamation mark",
    "^": "caret",
    "(": "left paren",
    ")": "right paren",
    "_": "underscore",
    "-": "dash",
    "[": "left bracket",
    "]": "right bracket",
    "{": "left brace",
    "}": "right brace",
    "\\": "backslash",
    "|": "vertical bar",
    ";": "semicolon",
    ":": "colon",
    "'": "apostrophe",
    "\"": "quote",
    ",": "comma",
    "?": "question mark",
    "\r": "carriage return",
    "\n": "line feed",
    "\t": "tab",
}

def speak(text,interrupt = False):
	speech.speak(text,interrupt)

class VirtualInput:
    def __init__(self, message="", password=False, whitelist=None, value="", callback=None, hidden_message="Hidden"):
        """Initializes the virtual input for Scrybe compatibility
        Parameters:
                app: The Scrybe app instance
                message (str): The message to display
                password (bool): Whether this is a password field
                whitelist (list): List of allowed characters
                value (str): Initial text value
                callback (callable): Callback function
                hidden_message (str): Message to speak for hidden characters
        """
        self.message = message
        self.callback = callback
        self.input_break = False
        
        # Set up whitelist
        if whitelist is None:
            whitelist = [i for i in string.printable if not i == "\r" or i == "\n"]
        self.whitelisted_characters = whitelist
        
        # Text and cursor management
        self.current_string = value
        self._cursor = max(0, len(self.current_string) - 1) if self.current_string else 0
        
        # Display settings
        self.hidden = password
        self.password_message = hidden_message
        self.repeating_characters = True
        self.repeating_keys = True
        
        # Input settings
        self.read_only = False
        self.multi_line = False
        self.can_exit = True
        self.can_escape = True
        self.should_break = False
        self.maximum_message_length = -1
        
        # Key repeat management
        self._key_times = {}
        self.key_repeat_timer = Timer()
        self.initial_key_repeating_time = 500
        self.repeating_increment = 50

    def toggle_character_repetition(self):
        if self.repeating_characters == False:
            self.repeating_characters = True
            return True
        elif self.repeating_characters == True:
            self.repeating_characters = False
            return False

    @property
    def is_at_character_limit(self):
        if self.should_break:
            return True
        return (
            False
            if self.maximum_message_length == -1
            or len(self.current_string) < self.maximum_message_length
            else True
        )

    @property
    def current_text(self):
        return self.current_string

    @current_text.setter
    def current_text(self, text):
        self.current_string = str(text)
        self._cursor = max(0, len(self.current_string) - 1)
    
    @property
    def text(self):
        return self.current_string
    
    @text.setter
    def text(self, value):
        self.current_string = str(value)
        self._cursor = max(0, len(self.current_string) - 1)
    
    @property
    def charindex(self):
        return self._cursor
    
    @charindex.setter
    def charindex(self, value):
        self._cursor = max(0, min(value, len(self.current_string)))
    
    @property
    def allowed_characters(self):
        return self.whitelisted_characters
    
    @allowed_characters.setter
    def allowed_characters(self, value):
        self.whitelisted_characters = value

    def clear(self):
        """Resets the input. This can be called outside of the class, but run will also do this internally upon every call"""
        self.current_string = ""
        self._cursor = 0
        self._key_times = {}
        self.key_repeat_timer.restart()

    def move_in_string(self, value):
        """Moves in a string. Used when the user presses left and right arrow keys
        Parameters:
                value (int): The value by which the cursor will be moved
        """
        self._cursor += value
        if self._cursor < 0:
            self._cursor = 0
        elif self._cursor > len(self.current_string):
            self._cursor = len(self.current_string)

    def get_character(self):
        """Retrieves the character at the cursor's position
        Return Value:
                A single character if the cursor is in the bounds of the string and the string is not empty, empty string otherwise
        """
        return (
            ""
            if len(self.current_string) == 0 or self._cursor == len(self.current_string)
            else self.current_string[self._cursor]
        )

    def insert_character(self, character):
        """Inserts a character into the text
        Parameters:
                character (str): The character to be inserted
        """
        if len(character) == 0:
            return
        self.current_string = (
            self.current_string[: max(0, self._cursor)]
            + character
            + self.current_string[max(0, self._cursor) :]
            if self._cursor < len(self.current_string)
            else self.current_string + character
        )
        self._cursor += len(character)
        self.speak_character(character if len(character) <= 1024 else f"Inserted {len(character)} characters")

    def remove_character(self):
        """Removes a character from the string based upon the cursor's position"""
        if self._cursor == 0:
            return
        self.speak_character(self.current_string[self._cursor - 1])
        if self._cursor == len(self.current_string):
            self.current_string = self.current_string[:-1]
        else:
            self.current_string = (
                self.current_string[: self._cursor - 1]
                + self.current_string[self._cursor :]
            )
        self._cursor -= 1
    def next_line(self):
        if len(self.current_string) == 0:
            return
        if len(self.current_string.splitlines()) == 1:
            speak(self.current_string)
            return
        if self._cursor < 0 or self._cursor >= len(self.current_string):
            return
        for counter in range(self._cursor, len(self.current_string)):
            if self.current_string[counter] != "\n":
                continue
            if self.current_string[counter] == "\n":
                self._cursor = counter + 1
                speak(speak_line(self._cursor))
                break
    def bottom_line(self):
        if len(self.current_string) == 0:
            return
        if self._cursor < 0 or self._cursor >= len(self.current_string):
            return
        for counter in range(self._cursor, len(self.current_string)):
            if self.current_string[counter] != "\n":
                continue
            if self.current_string[counter] == "\n":
                self._cursor = counter - 1
                self.speak_character(self.current_string[self._cursor])
                break
        if counter == len(self.current_string) - 1:
            self._cursor = len(self.current_string)
            speak("Blank")
    
    def prev_line(self):
        found_end = False
        if len(self.current_string) == 0:
            return
        if len(self.current_string.splitlines()) == 1:
            speak(self.current_string)
            return
        if self._cursor <= 0:
            return
        for counter in range(self._cursor, -1, -1):
            if counter == len(self.current_string):
                continue
            if counter > len(self.current_string):
                break
            if self.current_string[counter] != "\n":
                continue
            if self.current_string[counter] == "\n":
                if not found_end:
                    end = counter - 1
                    found_end = True
                else:
                    self._cursor = counter + 1
                    speak(speak_line(self._cursor))
                    break
        if counter <= 0 or counter > len(self.current_string):
            self._cursor = 0
            speak(speak_line(self._cursor))
    def top_line(self):
        if len(self.current_string) == 0:
            return
        if self._cursor <= 0:
            return
        if self._cursor > len(self.current_string):
            return

        for counter in range(self._cursor, -1, -1):
            if counter == len(self.current_string):
                continue
            if self.current_string[counter] != "\n":
                continue
            if self.current_string[counter] == "\n":
                self._cursor = counter + 1
                try:
                    self.speak_character(self.current_string[self._cursor])
                except:
                    self.speak_character(self.current_string[self._cursor-1])
                break
        if counter <= 0 or counter > len(self.current_string):
            self._cursor = 0
            self.speak_character(self.current_string[self._cursor])


    def speak_line(self, p):
        line = ""
        for i in range(p, len(self.current_string)):
            if self.current_string[i] != "\n":
                line += self.current_string[i]
            else:
                break
        return line

    def next_word(self):
        if len(self.current_string) == 0:
            return
        if self._cursor < 0 or self._cursor >= len(self.current_string):
            return
        for counter in range(self._cursor, len(self.current_string)):
            if self.current_string[counter] != " " and self.current_string[counter] != "\n":
                continue
            if self.current_string[counter] == " ":
                self._cursor = counter + 1
                speak(speak_word(self._cursor))
                break
            if self.current_string[counter] == "\n":
                self._cursor = counter + 1
                speak(speak_word(self._cursor))
                break
        if counter == len(self.current_string) - 1:
            self._cursor = len(self.current_string)
            speak("Blank")
    
    def prev_word(self):
        found_end = False
        if len(self.current_string) == 0:
            return
        if self._cursor <= 0:
            return
        for counter in range(self._cursor, -1, -1):
            if counter == len(self.current_string):
                continue
            if counter > len(self.current_string):
                break
            if self.current_string[counter] != " " and self.current_string[counter] != "\n":
                continue
            if self.current_string[counter] == " ":
                if not found_end:
                    end = counter - 1
                    found_end = True
                else:
                    self._cursor = counter + 1
                    speak(speak_word(self._cursor))
                    break
            if self.current_string[counter] == "\n":
                if not found_end:
                    end = counter - 1
                    found_end = True
                else:
                    self._cursor = counter + 1
                    speak(speak_word(self._cursor))
                    break
        if counter <= 0 or counter > len(self.current_string):
            self._cursor = 0
            speak(speak_word(self._cursor))

    def speak_word(self, p):
        word = ""
        for i in range(p, len(self.current_string)):
            if self.current_string[i] != " " and self.current_string[i] != "\n":
                word += self.current_string[i]
            else:
                break
        return word
    def speak_character(self, char, typing=False):
        """Outputs a given character respective the repeating_characters and password settings
        Parameters:
                character (str): The character to be outputted
        """
        if typing == True and not self.repeating_characters:
            return
        character = char
        if char == " ":
            character = "space"
        if char == "\r\n" or char == "\n":
            character = "new line"
        if spoken_symbols.get(char, None) is not None:
            character = spoken_symbols[char]
        if char.isupper():
            character = "cap" + char
        if self.hidden:
            speak(self.password_message)
        else:
            speak(character)

    def snap_to_top(self):
        """Snaps to the top of text (0 on the cursor position)"""
        self._cursor = 0
        self.speak_character(self.get_character())

    def snap_to_bottom(self):
        """Snaps to the bottom of text (len(self.current_string))"""
        self._cursor = len(self.current_string)
        self.speak_character(self.get_character())

    def toggle_input_to_letters(self):
        """Toggles the input to select only ascii letters"""
        self.whitelisted_characters = [a for a in string.ascii_letters]

    def toggle_input_to_digits(self, negative=False, decimal=False):
        """Toggles the input to select only ascii digits
        Parameters:
                negative (bool): Dictates whether the user can type in a dash (-)
                decimal (bool): Dictates whether a user can type in a period (.)
        """
        self.whitelisted_characters = [a for a in string.digits]
        if negative:
            self.whitelisted_characters.append("-")
        if decimal:
            self.whitelisted_characters.append(".")

    def toggle_input_to_all(self):
        """Toggles the input to accept all printable characters"""
        self.whitelisted_characters = [
            a for a in string.printable if not a == "\r" or a == "\n"
        ]

    def toggle_input_to_custom(self, characters):
        """Toggles the input to select user-provided input
        Parameters:
                characters (str): A string of characters the user wishes to allow the input to accept
        """
        self.whitelisted_characters = [a for a in characters]

    def run(self):
        """Retrieves user input
        Return Value:
                self.current_text (str): What the user entered
        """
        pygame.event.get()
        speak(self.message)
        self.clear()
        while not self.is_at_character_limit:
            pygame.display.update()
            clock.tick(60)
            if callable(self.callback):
                self.callback(self)
            if self.input_break:
                break
                
            keys = pygame.key.get_pressed()
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.KEYDOWN:
                    # Handle clipboard operations with Ctrl
                    if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
                        if event.key == pygame.K_c:
                            pyperclip.copy(self.current_string)
                            speak("text copied.")
                            continue
                        elif event.key == pygame.K_v and not self.read_only:
                            self.insert_character(pyperclip.paste())
                            speak("text pasted.")
                            continue
                    
                    # Handle Alt+C to clear all input
                    if (keys[pygame.K_LALT] or keys[pygame.K_RALT]) and event.key == pygame.K_c and not self.read_only:
                        self.current_string = ""
                        self._cursor = 0
                        speak("input cleared.")
                        continue
                    
                    if self.repeating_keys and event.key not in self._key_times:
                        self._key_times[event.key] = [
                            self.key_repeat_timer.elapsed
                            + self.initial_key_repeating_time,
                            event.unicode,
                        ]
                    if event.key == pygame.K_RETURN:
                        if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and self.multi_line and not self.read_only:
                            self.insert_character("\n")
                            #self._cursor += 1
                        else:
                            if self.can_exit:
                                pygame.event.get()  # Clear events
                                return self.current_text
                    elif self.can_escape and event.key == pygame.K_ESCAPE:
                        pygame.event.get()  # Clear events
                        return ""
                    elif event.key == pygame.K_BACKSPACE and not self.read_only:
                        self.remove_character()
                    elif event.key == pygame.K_TAB:
                        speak(self.message)
                    elif (event.key == pygame.K_UP or event.key == pygame.K_DOWN) and not self.multi_line:
                        speak(self.current_string)
                    elif event.key == pygame.K_UP and self.multi_line:
                        self.prev_line()
                    elif event.key == pygame.K_DOWN and self.multi_line:
                        self.next_line()

                    elif event.key == pygame.K_LEFT:
                        if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                            self.prev_word()
                        else:
                            self.move_in_string(-1)
                            self.speak_character(self.get_character())
                    elif event.key == pygame.K_RIGHT:
                        if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                            self.next_word()
                        else:
                            self.move_in_string(1)
                            self.speak_character(self.get_character())
                    elif event.key == pygame.K_HOME:
                        if self.multi_line and not keys[pygame.K_LCTRL] and not keys[pygame.K_RCTRL]: self.top_line()
                        elif self.multi_line and  (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]): self.top_line()
                        else: self.snap_to_top()
                    elif event.key == pygame.K_END:
                        if self.multi_line and not keys[pygame.K_LCTRL] and not keys[pygame.K_RCTRL]: self.bottom_line()
                        elif self.multi_line and  (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]): self.snap_to_bottom()
                        else: self.snap_to_bottom()
                    elif event.key == pygame.K_F2:
                        speak(
                            "Character repeat on"
                        ) if self.toggle_character_repetition() else speak(
                            "Character repeat off"
                        )
                elif event.type == pygame.TEXTINPUT and not self.read_only:
                    self.insert_character(event.text)
                elif event.type == pygame.KEYUP:
                    if event.key in self._key_times:
                        del self._key_times[event.key]
            for key in self._key_times:
                if self.key_repeat_timer.elapsed >= self._key_times[key][0]:
                    self._key_times[key][0] += self.repeating_increment
                    pygame.event.post(
                        pygame.event.Event(
                            pygame.KEYDOWN, key=key, unicode=self._key_times[key][1]
                        )
                    )
            pygame.time.wait(2)
        return self.current_text

    def get_integer_input(self, message, callback=None, negative=False, decimal=False):
        """Gets the input from the user and tries to convert it to integer. Will toggle itself to the previous input mode regardless of the result
        Parameters:
                message (str): See the run function
                callback (callable): See the run function
                negative (bool): See the toggle_input_to_digits function
                decimal (bool): See the toggle_input_to_digits function
        Return Value:
                A number upon success, None on failure
        """
        temp = "".join(self.whitelisted_characters)
        self.toggle_input_to_digits(negative, decimal)
        try:
            number = int(self.run())
        except ValueError:
            number = None
        self.toggle_input_to_custom(temp)
        return number

    def get_list_input(self, messages, callbacks=[]):
        """Allows the user to queue several messages in a row.
        Parameters:
                messages (list): The messages passed along to the run function as each prompt gets processed
                callbacks (list): Will be passed to the run function with the same indexes as the messages. If fewer callbacks are passed, None will be substituted
        """
        responses = []
        for i in range(len(messages)):
            self.message = messages[i]
            if i < len(callbacks) - 1:
                self.callback = callbacks[i]
            else:
                self.callback = None
            result = self.run()
            responses.append(result)
        return responses

    def get_integer_list_input(
        self, messages, callbacks=[], negative=False, decimal=False
    ):
        """Allows the user to queue several messages in a row requesting for integers. Will reset input to the previous mode regardless of success or failure
        Parameters:
                messages (list): See the  get_list_input function
                callbacks (list): See the get_list_input function
                negative (bool): See the toggle_input_to_digits function
                decimal (bool): See the toggle_input_to_digits function
        Return Value:
                A list of processed integers regardless of failure
        """
        # A bit repetitive, but must do it as we don't want to join strings every time we process an int
        temp = "".join(self.whitelisted_characters)
        self.toggle_input_to_digits(negative, decimal)
        results = []
        for i in range(len(messages)):
            try:
                self.message = messages[i]
                if i < len(callbacks) - 1:
                    self.callback = callbacks[i]
                else:
                    self.callback = None
                results.append(int(self.run()))
            except ValueError:
                break
        self.toggle_input_to_custom(temp)
        return results

