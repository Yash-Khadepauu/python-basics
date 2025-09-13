# Distance Converter
# Convert between kilometers, meters, and centimeters

def km_to_m(km):
    # TODO: Convert kilometers to meters
    pass

def m_to_cm(m):
    # TODO: Convert meters to centimeters
    pass

def cm_to_km(cm):
    # TODO: Convert centimeters to kilometers
    pass

def main():
    print("Welcome to the Distance Converter!")
    print("Options:")
    print("1. Kilometers to Meters")
    print("2. Meters to Centimeters")
    print("3. Centimeters to Kilometers")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        # Call conversion function
    elif choice == "2":
        m = float(input("Enter distance in meters: "))
        # Call conversion function
    elif choice == "3":
        cm = float(input("Enter distance in centimeters: "))
        # Call conversion function
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
