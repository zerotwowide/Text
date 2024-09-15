class Book:
    def __init__(self, ISBN, name):
        self.ISBN = ISBN
        self.name = name
    def __str__(self):
        return f"{self.name}-{self.ISBN}"