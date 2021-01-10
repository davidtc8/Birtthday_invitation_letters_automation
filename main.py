#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"
# 2nd test
import docx
import os



file_path = r"C:\Users\David Torres\Desktop\Programming\Python\100 Days of Code Course\Birtthday_invitation_letters_automation\Input\Names\invited_names.txt"
os.path.basename(file_path)
with open(file_path, mode = "r") as file:
    names = file.readlines()
    print(names)

# function to read the docx file
def reading_text(filename):
    doc = docx.Document(filename)

    completed_text = []

    for paragraph in doc.paragraphs:
        completed_text.append(paragraph.text)

    return '\n'.join(completed_text)

print(reading_text('starting_letter.docx'))

letter_content = reading_text('starting_letter.docx')

for name in names:
    stripped_name = name.strip()
    new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
    print(new_letter)
    with open(f'/Users/David Torres/Desktop/Programming/Python/100 Days of Code Course/Birtthday_invitation_letters_automation/Output/ReadyToSend/letter_for_{stripped_name}.docx', mode = 'w') as completed_letter:
        completed_letter.write(new_letter)
