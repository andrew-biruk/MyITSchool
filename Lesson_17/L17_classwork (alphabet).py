from string import ascii_lowercase


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))


class EngAlphabet(Alphabet):
    __letters_num = len(ascii_lowercase)

    def __init__(self):
        super().__init__("En", ascii_lowercase)

    def is_en_letter(self, letter):
        return letter.lower() in self.letters

    @classmethod
    def letters_num(cls):
        return cls.__letters_num

    @staticmethod
    def example():
        return "London is the capital of GB."


ea = EngAlphabet()
ea.print()
print(ea.letters_num())
print(ea.is_en_letter("g"))
print(ea.is_en_letter("ц"))
print(EngAlphabet.example())
