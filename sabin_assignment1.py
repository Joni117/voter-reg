"""This code registers the user to vote and verifies if user is eligible"""
# Assignment 1 Joni Sabin
# Register to vote
#CYOP 300 Secure Python 21 August 2024

#Check user input with list of valid State abbreviations
def state_list(state):
    """Function listing the months abbreviations"""
    valid_states = {
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA',
        'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT',
        'VA', 'WA', 'WV', 'WI', 'WY'
    }
    return state.upper() in valid_states #Converts state to uppercase and checks for validity

#Method to determine if zip entered is valid by checking length of digits entered by users
def is_valid_zip_code(zip_code):
    """Function calculating zipcode length"""
    # Check the length make sure its 5 and all characters are digits
    return len(zip_code) == 5 and zip_code.isdigit()

#Grab all the inputs and check for errors
def get_input(prompt, entry=None, error_msg="Invalid input. Retype entry or exit application."):
    """Function to grab all the inputs from user"""
    while True:
        value = input(prompt)
        if entry is None or entry(value): #No entry is an error
            return value
        print(error_msg) #Display error message

#Main method of application, mains are not always needed in python
def main():
    """Function the main method"""

    #Print out the prompt to ask user if they want to continue application
    print("Welcome to the Python Voter Registration Application.")

    #Accepts all variations of yes and no then exits application when 'no' is entered
    if get_input("Do you want to continue with Voter Registration? (Yes/No): ",
             lambda x: x.lower() in ['yes', 'no','y','n'],
                 "Please enter Yes or No.").lower() in ['no','n']:
        print("Exiting the application.")
        return

    f_name = get_input("What is your first name?: ",
                       lambda x: len(x) > 0,
                       "First name cannot be empty.")

    # Print out the prompt to ask user if they want to continue application as others
    if get_input("Do you want to continue with Voter Registration? (Yes/No): ",
             lambda x: x.lower() in ['yes', 'no', 'y', 'n'],
                 "Please enter Yes or No.").lower() in ['no', 'n']:
        print("Exiting the application.")
        return

    l_name = get_input("What is your last name?: ",
                       lambda x: len(x) > 0,
                       "Last name cannot be empty.")

    # Print out the prompt to ask user if they want to continue application as others
    if get_input("Do you want to continue with Voter Registration? (Yes/No): ",
             lambda x: x.lower() in ['yes', 'no', 'y', 'n'],
                 "Please enter Yes or No.").lower() in ['no', 'n']:
        print("Exiting the application.")
        return

    #Verrifies the entry for age is valid (a digit not letter) and doesn't go above 120
    def valid_age(age):
        """Function getting the age"""
        return age.isdigit() and 0 < int(age) <= 120

    #Prompt user for the age and collect valid one
    age = get_input("What is your age?: ", valid_age,
                    "The valid age range is 1-120") #This is displayed when user enters invalid age
    age = int(age)

    #Check for age under 18 reject anyone under 18
    if age < 18:
        print("You must be at least 18 years old to register to vote.")
        return

    # Print out the prompt to ask user if they want to continue application as others
    if get_input("Do you want to continue with Voter Registration? (Yes/No): ",
             lambda x: x.lower() in ['yes', 'no', 'y', 'n'],
                 "Please enter Yes or No.").lower() in ['no', 'n']:
        print("Exiting the application.")
        return

    #Prompt user for US Citizenship
    if get_input("Are you a U.S. Citizen? (Yes/No): ",
                 lambda x: x.lower() in ['yes', 'no', 'y', 'n'],
                 "Please enter Yes or No.").lower() == ['no','n']:
        print("Must be a U.S. Citizen to register to vote.") #Error due not being US citizen
        return

    # Print out the prompt to ask user if they want to continue application as others
    if get_input("Do you want to continue with Voter Registration? (Yes/No): ",
             lambda x: x.lower() in ['yes', 'no', 'y', 'n'],
                 "Please enter Yes or No.").lower() in ['no', 'n']:
        print("Exiting the application.")
        return

    #Prompt user to enter their state with two letters
    state = get_input("What state do you live in? (2 letter abbreviation): ",
                      state_list,
                      "Please enter a valid U.S. state abbreviation.").upper()

    #Prompt user for their zip check for valid number being 5 digits and tell user not valid
    zip_code = get_input("What is your ZIP code?: ",
                         is_valid_zip_code,
                         "Enter a valid 5-digit ZIP code.")


    #Display all the entered entities by user
    print("\nThanks for registering to vote. Here is the information we received:")
    print(f"Name (first, last): {f_name}, {l_name}")
    print(f"Age: {age}")
    print("U.S. Citizen: Yes")
    print(f"State: {state}")
    print(f"Zipcode: {zip_code}")
    print(f"Thanks for submitting your Voter Registration Application."
          "\nYour voter registration card should be shipped within 3 weeks :)")

#Close out the main method of the program
if __name__ == "__main__":
    main()
