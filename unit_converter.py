

type_of_unit_being_entered = input("Enter type of unit being converted ie celsius, farenheit")
type_of_unit_being_converted_to = input("Enter type of unit to convert to")
value_of_input = input("Enter value")

if type_of_unit_being_entered == "celsius" and type_of_unit_being_converted_to == "farenheit":
    value_of_output = (float(value_of_input) * 1.8) +32
if type_of_unit_being_entered == "farenheit" and type_of_unit_being_converted_to == "celsius":
    value_of_output = (float(value_of_input) -32) * 0.5556

print (value_of_output)
