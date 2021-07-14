from inverter import Inverter

ascii_characters = list()

for i in range(0, 128):
    ascii_characters.append(chr(i))

input_str = input("Enter your input text: ")

inverter = Inverter(input_str, ascii_characters)
output_str = inverter.invert()

for i in output_str:
    print(ascii_characters.index(i))