print("***Welcome to INEC Electronic Voting System***")
print("")
processing = True
while processing:
    task = input("***Enter: 1 - to Register Political Paties \n"
                 "\tEnter: 2 - to Register Voters***: ")
    if task == "1":
        partyA = PartyRegistration()
        continue
    elif task == "2":
        user_one = RegisterVoter()
        break


show_data()
show_registered_voter()
