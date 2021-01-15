##MADLIB

adjetive = ""
verv = ""
pronoun = ""

###ASK FOR ADJETIVES, PRONOUN AND VERB 

while adjetive == "":
    adjetive = input("Enter an adjective:\n")
while verv == "":
    verv = input("Enter an verv:\n")
while pronoun == "":
    pronoun = input("Enter an pronoun:\n")
    
###PRINTS THE SENTENCE WITH THE UPDATED VARIABLES
print(f"{pronoun} is {adjetive} at {verv} pickles and telling women about his emotional problems.")