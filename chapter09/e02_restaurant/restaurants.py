import chapter09.e02_restaurant.restaurant as rs

my_restaurant = rs.Restaurant('毛家饭店', '湘菜')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

