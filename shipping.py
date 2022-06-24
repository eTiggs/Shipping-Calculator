# Initilization 
inputWeight = input("How heavy is the package? (in lbs)")
groundFlatRate = 0.00
groundPriceLbs = 0.00
premiumFlatRate = 0.00
dronePriceLbs = 0.00
weight = float(inputWeight)

# Ground Shipping
if weight <= 2.00:
  groundFlatRate = 20.00
  groundPriceLbs = 1.50 * weight
elif weight > 2.00 and weight <= 6.00:
  groundFlatRate = 20.00
  groundPriceLbs = 3.00 * weight
elif weight > 6.00 and weight <= 10.00:
  groundFlatRate = 20.00
  groundPriceLbs = 4.00 * weight
else:
  groundFlatRate = 20.00
  groundPriceLbs = 4.75 * weight
# print(groundFlatRate + groundPriceLbs)

# Ground Shipping Premium
premiumFlatRate = 125.00
# print(premiumFlatRate)

# Drone Shipping
if weight <= 2.00:
  dronePriceLbs = 4.50 * weight
elif weight > 2.00 and weight <= 6.00:
  dronePriceLbs = 9.00 * weight
elif weight > 6.00 and weight <= 10.00:
  dronePriceLbs = 12.00 * weight
else:
  dronePriceLbs = 14.25 * weight
# print(dronePriceLbs)

#Display
print("--------------------------------------------------------")
print("====              Shipping Price List               ====")
print("--------------------------------------------------------")
print("====     Delivery Method            Price (£)       ====")
print("        -----------------          -----------          ")
print("====     Ground Shipping            £",groundFlatRate + groundPriceLbs,"         ====")
print("====     Premium Ground Shipping    £",premiumFlatRate,"        ====")
print("====     Drone Shipping             £", dronePriceLbs,"         ====")
print("--------------------------------------------------------")
