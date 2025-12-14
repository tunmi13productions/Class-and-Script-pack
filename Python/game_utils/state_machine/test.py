from state_machine import StateMachine, State

# Example state classes
class MenuState(State):
    def __init__(self):
        super().__init__("menu")
        
    def on_enter(self, state_machine):
        print("Entering menu state - showing options")
        
    def on_exit(self, state_machine):
        print("Exiting menu state")


class GameplayState(State):
    def __init__(self):
        super().__init__("gameplay")
        self.score = 0
        self.game_time = 0
        self.enemy_spawn_timer = 0
        
    def on_enter(self, state_machine):
        print("Entering gameplay state - starting game")
        
    def on_exit(self, state_machine):
        print(f"Exiting gameplay state - final score: {self.score}")
        
    def on_pause(self, state_machine):
        super().on_pause(state_machine)
        print(f"Gameplay paused - background systems continue")
        
    def on_resume(self, state_machine):
        super().on_resume(state_machine)
        print(f"Gameplay resumed - back to the action!")
        
    def on_update(self, state_machine):
        # Main game logic (only when active)
        self.score += 1
        self.game_time += 1
        self.enemy_spawn_timer += 1
        print(f"Game active - Score: {self.score}, Time: {self.game_time}")
        
    def on_background_update(self, state_machine):
        # Background processing (when paused/overlaid)
        self.game_time += 1  # Time always advances
        self.enemy_spawn_timer += 1
        
        # Maybe spawn enemies less frequently in background
        if self.enemy_spawn_timer % 5 == 0:
            print(f"Background: Enemy spawned at time {self.game_time}")
        
        # Other background tasks like autosave, network sync, etc.
        if self.game_time % 10 == 0:
            print(f"Background: Autosave at time {self.game_time}")


class PauseMenuState(State):
    def __init__(self):
        super().__init__("pause_menu")
        
    def on_enter(self, state_machine):
        print("Pause menu opened - game paused")
        
    def on_exit(self, state_machine):
        print("Closing pause menu")


class SettingsState(State):
    def __init__(self):
        super().__init__("settings")
        
    def on_enter(self, state_machine):
        print("Entering settings menu")
        
    def on_exit(self, state_machine):
        print("Saving settings and exiting")


# Example usage
if __name__ == "__main__":
    # Create state instances
    menu = MenuState()
    gameplay = GameplayState()
    pause_menu = PauseMenuState()
    settings = SettingsState()
    
    # Create state machine
    sm = StateMachine()
    
    # Add states to the machine
    sm.add_state(menu)
    sm.add_state(gameplay)
    sm.add_state(pause_menu)
    sm.add_state(settings)
    
    print("=== Pause vs Exit State Machine Demo ===")
    
    # Start in menu
    sm.change_state(menu)
    
    # Go to gameplay
    sm.change_state("gameplay")
    sm.update()  # Score: 1
    sm.update()  # Score: 2
    
    print("\n--- Opening settings as overlay (game continues in background) ---")
    # Overlay settings - gameplay continues in background
    sm.overlay_state(settings)
    print(f"Paused states: {sm.get_paused_states()}")
    
    # Update - settings is active, gameplay runs background updates
    sm.update()  # Background update for gameplay
    sm.update()  # Another background update
    
    # Close settings overlay
    sm.close_overlay()
    sm.update()  # Resume normal gameplay
    
    print(f"\n--- Testing different update modes ---")
    sm.overlay_state(pause_menu)
    
    print("Background only update:")
    sm.update_background_only()
    
    print("Foreground only update:")
    sm.update_foreground_only()
    
    print("Full update (background + foreground):")
    sm.update()
    
    sm.close_overlay()
    
    print(f"\nFinal state: {sm.get_current_state_name()}")
    print(f"Final score: {gameplay.score}")
    print(f"Total game time: {gameplay.game_time}")
    print(f"Enemy spawn timer: {gameplay.enemy_spawn_timer}")