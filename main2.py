from inverter import Inverter

ascii_characters = list()

for i in range(0, 127):
    ascii_characters.append(chr(i))

input_str = input("Enter your input text: ")

inverter = Inverter(input_str, ascii_characters)
output_str = inverter.invert()

print(output_str)