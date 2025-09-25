# Distance Converter
# Convert between kilometers, meters, and centimeters

def km_to_m(km):
    m = km * 1000
    print("km = ", m, "m")
    pass

def m_to_cm(m):
    cm = m * 100
    print("m = ", cm, "cm")
    pass

def cm_to_km(cm):
    km = cm / 100000
    print("cm = ", km, "km")
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
        km_to_m(km)
    elif choice == "2":
        m = float(input("Enter distance in meters: "))
        m_to_cm(m)
    elif choice == "3":
        cm = float(input("Enter distance in centimeters: "))
        cm_to_km(cm)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
