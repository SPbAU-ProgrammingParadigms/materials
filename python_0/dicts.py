### Dictionaries - Map
empty_dict = {} # or dict()
capitals = dict(France='Paris',
                Germany='Berlin',
                Zimbabwe='Harare')
capitals_2 = {'USA': 'Washington, D.C',
              'Australia': 'Canberra',
              'Russia': 'Moscow'}
capitals_3 = dict([('Ireland', 'Dublin'), ('Poland', 'Warsaw')])
capitals.update(capitals_2)
capitals.update(capitals_3)

capitals['Russia'] = 'Saint-Petersburg'
len(capitals)
print(capitals['Zimbabwe'])
# d.keys(), d.values(), d.items()
# for key in capitals:
#     print(key)
# for key, value in capitals.items():
#     print(key, ':', value)

# dict comprehensions
{x: x * x for x in range(10) if x % 2 == 0}


### sets
# s = {1, 2,'hello'}
# 'hello' in s # True
# set comprehensions
{i for i in range(1, 10, 2)}
