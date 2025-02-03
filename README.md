Unit Converter
    This is a Python program for converting units between different categories: Length, Weight, Temperature, and Time.

Code Description
    The program provides a menu with four conversion categories:

  Length
  Weight
  Temperature
  Time
Functions:
  get_valid_number(allow_negative=True): Asks the user to input a number and checks if it’s valid. It can allow or disallow negative numbers based on the input setting.

  converter_menu(title, options, conversions): Displays a menu with conversion options for the selected category, takes the user's choice, and shows the conversion result.

  length(): Handles unit conversions related to length (e.g., cm to meters, meters to feet).

  weight(): Handles unit conversions related to weight (e.g., grams to kilograms, kilograms to pounds).

  temperature(): Handles unit conversions related to temperature (e.g., Celsius to Fahrenheit, Fahrenheit to Celsius).

  time_converter(): Handles unit conversions related to time (e.g., seconds to minutes, minutes to hours).

  home(): Displays the main menu and allows the user to choose a category or exit the program.

Program Flow:
  The user starts at the main menu and selects a category (Length, Weight, Temperature, or Time).
  The program shows conversion options for the chosen category.
  The user selects a conversion, inputs a number, and gets the result.
  The user can return to the main menu or exit.
Error Handling:
  The program checks if the user inputs a valid number.
  It ensures the conversion choice is within the valid options.
  This is a brief description that explains the core functions and flow of the program.








