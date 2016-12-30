import chapter09.e02_restaurant.restaurant as rs
class IceCreamStand(rs.Restaurant):
    def __init__(self,restaurant_name, *flavors):
        cuisine_type = 'cool drink'
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        if self.flavors:
            print('The', self.restaurant_name, 'provide ice cream with follow flavors:')
            print(self.flavors)
        else:
            print('No flavors.')