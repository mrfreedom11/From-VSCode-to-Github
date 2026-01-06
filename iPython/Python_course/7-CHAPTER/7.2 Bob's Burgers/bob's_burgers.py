class Restaurant:
    def __init__(self, name, place, gpa, delivery):
        self.name = name
        self.place = place
        self.gpa = gpa
        self.delivery = delivery

# objectlar:
bobs = Restaurant("Bob's Burgers", "American Diner", 4.7, False)
abrors = Restaurant("Somsachalar", "Ko'krak", 5.1, False)
azizs = Restaurant("Fast-Ko'kraklar", "America", 1.5, True)

print(vars(bobs))
print(vars(abrors))
print(vars(azizs))

