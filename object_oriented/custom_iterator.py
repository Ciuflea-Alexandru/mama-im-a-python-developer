# create a class which acts as an iterator that counts backwards from a starting number to zero

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """Returns the next value or signals the end of iteration."""
        if self.current < 0:
            raise StopIteration
        
        value = self.current
        self.current -= 1
        return value

# Example Usage
if __name__ == "__main__":
    print("Starting countdown:")
    for number in Countdown(5):
        print(number, end=" ")
        
    print("\n\nManual iteration example:")
    iterator = Countdown(3)
    print(next(iterator))  # 3
    print(next(iterator))  # 2