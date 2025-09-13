# Digital Clock
# Display current time in HH:MM:SS format

from datetime import datetime
import time

def get_current_time():
    # TODO: Return the current system time in formatted string
    pass

def main():
    print("Digital Clock - Press Ctrl+C to stop\n")
    
    try:
        while True:
            # Get current time and display it
            # Use time.sleep(1) to update every second
            pass
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    main()
