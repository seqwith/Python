#
# Michael Winder
# SEC290 Summer 2020
# July, 18, 2020
# Homework 2
#

print('Automobile Fuel Cost Calculator')
print('')
print('This program may help you decide which car makes sense for you based on your budget.  You will be asked to enter the MPG for the car you have in mind, thte average number of miles you expect to drive each month and the cost per gallon for fuel.')
print('')
print('The program will then calculate the monthly fuel cost.')
print('')
carMpg = float(input("Please enter the car's MPG (Mile per Gallon): "))
avgMiles = int(input("Please enter your monthly miles driven: "))
fuelPrice = float(input("What is the price per gallon for fuel: $"))

gallonConsumed = avgMiles/carMpg
monthlyCost = gallonConsumed * fuelPrice

print('')
print("Given price of fuel at ${}/gallon and {} miles/month travelled:" .format(fuelPrice, avgMiles))
print('')
print("Gallons used per month: {:.1f}" .format(gallonConsumed))
print("Monthly cost of fuel: {:.2f}" .format(monthlyCost))
