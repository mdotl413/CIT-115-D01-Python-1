# Compound Interest with Loops

# Get User Input for Deposit
blnNeedDeposit = True  
while blnNeedDeposit:
    strInput = input("What is the Original Deposit (positive value): ")
    
# Float Validation
    blnIsValidFloat = True
    intDecimalCount = 0
    
    if strInput == "":
        blnIsValidFloat = False
    elif strInput == ".":
        blnIsValidFloat = False
    else:
      
        for char in strInput:
            if char == '.':
                intDecimalCount += 1
            elif char not in "0123456789":
# If it's not a decimal or number, it's invalid
                blnIsValidFloat = False 
        
        if intDecimalCount > 1:
            blnIsValidFloat = False  # Can't have more than one decimal
# End of Validation
            
    if blnIsValidFloat:
        fltDeposit = float(strInput)
        if fltDeposit > 0:
            blnNeedDeposit = False
        else:
            print("Input must be a positive numeric value")
    else:
        print("Input must be a positive numeric value (e.g., 100 or 100.50)")

# Get User Input for Interest Rate
blnNeedRate = True  
while blnNeedRate:
    strInput = input("What is the Interest Rate (positive value): ")
    
# Float Validation
    blnIsValidFloat = True
    intDecimalCount = 0
    
    if strInput == "":
        blnIsValidFloat = False
    elif strInput == ".":
        blnIsValidFloat = False
    else:
        for char in strInput:
            if char == '.':
                intDecimalCount += 1
            elif char not in "0123456789":
                blnIsValidFloat = False
        if intDecimalCount > 1:
            blnIsValidFloat = False
# End of Validation
            
    if blnIsValidFloat:
        fltInterestRate = float(strInput)
        if fltInterestRate > 0:
            blnNeedRate = False
        else:
            print("Input must be a positive numeric value")
    else:
        print("Input must be a positive numeric value (e.g., 5 or 5.75)")

# Get User Input for Months
blnNeedMonths = True  
while blnNeedMonths:
    strInput = input("What is the Number of Months (positive value): ")
    
# Manual Integer Validation
    blnIsValidInteger = True
    if strInput == "":
        blnIsValidInteger = False
    else:
        
        for char in strInput:
            if char not in "0123456789":
# If any character is not a number, it's invalid
                blnIsValidInteger = False
# End of Validation
                
    if blnIsValidInteger:
        intMonths = int(strInput)
        if intMonths > 0:
            blnNeedMonths = False
        else:
            print("Input must be a positive value (not zero)")
    else:
        print("Input must be a positive WHOLE number (e.g., 12)")

# Get User Input for Goal
blnNeedGoal = True  
while blnNeedGoal:
    strInput = input("What is the Goal Amount (can enter 0 but not negative): ")
    
# Manual Float Validation
    blnIsValidFloat = True
    intDecimalCount = 0
    
    if strInput == "":
        blnIsValidFloat = False
    elif strInput == ".":
        blnIsValidFloat = False
    else:
        for char in strInput:
            if char == '.':
                intDecimalCount += 1
            elif char not in "0123456789":
                blnIsValidFloat = False
        if intDecimalCount > 1:
            blnIsValidFloat = False
    # --- End of Validation ---
            
    if blnIsValidFloat:
        fltGoal = float(strInput)
        if fltGoal >= 0:
            blnNeedGoal = False
        else:
            print("Input must 0 or greater")
    else:
        print("Input must be a non-negative number (e.g., 5000 or 0)")

# Convert Interest Rate
fltMonthlyRate = (fltInterestRate / 100) / 12

# Calculate and Display Monthly Balance
print("\n--- Monthly Account Balance ---")
fltCurrentBalance = fltDeposit  

for intMonthNum in range(1, intMonths + 1):
    fltMonthlyInterest = fltCurrentBalance * fltMonthlyRate
    fltCurrentBalance += fltMonthlyInterest
    print(f"Month: {intMonthNum:<3} Account Balance is: ${fltCurrentBalance:,.2f}")

# Calculate Months to Reach Goal
if fltGoal > fltDeposit:
    fltGoalBalance = fltDeposit
    intGoalMonths = 0
    
    while fltGoalBalance < fltGoal:
        fltMonthlyInterest = fltGoalBalance * fltMonthlyRate
        fltGoalBalance += fltMonthlyInterest
        intGoalMonths += 1
        
    print("\n--- Savings Goal ---")
    print(f"It will take: {intGoalMonths:,} months to reach the goal of ${fltGoal:,.2f}")

elif fltGoal > 0 and fltGoal <= fltDeposit:
    print(f"\nYour deposit of ${fltDeposit:,.2f} already meets or exceeds your goal of ${fltGoal:,.2f}.")