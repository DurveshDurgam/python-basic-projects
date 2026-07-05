# ask if user wants to convert weight from kilograms to pounds or vice versa, then
# take input from the user for weight in kilogram/pounds 
# convert it to the other unit.
#  Print the result of the conversion.

weight_input = input("Enter your weight '): ").strip().lower()
unit = input("Is this in kilograms or pounds? (kg/lb): ").strip().lower()

if unit == "kg":
    weight_in_pounds = float(weight_input) * 2.20462
    print(f"{weight_input} kilograms is equal to {weight_in_pounds:.2f} pounds.")
elif unit == "lb":
    weight_in_kilograms = float(weight_input) / 2.20462
    print(f"{weight_input} pounds is equal to {weight_in_kilograms:.2f} kilograms.")
else:
    print("Invalid unit. Please enter 'kg' for kilograms or 'lb' for pounds.")