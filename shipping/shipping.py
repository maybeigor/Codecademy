weight = 41.5
flat_charge= 20
cost_prime_ground = 125
cost_ground = ""
cost_drone = ""
#Ground Shipping 
if weight <= 2:
 cost_ground= 1.50 * weight + flat_charge
elif weight <= 6:
    cost_ground= 3.00 * weight + flat_charge
elif weight <= 10:
    cost_ground = 4.00 * weight + flat_charge
elif weight > 10:
    cost_ground = 4.75 * weight + flat_charge
else:
  print ("Error, Weight cannot be equal to given value")
print ("Ground prise: ", cost_ground , "$")

# Prime Ground Shipping
cost_prime_ground = 125
print ("Premium prise: ", cost_prime_ground , "$")

#Drone Shipping 
if weight <= 2:
 cost_drone= 4.50 * weight
elif weight <= 6:
    cost_drone= 9.00 * weight
elif weight <= 10:
    cost_drone = 12.00 * weight
elif weight > 10:
    cost_drone = 14.25 * weight
else:
  print ("Error, Weight cannot be equal to given value")
print ("Drone prise: ", cost_drone , "$")
