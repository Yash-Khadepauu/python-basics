# Digital Clock
# Display current time in HH:MM:SS format

from datetime import datetime
import time

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")
    pass

def main():
    print("Digital Clock - Press Ctrl+C to stop\n")
    
    try:
        while True:
            current_time = get_current_time()
            print("\r" + current_time, end="")
            time.sleep(1)
            pass
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    main()
