'''

Basta Fazoolin'
You’ve started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart.
The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.

'''

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f'{self.name} menu available from {self.start_time} to {self.end_time}'

    def calculate_bill(self, purchasd_items):
        total = 0
        for k in purchasd_items:
            total += self.items[k]
        return total


brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu('brunch', brunch_items, 1100, 1600)
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu('early_bird', early_bird_items, 1500, 1800)

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu('dinner', dinner_items, 1700, 2300)

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu('kids', kids_items, 1100, 2100)


###############################################################
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        print(f'we are located at {address}')

    def available_menus(self, time):
        return Menu


flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


arepas_menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_place = Franchise("189 Fitzgerald Avenue", [brunch, early_bird, dinner, kids])
myBiz = Business("Take a' Arepa", [arepas_place, flagship_store, new_installment])