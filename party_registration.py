list_of_parties = []
party_dict = {}


class PartyRegistration:
    """ Takes in Party Registration From INEC"""

    def __init__(self):
        registering = True
        while registering:
            party = input("Enter Political Party Name \n (enter 'q' or press "
                          "Enter to quit): ").lower()
            if party == "" or party == "q":
                break
            list_of_parties.append(party)
            party_dict[party] = 0
            continue  # continues the loop until user enters q or presses enter
        self.party = party
   
    def store_party(self):
        pass


def show_data():
    print(list_of_parties)
    print(party_dict)
