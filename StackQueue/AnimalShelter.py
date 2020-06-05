"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linkedlist data structure.
"""

class Animal:
    def __init__(self, typ):
        self.typ = typ
        self.time = 0

    def __str__(self):
        return self.typ

class Queue:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.time = 0

    def enqueue(self, animal):
        self.time += 1
        if animal.typ == "dog":
            animal.time = self.time
            self.dog_queue.append(animal)
        else:
            animal.time = self.time
            self.cat_queue.append(animal)

    def dequeue_dog(self):
        dog = self.dog_queue[0]
        del self.dog_queue[0]
        return dog

    def dequeue_cat(self):
        cat = self.cat_queue[0]
        del self.cat_queue[0]
        return cat

    def dequeue_any(self):
        if self.dog_queue[0].time < self.cat_queue[0].time:
            dog = self.dog_queue[0]
            del self.dog_queue[0]
            return dog
        else:
            cat = self.cat_queue[0]
            del self.cat_queue[0]
            return cat

    def __str__(self):
        return "dog: " + str([animal.typ for animal in self.dog_queue]) + "\n" + \
               "cat: " + str([animal.typ for animal in self.cat_queue])




if __name__ == '__main__':
    animal_queue = Queue()
    for i in range(10):
        if i%2 == 0:
            animal = Animal("dog")
        else:
            animal = Animal("cat")
        animal_queue.enqueue(animal)
    print(animal_queue)

    #
    print(animal_queue.dequeue_any())
    print(animal_queue.dequeue_any())
    print(animal_queue.dequeue_any())

    print(animal_queue)


