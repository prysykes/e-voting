import json

voters_details = {}
registered_voters = []
file_path = 'textFiles\store_voters.json'


class VoterRegistration:
    def __init__(self):
        registering = True
        while registering:
            print("Enter quit to end the registration process")
            fname = input("Enter Your First Name: ")
            lname = input("Enter Your Last Name: ")
            state_of_origin = input("Enter Your state of origin: ")
            try:
                age = int(input("Enter Your Age: "))
            except ValueError:
                print("Your Age Should be a Number! ")
                age = int(input("Enter Your Age: "))
            self.fname = fname
            self.lname = lname
            self.state = state_of_origin
            self.age = age
            if age < 18:
                print("You are not up to the voting Age!")
                registering = False
            else:
                """Creates a dictionary object for a
                particular voter and stores in a list"""
                voters_details["First Name"] = self.fname
                voters_details["Last Name"] = self.lname
                voters_details["State of Origin"] = self.state
                voters_details["Age"] = self.age
                registered_voters.append(voters_details)
            response = input("Any other voter to register(enter yes or no or quit)): ").lower()
            if response == "no" or response == "quit":  # checks if there are more voters to register
                break
    
    def store_voter(self):
        with open(file_path, 'a', newline="\n", encoding="utf-8") as f_voters:
            json.dump(registered_voters, f_voters)


def show_registered_voter():
    print(voters_details)
    print(registered_voters)
