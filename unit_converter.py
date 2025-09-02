
def km_to_miles(km: float) -> float:
    return km * 0.621371

def miles_to_km(miles: float) -> float:
    return miles / 0.621371

def c_to_f(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

def f_to_c(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def main():
    print("🌍 Unit Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

    choice = input("Choose conversion (1-4): ").strip()

    try:
        if choice == '1':
            km = float(input("Enter kilometers: "))
            print(f"{km} km = {km_to_miles(km):.2f} miles")
        elif choice == '2':
            miles = float(input("Enter miles: "))
            print(f"{miles} miles = {miles_to_km(miles):.2f} km")
        elif choice == '3':
            c = float(input("Enter Celsius: "))
            print(f"{c}°C = {c_to_f(c):.2f}°F")
        elif choice == '4':
            f = float(input("Enter Fahrenheit: "))
            print(f"{f}°F = {f_to_c(f):.2f}°C")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("❌ Please enter a valid number.")


if __name__ == "__main__":
    main()
