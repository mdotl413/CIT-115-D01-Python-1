sWelcome = "Welcome to Marciano's Tempature Convereter"
print(sWelcome)

sTempInput = input("Please enter the temperature")
fTempInput = float(sTempInput)
sUnitInput = input("Is this temperature in Fahrenheit (F) or Celsius (C)? ")

if sUnitInput != 'F' and sUnitInput != 'f' and sUnitInput != 'c' and sUnitInput != 'C':
    print("Enter a F or C")
    raise SystemExit

if sUnitInput == 'F' or sUnitInput == 'f':    
    
    if fTempInput > 212.0:
        print("Temp can not be > 212")

    else:
        fCelcius = ( 5.0/9.0 ) * (fTempInput - 32.0)
        print(f"The Celisius equivalent is:{fCelcius:.1f}")
        
elif sUnitInput == 'C' or sUnitInput == 'c':
    if fTempInput > 100.0:
        
        print("Temp can not be > 100")
        
    else:
        fFahrenheit = ((9.0 / 5.0) * fTempInput) + 32.0
        
        print(f"The Fahrenheit equivalent is: {fFahrenheit:.1f}")
