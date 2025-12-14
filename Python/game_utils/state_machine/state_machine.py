class State:
    """Base class for all states."""
    
    def __init__(self, name):
        self.name = name
        self.is_paused = False
        
    def on_enter(self, state_machine):
        """Called when entering this state."""
        pass
        
    def on_exit(self, state_machine):
        """Called when fully exiting this state."""
        pass
        
    def on_pause(self, state_machine):
        """Called when this state is paused (but stays active in background)."""
        self.is_paused = True
        
    def on_resume(self, state_machine):
        """Called when this state is resumed from pause."""
        self.is_paused = False
        
    def on_update(self, state_machine):
        """Called during state updates (only if not paused)."""
        pass
        
    def on_background_update(self, state_machine):
        """Called during background updates (when state is paused/overlaid)."""
        pass
        
    def __str__(self):
        return self.name


class StateMachine:
    def __init__(self, initial_state=None):
        """
        Initialize the state machine.
        
        Args:
            initial_state: The starting state (State object or string)
        """
        self.states = {}  # Dictionary to hold state objects by name
        self.current_state = None
        self.state_stack = []  # Stack for push/pop operations
        self.paused_states = []  # Stack of paused states that continue running
        
        if initial_state:
            if isinstance(initial_state, State):
                self.add_state(initial_state)
                self.current_state = initial_state
            else:
                # If string is passed, we'll set it later when state is added
                self._initial_state_name = initial_state
        
    def add_state(self, state):
        """
        Add a state to the machine.
        
        Args:
            state: State object to add
        """
        if not isinstance(state, State):
            raise TypeError("State must be an instance of State class")
            
        self.states[state.name] = state
        
        # Set initial state if it was specified as string
        if hasattr(self, '_initial_state_name') and state.name == self._initial_state_name:
            self.current_state = state
            delattr(self, '_initial_state_name')
        
    def change_state(self, new_state):
        """
        Change to a new state, fully exiting the current state.
        
        Args:
            new_state: State object or string name of state to change to
        """
        # Handle both State objects and string names
        if isinstance(new_state, str):
            if new_state not in self.states:
                raise ValueError(f"State '{new_state}' not found")
            new_state = self.states[new_state]
        elif isinstance(new_state, State):
            if new_state.name not in self.states:
                raise ValueError(f"State '{new_state.name}' not added to state machine")
        else:
            raise TypeError("new_state must be State object or string")
            
        # Call exit callback for current state
        if self.current_state:
            self.current_state.on_exit(self)
            
        # Change state
        old_state = self.current_state
        self.current_state = new_state
        
        # Call enter callback for new state
        self.current_state.on_enter(self)
        
        old_name = old_state.name if old_state else "None"
        print(f"State changed from '{old_name}' to '{new_state.name}'")
        
    def push_state(self, new_state):
        """
        Push current state onto stack and change to new state (exits current state).
        
        Args:
            new_state: State object or string name of state to push to
        """
        if self.current_state:
            self.state_stack.append(self.current_state)
        self.change_state(new_state)
        
    def overlay_state(self, new_state):
        """
        Overlay a new state while keeping current state running in background.
        Current state is paused but continues to exist.
        
        Args:
            new_state: State object or string name of state to overlay
        """
        # Handle both State objects and string names
        if isinstance(new_state, str):
            if new_state not in self.states:
                raise ValueError(f"State '{new_state}' not found")
            new_state = self.states[new_state]
        elif isinstance(new_state, State):
            if new_state.name not in self.states:
                raise ValueError(f"State '{new_state.name}' not added to state machine")
        else:
            raise TypeError("new_state must be State object or string")
        
        # Pause current state and add to paused stack
        if self.current_state:
            self.current_state.on_pause(self)
            self.paused_states.append(self.current_state)
            print(f"Pausing '{self.current_state.name}' state")
            
        # Change to new state
        old_state = self.current_state
        self.current_state = new_state
        self.current_state.on_enter(self)
        
        old_name = old_state.name if old_state else "None"
        print(f"Overlaying '{new_state.name}' over '{old_name}'")
        
    def pop_state(self):
        """
        Pop previous state from stack and return to it.
        Returns True if successful, False if stack is empty.
        """
        if not self.state_stack:
            print("No states to pop - stack is empty")
            return False
            
        previous_state = self.state_stack.pop()
        self.change_state(previous_state)
        return True
        
    def close_overlay(self):
        """
        Close current overlay state and resume the paused state underneath.
        Returns True if successful, False if no paused states.
        """
        if not self.paused_states:
            print("No paused states to resume")
            return False
            
        # Exit current overlay state
        if self.current_state:
            self.current_state.on_exit(self)
            print(f"Closing overlay '{self.current_state.name}'")
            
        # Resume paused state
        self.current_state = self.paused_states.pop()
        self.current_state.on_resume(self)
        print(f"Resuming '{self.current_state.name}' state")
        return True
        
    def update(self):
        """
        Update the current state and run background updates for paused states.
        """
        # Run background updates for paused states
        for state in self.paused_states:
            state.on_background_update(self)
            
        # Update current active state
        if self.current_state and not self.current_state.is_paused:
            self.current_state.on_update(self)
            
    def update_foreground_only(self):
        """
        Update only the current active state, skip background processing.
        """
        if self.current_state and not self.current_state.is_paused:
            self.current_state.on_update(self)
            
    def update_background_only(self):
        """
        Update only the paused background states.
        """
        for state in self.paused_states:
            state.on_background_update(self)
            
    def update_all(self):
        """
        Update current state AND all paused states using their main update methods.
        (Use with caution - this treats paused states as if they're active)
        """
        # Update all paused states with their main update
        for state in self.paused_states:
            state.on_update(self)
            
        # Update current state
        if self.current_state:
            self.current_state.on_update(self)
            
    def get_current_state(self):
        """Return the current state object."""
        return self.current_state
        
    def get_current_state_name(self):
        """Return the name of the current state."""
        return self.current_state.name if self.current_state else None
        
    def get_paused_states(self):
        """Return list of paused state names."""
        return [state.name for state in self.paused_states]
        
    def get_stack_depth(self):
        """Return the number of states in the stack."""
        return len(self.state_stack)


