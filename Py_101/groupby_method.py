from itertools import groupby


vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durange'),
            ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
            ('Dodge', 'Charger'), ('Ford', 'GT')]


sorted_vehicles = sorted(vehicles)


for key, group in groupby(sorted_vehicles, lambda make: make[0]):
    for make, model in group:
        print('{model} is make by {make}'.format(model=model,
                                                 make=make))
    print('**** END OF GROUP ***\n')
