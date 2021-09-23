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
births = float(input("Enter births per second:"))
deaths = float(input("Enter deaths per second:"))
migration = float(input("Enter migration per second:"))
years = float(input("Enter how many years into the future:"))
population = float(input("Enter the population:"))

# time
# minBirth = births / 60
# hoursBirths = minBirth / 60
# daysBirths = hoursBirths / 24
# yearsBirths = daysBirths / 365.25
# minDeaths = deaths / 60
# hoursDeaths = minDeaths / 60
# daysDeaths = hoursDeaths / 24
# yearsDeaths = daysDeaths / 365.25
# minMigration = migration / 60
# hoursMigration = minMigration / 60
# daysMigration = hoursMigration / 24
# yearsMigration = daysMigration / 365.25
# equations
projectedPopulation = ((births - deaths - migration)*population) * years * 365 * 24 * 60 * 60 + population

# if
# print
print("Projected population is:", projectedPopulation)
