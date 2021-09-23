# Programmers: Aidan, Anthony
# Course: CS151, Dr.Rajeev
# Date: 9/23/21
# Lab Number:2
# Program Inputs: Years, Births, Deaths, Migration
# Program Outputs: Projected population

# Problem Every country has a change in population over time (up or down) due to three causes: births, deaths,
# and migration. Write a program that estimates future population size for a country given its number of births,
# deaths, and migrations per second, the current population, and the desired number of years in the future for the
# estimate. For example, if the user enters 0.125 births per second, 0.0833 deaths per second, 0.0357 inmigrations
# per second, a current population of 326,766,748 (estimates from the US Census) and wants to estimate the
# population 5 years into the future, the program should respond with an estimate of 338,971,180. Note: to
# specify net emmigration, use a negative number for migration.

# inputs
births = .125
deaths = .0833
migration = .0357
years = 5
population = 326766748
# births = float(input("Enter births per second:"))
# deaths = float(input("Enter deaths per second:"))
# migration = float(input("Enter migration per second:"))
# years = float(input("Enter how many years into the future:"))
# population = float(input("Enter the population:"))

# equations
popRate = (births - deaths + migration)
print(popRate)
projectedPopulation = popRate * 31536000 * years + population

# if
if projectedPopulation <= 0:
    print("Projected population will die off.")
elif projectedPopulation >= 0:
    print("Projected population is:", projectedPopulation)
