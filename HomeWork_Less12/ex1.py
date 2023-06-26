def convert_temperature(temperature: float, unit: str):
    if unit == "C":
        converted_temperature = (temperature * 9 / 5) + 32
        return converted_temperature, "F"
    elif unit == "F":
        converted_temperature = (temperature - 32) * 5 / 9
        return converted_temperature, "C"
    else:
        return "Invalid unit", ""

temperature_input = float(input("Enter the temperature: "))
unit_input = input("Enter the current unit (C/F): ")

converted_temperature, converted_unit = convert_temperature(temperature_input, unit_input)
if converted_unit != "":
    print("Converted temperature:", converted_temperature, converted_unit)
else:
    print(converted_temperature)
