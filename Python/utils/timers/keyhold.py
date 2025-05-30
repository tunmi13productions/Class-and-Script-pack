from pygame_timer import Timer
class key_hold:
    def __init__(self, key_code, sett1, sett2):
        self.key_code = key_code
        self.sett1 = sett1  # Initial delay before repeating (ms)
        self.sett2 = sett2  # Repeat interval after initial delay (ms)
        self.repeat_time = sett1
        self.key_timer = Timer()
        self.key_flag = 0
        
    def pressing(self, keys_pressed):
        """
        Check if key should trigger based on hold timing
        keys_pressed: pygame.key.get_pressed() result
        """
        if not keys_pressed[self.key_code]:
            self.repeat_time = 0
            self.key_timer.restart()
            self.key_flag = 0
            return False
            
        if self.key_timer.elapsed >= self.repeat_time:
            self.key_timer.restart()
            
            if self.key_flag == 0:
                self.key_flag = 1
                self.repeat_time = self.sett1
                self.key_timer.restart()
                return True
                
            if self.key_flag == 1:
                self.key_flag = 2
                self.key_timer.restart()
                self.repeat_time = self.sett2
                return False
                
            if self.key_flag == 2:
                self.key_timer.restart()
                return True
                
            return True
        return False

