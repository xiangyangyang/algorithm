import random

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    tricks = []
    def add_trick(self,trick):
        self.tricks.append(trick)

if __name__ == '__main__':
    d = Dog("fido")
    e = Dog("Buddy")
    d.add_trick("roll over")
    e.add_trick("play dead")
    print(d.tricks)
    print(e.tricks)

    def random_index(nums, target):
        indices = [i for i, num in enumerate(nums) if num == target]
        if indices:
            return random.choice(indices)
        else:
            return -1




