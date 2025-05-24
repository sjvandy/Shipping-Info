# Ask the user for the weight of the package.
weight = float(input("What is the weight of the package in lbs?: "))

if weight <= 2:
  ground_cost = (weight * 1.5) + 20
elif weight <= 6:
  ground_cost = (weight * 3) + 20
elif weight <= 10:
  ground_cost = (weight * 4) + 20
else:
  ground_cost = (weight * 4.75) + 20

premium_cost = 125.00

if weight <= 2:
  drone_cost = weight * 4.50
elif weight <= 6:
  drone_cost = weight * 9.00
elif weight <= 10:
  drone_cost = weight * 12.00
else:
  drone_cost = weight * 14.25

if ground_cost < premium_cost and ground_cost < drone_cost:
  print("\nThe cheapest shipping method is Ground Shipping.")
  print(f"It will cost: ${ground_cost:.2f}")
elif premium_cost < ground_cost and premium_cost < drone_cost:
  print("\nThe cheapest shipping method is Ground Shipping Premium.")
  print(f"It will cost: ${premium_cost:.2f}")
else:
  print("\nThe cheapest shipping method is Drone Shipping.")
  print(f"It will cost: ${drone_cost:.2f}")