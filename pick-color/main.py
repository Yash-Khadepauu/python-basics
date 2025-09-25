# Color Picker Simulator
# Picks a random color from a predefined list

import random

def get_random_color():
    colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"]
    return random.choice(colors)
    pass

def main():
    print("Random Color Picker")

    try:
        while True:
            input("Press Enter to pick a color (or Ctrl+C to quit)...")
            color = get_random_color()
            print("Your color is: ", color)
    except KeyboardInterrupt:
        print("Stopped.")

if __name__ == "__main__":
    main()
