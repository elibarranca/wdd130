import math

"""
calculate the speed of a falling object with the formula
v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
now you have to convert it for python
"""
print()
print("Welcome to the velocity calculator. Please enter the following:?\n")
print()

#enter the information and begin calcualtions

m=float(input("Mass (in kg):  "))
g=float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter):  "))
t=float(input(("Time (in seconds):  ")))
p=float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water):  "))
A=float(input(("Cross sectional area (in m^2):  ")))
C=float(input(("Drag constant (0.5 for sphere, 1.1 for cylinder):  ")))
print()

#formulas

c=1/2 * p * A * C
velocity_at_t=  math.sqrt(m*g/c) * (1 - math.exp((- math.sqrt(m * g * c)/m) * t))

#results
print(f"The inner value of c is:  {c:.3f}")
print(f"The velocity after {t} seconds is:  {velocity_at_t:.3f}m/s")
print()