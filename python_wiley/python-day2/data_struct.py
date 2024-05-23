cart=[]
cart.append('Iphone')
cart.append('airPods')
cart.append('harman-kardan')
cart.append('ipad')
cart.append('macbook')
combo_offer=['charger','backpack','screen']
cart.extend(combo_offer)
cart.remove('harman-kardan')
del cart[1]
x=cart.pop(2)
print(x)
print(cart[-2])
cart.sort()
print(cart)