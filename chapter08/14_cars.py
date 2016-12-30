def make_car(manufacturer, model, **car_info):
    """
    make car profile with manufacturer, model, and other info
    :param manufacturer:
    :param model:
    :param car_info:
    :return: dictionary car_profile{'manufacturer': manufacturer, 'model': model, ...}
    """
    car_profile = {}
    car_profile['manufacturer'] = manufacturer.lower().title()
    car_profile['model'] = model
    for k, v in car_info.items():
        car_profile[k] = v

    return car_profile

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('benz', 'ml 350')
print(car)