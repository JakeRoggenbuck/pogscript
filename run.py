import argparse


def parser():
    parse = argparse.ArgumentParser()

    parse.add_argument("-i", "--infile", help="Input file name", required=True)
    return parse.parse_args()


class Inter:
    def __init__(self, content: str):
        self.content = content
        self.memory = []
        self.line = 0

    def log_error(self, message: str):
        print(f"ERROR: {message} on line {self.line}")
        exit(0)

    def safe_check_int(self, i: str):
        i = i.rstrip()
        if i.isnumeric():
            return int(i)
        else:
            self.log_error(f"Index '{i}' is not numeric")

    def safe_read_mem(self, i: str):
        i = self.safe_check_int(i)

        if len(self.memory) > i:
            return self.memory[i]
        else:
            self.log_error(f"Could not access memory address '{i}'")

    def get_int(self, i):
        return int(self.safe_read_mem(i))

    def get_str(self, i):
        return str(self.safe_read_mem(i))

    def int_duet(self, values):
        return self.get_int(values[1]), self.get_int(values[2])

    def str_duet(self, values):
        return self.get_str(values[1]), self.get_str(values[2])

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    def apply_to_mem(self, duet, f, values):
        out = f(*duet(values))
        self.memory.append(out)

    def single(self, bar, command, values):
        if command == "v":
            self.memory.append(bar[2:])

        elif command == "a":
            self.apply_to_mem(self.int_duet, self.add, values)

        elif command == "s":
            self.apply_to_mem(self.int_duet, self.sub, values)

        elif command == "m":
            self.apply_to_mem(self.int_duet, self.mul, values)

        elif command == "d":
            self.apply_to_mem(self.int_duet, self.div, values)

        elif command == "p":
            self.apply_to_mem(self.str_duet, self.add, values)

        elif command == "c":
            num = self.safe_read_mem(bar[2:])
            char = chr(self.safe_check_int(num))
            self.memory.append(char)

        elif command == "i":
            prompt = bar[2:]
            intake = input(prompt)
            self.memory.append(intake)

        elif command == "o":
            place = bar[2:]
            print(self.memory[int(place)])

    def run(self):
        self.content.replace('\n', '')
        new = self.content.replace(' ', '')
        codeslice = new.rsplit(">")

        for bar in codeslice:
            self.line += 1
            command = bar[0]
            values = bar.rsplit("{")

            self.single(bar, command, values)


def main():
    args = parser()
    with open(args.infile) as file:
        data = file.read()
        inter = Inter(data)

        inter.run()


if __name__ == "__main__":
    main()
