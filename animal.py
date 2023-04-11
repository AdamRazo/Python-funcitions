class Animal:
    def speak(self):
        print('the animal makes a sound')

    class Dog(Animal):
        def speak(self):
            print('Bark, Bark')

    animal = Animal()
    fido = Dog()

    animal.speak()
    fido.speak()