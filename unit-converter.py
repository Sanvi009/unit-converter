def get_valid_number(allow_negative=True):
    while True:
        try:
            num = float(input("Enter the number: "))
            if not allow_negative and num < 0:
                print("⚠️ Invalid input! Please enter a non-negative number.")
            else:
                return num
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")


def converter_menu(title, options, conversions):
    print(f"\n{title}")
    for key, value in options.items():
        print(f"{key} : {value}")
    print(f"{len(options) + 1} : Home")

    while True:
        try:
            ask = int(input(f"What do you want to convert? (1-{len(options) + 1}): "))
            if 1 <= ask <= len(options):
                num = get_valid_number()
                print(conversions[ask](num))
            elif ask == len(options) + 1:
                return  
            else:
                print(f"❌ Please enter a valid number between 1-{len(options) + 1}.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")


def length():
    options = {
        1: "Centimeter to Meter",
        2: "Meter to Feet",
        3: "Feet to Kilometer",
        4: "Kilometer to Miles",
        5: "Miles to Kilometer"
    }
    conversions = {
        1: lambda num: f"{num} cm = {num / 100} meters",
        2: lambda num: f"{num} meters = {num * 3.28084} feet",
        3: lambda num: f"{num} feet = {num / 3280.84} kilometers",
        4: lambda num: f"{num} km = {num / 1.60934} miles",
        5: lambda num: f"{num} miles = {num * 1.60934} kilometers"
    }
    converter_menu("📏 Length Converter", options, conversions)


def weight():
    options = {
        1: "Gram to Kilogram",
        2: "Kilogram to Pound",
        3: "Pound to Kilogram",
        4: "Kilogram to Gram"
    }
    conversions = {
        1: lambda num: f"{num} g = {num / 1000} kg",
        2: lambda num: f"{num} kg = {num * 2.20462} pounds",
        3: lambda num: f"{num} lbs = {num * 0.453592} kg",
        4: lambda num: f"{num} kg = {num * 1000} g"
    }
    converter_menu("⚖️ Weight Converter", options, conversions)


def temperature():
    options = {
        1: "Celsius to Fahrenheit",
        2: "Fahrenheit to Celsius",
        3: "Celsius to Kelvin",
        4: "Kelvin to Celsius",
        5: "Fahrenheit to Kelvin",
        6: "Kelvin to Fahrenheit"
    }
    conversions = {
        1: lambda num: f"{num}°C = {(num * 9/5) + 32}°F",
        2: lambda num: f"{num}°F = {(num - 32) * 5/9}°C",
        3: lambda num: f"{num}°C = {num + 273.15} K",
        4: lambda num: f"{num} K = {num - 273.15}°C",
        5: lambda num: f"{num}°F = {(num - 32) * 5/9 + 273.15} K",
        6: lambda num: f"{num} K = {(num - 273.15) * 9/5 + 32}°F"
    }
    converter_menu("🌡️ Temperature Converter", options, conversions)


def time_converter():
    options = {
        1: "Seconds to Minutes",
        2: "Minutes to Hours",
        3: "Hours to Days",
        4: "Days to Weeks",
        5: "Weeks to Months (Approx)",
        6: "Months to Years (Approx)",
        7: "Years to Days"
    }
    conversions = {
        1: lambda num: f"{num} sec = {num / 60:.2f} min",
        2: lambda num: f"{num} min = {num / 60:.2f} hours",
        3: lambda num: f"{num} hours = {num / 24:.2f} days",
        4: lambda num: f"{num} days = {num / 7:.2f} weeks",
        5: lambda num: f"{num} weeks = {num / 4.345:.2f} months",
        6: lambda num: f"{num} months = {num / 12:.2f} years",
        7: lambda num: f"{num} years = {num * 365:.2f} days"
    }
    converter_menu("⏳ Time Converter", options, conversions)


def home():
    while True:
        print("\n🏠 Welcome to Unit Converter")
        print("1 : Length")
        print("2 : Weight")
        print("3 : Temperature")
        print("4 : Time")
        print("5 : Exit")

        try:
            ask = int(input("Choose a category (1-5): "))
            if ask == 1:
                length()
            elif ask == 2:
                weight()
            elif ask == 3:
                temperature()
            elif ask == 4:
                time_converter()
            elif ask == 5:
                print("👋 Exiting... Goodbye!")
                break  
            else:
                print("❌ Please enter a valid number between 1-5.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")


home()