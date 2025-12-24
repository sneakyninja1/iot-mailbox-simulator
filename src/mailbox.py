import time 
import random 
import threading
from typing import Callable, Optional

class IOTMailbox: 
    def __init__(self, interval_ms, signal_callback):
        self._interval_ms = interval_ms
        self._signal_callback = signal_callback
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._last_light_level = 1.0


    def start(self): 
        if self._running: 
            return
        
        self._running = True
        self._thread= threading.Thread(target=self._monitor_loop, daemon = True)
        self._thread.start()

    def stop(self) -> None: 
        if self._running == False:
            return 
    
        self._running = False

    def _monitor_loop(self):
        while self._running:
            light_level = self._sample_light_level()
            self._signal_callback(light_level)
            time.sleep(self._interval_ms / 1000)

    def _sample_light_level(self): 
        magnitude = random.random()

        if (self._last_light_level >= 0):
            new_level = -magnitude
        else:
            new_level = magnitude
        
        self._last_light_level = new_level
        return new_level
