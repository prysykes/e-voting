from party_registration import PartyRegistration
from party_registration import show_data


print("***Welcome to INEC party registration System*** \n")
print("***Enter party name press enter to save\n***")

partyone = PartyRegistration()
partyone.store_party()
show_data()
