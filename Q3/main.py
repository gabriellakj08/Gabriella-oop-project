from animal import Animal
from dog import Dog
from cat import Cat

def main():
    animals = [Dog(), Cat()]

    for animal in animals:
        if isinstance(animal, Animal):
            print(animal.speak())

if __name__ == "__main__":

    main()
