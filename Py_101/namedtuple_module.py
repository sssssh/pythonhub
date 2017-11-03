from collections import namedtuple


Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc='Ford Engine',
                   cost=1200.00, amount=10)
print(auto_parts.id_num)


# also
auto_parts = ('1234', 'Ford Engine', 1200.00, 10)
id_num, desc, cost, amount = auto_parts


#
Auto_parts = {'id_num': '1314', 'desc': 'Asher Guan',
              'cost': 12145.00, 'amount': 23}
parts = namedtuple('Auto_parts', Auto_parts.keys())(**Auto_parts)
print(parts)
