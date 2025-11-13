#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    Names =names.readlines()

for name in Names:
    with open("./Input/Letters/starting_letter.txt") as letter:
        mock_letter = letter.read()
        mock_letter = mock_letter.replace('[name]', name.strip())
        with open(f"./Output/ReadyToSend/Letter_for_{name.strip()}",'w') as new_letter:
            new_letter.write(mock_letter)
