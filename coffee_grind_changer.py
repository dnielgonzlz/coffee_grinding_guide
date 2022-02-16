### COFFEE GRIND SIZE CALCULATOR IN MYTHOS COFFEE GRINDERS ###
#Information about the coffee extraction and dial in of the coffee used
grind_size = float(input("What is the size of the grinding on the Mythos? ")) #The number that is showed on the notch, that is used as an arbitrary measurement
dial_in_expected_time = int(input("What is the ideal time in seconds that the coffee needs to be brewed? ")) #The time that when the coffee is extracted tastes the best
real_extraction_time = int(input("How much time does this extraction actually took? "))
error_difference_extraction = dial_in_expected_time - real_extraction_time

#ADJUSTMENTS IN THE GRIND SIZE - CHART
THREE_EXTRA_SECONDS_OF_EXTRACTION = 2 #To achieve 3 seconds more on the extraction, reduce two points on the arbitrary measurement in the Mythos
THREE_LESS_SECONDS_OF_EXTRACTION = 2 #To achieve 3 seconds less in the extraction, increase two points on the arbitrary measurement in the Mythos
ADJUSTING_TIME_FINER_EXTRACTION = 0.15
ADJUSTING_TIME_COARSER_EXTRACTION = 0.15
finer_grinding_time = 0
coarser_grinding_time = 0

#ADJUSTMENTS IN THE GRIND SIZE - MAKING IT FINER
if 0.5 < error_difference_extraction <= 3:
    finer_grind_size = grind_size - THREE_EXTRA_SECONDS_OF_EXTRACTION
elif 3 < error_difference_extraction <= 6:
    finer_grind_size = grind_size - THREE_EXTRA_SECONDS_OF_EXTRACTION*2
elif 6 < error_difference_extraction <= 9:
    finer_grind_size = grind_size - THREE_EXTRA_SECONDS_OF_EXTRACTION*3
elif 9 < error_difference_extraction <= 12:
    finer_grind_size = grind_size - THREE_EXTRA_SECONDS_OF_EXTRACTION*4
elif 12 < error_difference_extraction <= 15:
    finer_grind_size = grind_size - THREE_EXTRA_SECONDS_OF_EXTRACTION*5

#MESSAGE TO GRIND FINER
if 0.5 < error_difference_extraction <= 3:
    print("\nYou need to decrease the Mythos Grind size by 2 points and increase Mythos grinding time 0.5 seconds.\n")
elif 3 < error_difference_extraction <= 6:
    print("\nYou need to decrease the Mythos Grind size by 4 points and increase Mythos grinding time 1 seconds.\n")
elif 6 < error_difference_extraction <= 9:
    print("\nYou need to decrease the Mythos Grind size by 6 points and increase Mythos grinding time 1.5 seconds.\n")
elif 9 < error_difference_extraction <= 12:
    print("\nYou need to decrease the Mythos Grind size by 8 points and increase Mythos grinding time 2 seconds.\n")
elif 12 < error_difference_extraction <= 15:
    print("\nYou need to decrease the Mythos Grind size by 10 points and increase Mythos grinding time 2.5 seconds.\n")

#ADJUSTMENTS IN THE GRIND SIZE - MAKING IT COARSER
if -0.5 > error_difference_extraction >= -3:
    coarser_grind_size = grind_size + THREE_LESS_SECONDS_OF_EXTRACTION
elif -3 > error_difference_extraction >= -6:
    coarser_grind_size = grind_size + THREE_LESS_SECONDS_OF_EXTRACTION*2
elif -6 > error_difference_extraction >= -9:
    coarser_grind_size = grind_size + THREE_LESS_SECONDS_OF_EXTRACTION*3
elif -9 > error_difference_extraction >= -12:
    coarser_grind_size = grind_size + THREE_LESS_SECONDS_OF_EXTRACTION*4
elif -12 > error_difference_extraction >= -15:
    coarser_grind_size = grind_size + THREE_LESS_SECONDS_OF_EXTRACTION*5

#MESSAGE TO GRIND COARSER
if -0.5 > error_difference_extraction >= -3:
    print("\nYou need to increase the Mythos Grind size by 2 points and decrease Mythos grinding time -0.5 seconds.\n")
elif -3 > error_difference_extraction >= -6:
    print("\nYou need to increase the Mythos Grind size by 4 points and decrease Mythos grinding time -1 seconds.\n")
elif -6 > error_difference_extraction >= -9:
    print("\nYou need to increase the Mythos Grind size by 6 points and decrease Mythos grinding time -1.5 seconds.\n")
elif -9 > error_difference_extraction >= -12:
    print("\nYou need to increase the Mythos Grind size by 8 points and decrease Mythos grinding time -2 seconds.\n")
elif -12 > error_difference_extraction >= -15:
    print("\nYou need to increase the Mythos Grind size by 10 points and decrease Mythos grinding time -2.5 seconds.\n")

#Burrs Change ALERT
if grinding_coffee_time >= 8:
    print ("\nYour burrs are very old. Your grinder takes that time to grind the coffee because the burrs"
           "are not sharp enough, which also decreases extraction quality. \nChange the burrs ASAP!")