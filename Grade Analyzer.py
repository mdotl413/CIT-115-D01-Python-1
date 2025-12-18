# Name

strName = input("Name of the person we are calculating the grades for: ")

# Test grade inputs

fltTest1 = float (input("Enter Test 1 score: "))
fltTest2 = float (input("Enter Test 2 score: "))
fltTest3 = float (input("Enter Test 3 score: "))
fltTest4 = float (input("Enter Test 4 score: "))

strDropLow = input("Do you wish to drop the lowest grade Y or N? ").upper()

if fltTest1 < 0 or fltTest2 < 0 or fltTest3 < 0 or fltTest4 < 0:
         print("Test score must be greater than 0")
         exit()
if strDropLow != "Y" and strDropLow != "N":
            print("Enter Y or N to drop the lowest grade.")
            exit()
if strDropLow == "Y":
    if fltTest1 <= fltTest2 and fltTest1 <= fltTest3 and fltTest1 <= fltTest4:
# If fltTest1 is the lowest then its dropped
        fltAverage = (fltTest2 + fltTest3 + fltTest4) / 3.0
    elif fltTest2 <= fltTest1 and fltTest2 <= fltTest3 and fltTest2 <= fltTest4:
# If fltTest2 is the lowest then its dropped
        fltAverage = (fltTest1 + fltTest3 + fltTest4) / 3.0
    elif fltTest3 <= fltTest1 and fltTest3 <= fltTest2 and fltTest3 <= fltTest4:
        fltAverage = (fltTest1 + fltTest2 + fltTest4) / 3.0
# If fltTest3 is the lowest then its dropped
    else:
        fltAverage = (fltTest1 + fltTest2 + fltTest3) / 3.0
elif strDropLow == "N":
     fltAverage = (fltTest1 + fltTest2 + fltTest3 + fltTest4) / 4.0
        
# defining Letter grade

if fltAverage >= 97.0:
    strLetterGrade = "A+"
elif fltAverage >= 94.0:
        strLetterGrade = "A"
elif fltAverage >= 90.0:
        strLetterGrade = "A-"
elif fltAverage >= 87.0:
    strLetterGrade = "B+"
elif fltAverage >= 84.0:
    strLetterGrade = "B"
elif fltAverage >= 80.0:
    strLetterGrade = "B-"
elif fltAverage >= 77.0:
     strLetterGrade = "C+"
elif fltAverage >= 74.0:
     strLetterGrade = "C"
elif fltAverage >= 70.0:
     strLetterGrade = "C-"
elif fltAverage >= 67.0:
     strLetterGrade = "D+"
elif fltAverage >= 64.0:
     strLetterGrade = "D"
elif fltAverage >=  60.0:
     strLetterGrade = "D-"
else: 
     strLetterGrade = "F"
        
#  Ouput
print(f"{strName} Caluculated test average is: {fltAverage:.1f}")
print(f" Letter grade is: {strLetterGrade}")
input("\nPress the enter key to exit.")