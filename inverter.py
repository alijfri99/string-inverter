class Inverter:
    def __init__(self, input_str, lowercase_letters):
        self.input_str = input_str
        self.lowercase_letters = lowercase_letters

    def invert(self):
        output_str = self.input_str[0]
        for i in range(1, len(self.input_str)):
            distance = self.lowercase_letters.index(self.input_str[i]) \
                       - self.lowercase_letters.index(self.input_str[i - 1])
            char_location = (self.lowercase_letters.index(output_str[i - 1]) - distance) % 26
            output_str += self.lowercase_letters[char_location]

        return output_str
