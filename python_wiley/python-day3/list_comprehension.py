# # print([ f'2 * {i} = {2*i}'  for i in range(5) ])

# colors=['Red','indigo','pink','orange','purple']

# print([x for x in range(100) if x<6])

# print([f'{x}:even' if x%2==0 else f'{x}:odd' for x in range(100)])

# pw=[110,120,130,140,150,160]

# print([f'{x} pounds = {round(x*0.453)}' for x in pw])

karachiBakery= [ ('veg','biscuit'), ('veg','dhokla') ,('nonveg','butterchicken'),('veg','paneer'),('nonveg','prawns')]
print([x[1] for x in karachiBakery if x[0]=='veg'])