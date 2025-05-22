# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: May 19, 2025
# This is an Ohm's law calculator that gets the resistance, voltage ,and current, depending on what the user wants
# It uses different functions for each option
# It gets all the user input in the main


# Function to calculate current: I = V / R
def calculate_current(voltage, resistance):
    return voltage / resistance


# Function to calculate resistance: R = V / I
def calculate_resistance(voltage, current):
    return voltage / current


# Function to calculate voltage: V = I * R
def calculate_voltage(current, resistance):
    return current * resistance


# Main program
def main():
    # Display the first message of the program and the calculation possible
    print("Welcome to the Ohm’s Law Calculator!")
    print("1: Calculate Current (I = V / R)")
    print("2: Calculate Resistance (R = V / I)")
    print("3: Calculate Voltage (V = I x R)")

    # While loop for not stopping the program until it get the correct numbers
    while True:
        # Get the choice of which calculation to do from the user as a string
        choice_str = input("Choose an option (1, 2, or 3): ")
        # Try catch for any Invalid input that is not 1,2,3
        try:
            # Type cast the choice_str to an integer
            choice = int(choice_str)
        except ValueError:
            print(f"Invalid input! Please enter 1, 2, or 3.\n")
            # If this input is Invalid, the code will continue
            continue

        # If statement if the user chooses option one
        if choice == 1:
            # Get the voltage and resistance from the user as strings
            voltage_str = input("Enter the voltage (V): ")
            resistance_str = input("Enter the resistance (R): ")
            # Try catch if the input is not a float
            try:
                # Type cast voltage and resistance to a float
                voltage = float(voltage_str)
                resistance = float(resistance_str)
            except ValueError:
                print(f"Invalid input! Please enter numeric values.\n")
                # Continue, it will go back to the beginning of the while true
                continue

            # If statement if the resistance or voltage is less than or equal to zero
            # Resistance and voltage can not be less than 0 or 0
            if resistance <= 0 or voltage < 0:
                if resistance == 0:
                    print(f"Error: Resistance cannot be zero.\n")
                else:
                    print(f"Error: Resistance and Voltage must be positive numbers.\n")
                    # continue, meaning the code doesn't break yet
                continue

            # call the calculate current function and stor it in the variable current
            current = calculate_current(voltage, resistance)
            # Display the current
            print(f"The current (I) is: {current:.2f} Amps")

        # elif statement if the user picks option two
        elif choice == 2:
            # Get the user voltage and current
            voltage_str = input("Enter the voltage (V): ")
            current_str = input("Enter the current (I): ")
            # try catch for type casting voltage and current to a float
            try:
                voltage = float(voltage_str)
                current = float(current_str)
            except ValueError:
                print(f"Invalid input! Please enter numeric values.\n")
                # Continue so it goes back to the while true
                continue

            # if statement of the current and voltage is not less than 0 or 0
            if current <= 0 or voltage < 0:
                # Nest if, if the user enters 0
                if current == 0:
                    print(f"Error: Current cannot be zero.\n")
                # Else for any other input that is less than zero
                else:
                    print(f"Error: Current and Voltage must be positive numbers.\n")
                # Continue so the code goes back to while true if this is true
                continue

            # Call the function to calculate resistance, and store it in a variable called resistance
            resistance = calculate_resistance(voltage, current)
            # Display the resistance
            print(f"The resistance (R) is: {resistance:.2f} Ohms")

        # elif statement if the user chooses option 3
        elif choice == 3:
            # Get the current and resistance as a string
            current_str = input("Enter the current (I): ")
            resistance_str = input("Enter the resistance (R): ")
            # Try catch to type cast current and resistance to a float
            try:
                current = float(current_str)
                resistance = float(resistance_str)
            except ValueError:
                print(f"Invalid input! Please enter numeric values.\n")
                # Continue, so the code goes back to the while true
                continue

            # If the current or resistance is less than 0 or equal to 0
            # Display an Invalid error, and continue
            if current <= 0 or resistance <= 0:
                print(f"Error: Current and Resistance must be positive and non-zero.\n")
                continue

            # Call the calculate voltage function and store it in a variable called voltage
            voltage = calculate_voltage(current, resistance)
            # Display the voltage
            print(f"The voltage (V) is: {voltage:.2f} Volts")

        # else statement if the user doesn't pick 1,2, or 3
        else:
            print(f"Please choose a valid option: 1, 2, or 3.\n")
            # continue so it asks again
            continue

        # Break the loop if a valid calculation is done
        break


if __name__ == "__main__":
    main()
