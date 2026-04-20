import numpy as np

class PragatiFlowAgent:
    """
    This is the Brain of the traffic signal. 
    It learns by getting 'rewards' for good choices and 'penalties' for bad ones.
    """
    def __init__(self):
        # These are the 'Weights' - how much the AI cares about each problem.
        self.w_wait = 0.5        # Cares about people waiting
        self.w_emergency = 1.0   # Cares EXTRA about ambulances
        self.w_pollution = 0.2   # Cares about smoke/emissions

    def act(self, state):
        """
        The AI looks at the road (the state) and decides: 
        0 = Stay Red, 1 = Turn Green
        """
        # If an ambulance is detected, the AI will almost always choose 1 (Green)
        if state['ambulance_present']:
            return 1 
        
        # Otherwise, it would usually pick based on where the most cars are
        return 0 if state['queue_length'] < 5 else 1

    def compute_reward(self, state, action):
        """
        This tells the AI if it did a good job.
        Negative numbers are 'ouch' (penalties).
        """
        penalty = 0
        
        # Penalty 1: Making cars wait too long
        penalty += state['wait_time'] * self.w_wait
        
        # Penalty 2: The biggest 'Ouch' - stopping an ambulance!
        if state['ambulance_present'] and action == 0:
            penalty += 1000  # Massive penalty for blocking an ambulance
            
        # We return a negative value because the AI wants to get as close to 0 as possible
        return -penalty

print("Agent logic initialized. Ready to connect to the simulation!")