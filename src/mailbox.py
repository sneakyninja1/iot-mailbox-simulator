import time 
import random 
import threading
from typing import Callable, Optional

class IOTMailbox: 
    def __intit__(self, interval_ms, signal_callback):
        self._interval_ms = interval_ms
        self._signal_callback = signal_callback
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._last_light_level = 1.0


    def start(self): 
        pass
    
    def stop(self): 
        pass

    def _monitor_loop(self):
        pass

    def _sample_light_level(self): 
        magnitude = random.random()

        if (self._sample_light_level >= 0):
            new_level = -magnitude
        else:
            new_level = magnitude
        
        self._sample_light_level = new_level
        return new_level
