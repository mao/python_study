def city_country(city_name, country):
    return str(city_name.lower().title() + ', ' + country.lower().title())

print(city_country('changsha', 'china'))
print(city_country('beIjing', 'chIna'))
print(city_country('new york', 'america'))