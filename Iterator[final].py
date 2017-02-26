class count_to:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index != len(self.numbers) - 1:
            self.index += 1
        else:
            self.index = 0
        return self.numbers[self.index]

if __name__ == "__main__":
    numbers = ["one", "two", "Free", "four", "five", "six", "seven", "eight", "nine", "\n"]
    num = int(input("Enter a digit: "))
    count = count_to(numbers)

    print(end=' ')
    for i in range(num):
        print(count.__next__(), end=' ')
