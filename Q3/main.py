from animal import Animal
from dog import Dog
from cat import Cat

def main():
    # יצירת אובייקטים ללא פרמטרים מיותרים
    animals = [Dog(), Cat()]

    for animal in animals:
        # שימוש ב-isinstance כפי שנדרש במטלה
        if isinstance(animal, Animal):
            print(animal.speak())

if __name__ == "__main__":
    main()