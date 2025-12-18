#    Inter Planetary Weights

# Defining the Named Constants
MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91 
MOON_GRAVITY = 0.165
MARS_GRAVITY = 0.38 
JUPITER_GRAVITY = 2.34  
SATURN_GRAVITY = 0.93 
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.12
PLUTO_GRAVITY = 0.066

# Get input from the user

sName = input("What is your name: ")

# Ask for the weight

sWeight = input("What is your weight: ")

# Convert weight to a number

fEarthWeight = float(sWeight)

# Doing the calculations

fMercuryWeight = fEarthWeight * MERCURY_GRAVITY
fVenusWeight = fEarthWeight * VENUS_GRAVITY
fMoonWeight = fEarthWeight * MOON_GRAVITY
fMarsWeight = fEarthWeight * MARS_GRAVITY
fJupiterWeight = fEarthWeight * JUPITER_GRAVITY
fSaturnWeight = fEarthWeight * SATURN_GRAVITY
fUranusWeight = fEarthWeight * URANUS_GRAVITY
fNeptuneWeight = fEarthWeight * NEPTUNE_GRAVITY
fPlutoWeight = fEarthWeight * PLUTO_GRAVITY

# Print the results

print(sName + " here are your weights on our Solar System's planets:")

# Print each planet's weight

print("Weight on Mercury:   ", format(fMercuryWeight, '10.2f'))
print("Weight on Venus:     ", format(fVenusWeight, '10.2f'))
print("Weight on our Moon:  ", format(fMoonWeight, '10.2f'))
print("Weight on Mars:      ", format(fMarsWeight, '10.2f'))
print("Weight on Jupiter:   ", format(fJupiterWeight, '10.2f'))
print("Weight on Saturn:    ", format(fSaturnWeight, '10.2f'))
print("Weight on Uranus:    ", format(fUranusWeight, '10.2f'))
print("Weight on Neptune:   ", format(fNeptuneWeight, '10.2f'))
print("Weight on Pluto:     ", format(fPlutoWeight, '10.2f'))