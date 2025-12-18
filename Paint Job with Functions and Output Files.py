# Paint Job with Functions and Output Files

import math

def getFloatInput(sPrompt):
    
    # function will ask user for input using sPrompt
    # It will loop until the user provides a valid number thats greater than 0
    
    while True:
        sInput = input(f"{sPrompt}: ")
        try:
            fValue = float(sInput)
            if fValue > 0:
                return fValue
            else:
                print("Error: Please enter a value greater than zero.")
        except ValueError:
            print("Error: Input must be a valid numeric value.")

def getGallonsOfPaint(fWallSpace, fFeetPerGallon):
    
    # Calculate how many gallons of paint are needed
    
    return math.ceil(fWallSpace / fFeetPerGallon)

def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    
    # Calculate total  amount of labor hours
    
    return fLaborHoursPerGallon * iTotalGallons

def getLaborCost(fTotalLaborHours, fLaborChargePerHour):
    
    # Calculate the total cost for labor
    
    return fTotalLaborHours * fLaborChargePerHour

def getPaintCost(iTotalGallons, fPaintPrice):
    
    # Calculate the total cost of paint
    
    return iTotalGallons * fPaintPrice

def getSalesTax(sState):
    
    # This function returns the specific tax rate for a given state
    # Convert input to uppercase so ct works the same as CT
    
    sStateUpper = sState.upper()
    
    if sStateUpper == "CT":
        return 0.06
    elif sStateUpper == "MA":
        return 0.0625
    elif sStateUpper == "ME":
        return 0.085
    elif sStateUpper == "NH":
        return 0.0
    elif sStateUpper == "RI":
        return 0.07
    elif sStateUpper == "VT":
        return 0.06
    else:
        # Default to 0 if the state isn't listed
        return 0.0

def showCostEstimate(iGallons, fLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCost):
    
    # Print the results
    
    print("\n" + "-"*30)
    print(f"Gallons of paint: {iGallons}")
    print(f"Hours of labor: {fLaborHours:.1f}")
    print(f"Paint charges: ${fPaintCost:,.2f}")
    print(f"Labor charges: ${fLaborCost:,.2f}")
    print(f"Tax: ${fTaxAmount:,.2f}")
    print(f"Total cost: ${fTotalCost:,.2f}")
    print("-"*30)

def saveToFile(sLastName, iGallons, fLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCost):
    
    # Create the file name using the customer last name
    
    sFileName = f"{sLastName}_PaintJobOutput.txt"
    
    try:
        
        # Open the file in write mode
        
        with open(sFileName, 'w') as file:
            file.write(f"Customer Last Name: {sLastName}\n")
            file.write(f"Gallons of paint: {iGallons}\n")
            file.write(f"Hours of labor: {fLaborHours:.1f}\n")
            file.write(f"Paint charges: ${fPaintCost:,.2f}\n")
            file.write(f"Labor charges: ${fLaborCost:,.2f}\n")
            file.write(f"Tax: ${fTaxAmount:,.2f}\n")
            file.write(f"Total cost: ${fTotalCost:,.2f}\n")
            
        print(f"\nFile: {sFileName} was created.")
    except Exception as e:
        print(f"Error creating file: {e}")

def main():
    
    # Ask the user for all the necessary numbers
    
    fWallSpace = getFloatInput("Enter wall space in square feet")
    fPaintPrice = getFloatInput("Enter paint price per gallon")
    fFeetPerGallon = getFloatInput("Enter feet per gallon")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon")
    fLaborChargePerHour = getFloatInput("Labor charge per hour")
    
    # Ask for text inputs for state and customer name
    
    sState = input("State job is in: ")
    sLastName = input("Customer Last Name: ")

    # Perform Calculations
    
    iGallons = getGallonsOfPaint(fWallSpace, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iGallons, fPaintPrice)
    
    # Calculate Tax
    
    fSubTotal = fLaborCost + fPaintCost
    fTaxRate = getSalesTax(sState)
    fTaxAmount = fSubTotal * fTaxRate
    
    fTotalCost = fSubTotal + fTaxAmount

    # Show the results on the screen
    
    showCostEstimate(iGallons, fLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCost)
    
    # Saves info to the file
    
    saveToFile(sLastName, iGallons, fLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCost)

# Start the program

main()