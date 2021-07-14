from inverter import Inverter

lowercase_letters = list()
uppercase_letters = list()
numbers = list()
symbols = list()
uppercase_locations = list()
preserved_locations = dict()

for i in range(0, 128):
    if i in range(48, 58):
        numbers.append(chr(i))
    elif i in range(65, 91):
        uppercase_letters.append(chr(i))
    elif i in range(97, 123):
        lowercase_letters.append(chr(i))
    else:
        symbols.append(chr(i))

input_str = input("Enter your input text: ")

# preprocessing
for i in range(len(input_str)):
    if input_str[i] in symbols or input_str[i] in numbers:
        preserved_locations[i] = input_str[i]

    elif input_str[i] in uppercase_letters:
        uppercase_locations.append(i)

for symbol in preserved_locations.values():
    input_str = input_str.replace(symbol, '')

input_str = input_str.lower()

inverter = Inverter(input_str, lowercase_letters)
output_str = inverter.invert()

output_str_list = [character for character in output_str]

for index in preserved_locations.keys():
    output_str_list.insert(index, preserved_locations[index])

for index in uppercase_locations:
    output_str_list[index] = output_str_list[index].upper()

output_str = ""
print(output_str.join(output_str_list))
