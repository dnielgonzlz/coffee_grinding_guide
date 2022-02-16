### COFFEE GRIND SIZE CALCULATOR IN MYTHOS COFFEE GRINDERS ###
#Information about the coffee extraction and dial in of the coffee used
GRINDING_COFFEE_TIME = float (input("How much time does the coffee takes to be grinded? ")) #Time that takes for the Mythos to grind the coffee beans
GRIND_SIZE = float (input ("What is the size of the grinding on the Mythos? ")) #The number that is showed on the notch, that is used as an arbitrary measurement
DIAL_IN_EXPECTED_TIME = int (input("What is the ideal time in seconds that the coffee needs to be brewed? ")) #The time that when the coffee is extracted tastes the best
DOSE_OF_COFFEE = float (input("How much grams of coffee are you using? ")) #Dose of coffee that goes on the portafilter
REAL_EXTRACTION_TIME = int (input("How much time does this extraction actually took? "))

#ADJUSTMENTS IN THE GRIND SIZE
THREE_EXTRA_SECONDS_OF_EXTRACTION = -2 #To achieve 3 seconds more on the extraction, reduce two points on the arbitrary measurement in the Mythos
THREE_LESS_SECONDS_OF_EXTRACTION = +2 #To achieve 3 seconds less in the extraction, increase two points on the arbitrary measurement in the Mythos

#Burrs Change ALERT
if GRINDING_COFFEE_TIME >= 10:
    print ("\nYour burrs are very old. Your grinder takes that time to grind the coffee because the burrs"
           "are not sharp enough, which also decreases extraction quality. \nChange the burrs ASAP!")
