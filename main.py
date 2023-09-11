import time
from CounterGadget import *
from StopWatchController import * 

time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

mystopwatch=StopWatchController()

mystopwatch.run()
