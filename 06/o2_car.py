class Car:

    brand = 'BMW'
    available_colors = ('Red', 'Blue', 'White', 'Black', 'Yellow')

    def __init__(self, model, max_speed, color='Grey', certified=False):
        self.model = model
        self.max_speed = max_speed
        self.color = color
        self.certified = certified
        self.actual_speed = 0

    def description(self):
        print("Car description:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Maximum speed: {self.max_speed}")
        print(f"Actual speed: {self.actual_speed}")
        print(f"Color: {self.color}")
        print(f"Certified: {self.certified}")
        print()

    def certification(self):
        if not self.certified:
            self.certified = True
            self.description()
        else:
            print("The car was already certified\n")

    def paint(self, chosen_color):
        while True:
            if chosen_color in self.available_colors:
                self.color = chosen_color
                self.description()
                break
            else:
                print(f"The chosen color {chosen_color} is not available")
                chosen_color = input(f"Please choose another color from"
                                     f" the available colors list: "
                                     f"{self.available_colors}:\n")
                chosen_color = chosen_color.title()
                continue

    def acceleration(self, speed_acceleration):
        if speed_acceleration > 0:
            if speed_acceleration <= self.max_speed:
                self.actual_speed = speed_acceleration
                self.description()
            else:
                self.actual_speed = self.max_speed
                self.description()
        else:
            print("Error! Invalid input! The speed value is invalid\n")

    def car_break(self):
        self.actual_speed = 0
        self.description()
