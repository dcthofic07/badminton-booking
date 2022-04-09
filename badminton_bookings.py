def total_cost():
    default_players = 2
    print("Hi, Welcome to Leicester City Council Badminton Booking.")
    print("Please note : 1 court booking includes 2 players only, any addtional players need to pay 3£ each")
    no_of_courts = input("How many courts do you wish to book today? ")
    no_of_hours = input("For how many hours do you wish to book these courts for? ")
    additional_players = input("No of additional players : ")
    basic_cost = 10.50
    additional_players_cost = 3
    tc = (int(no_of_courts)*int(no_of_hours)*basic_cost)+((int(additional_players)*additional_players_cost)*int(no_of_hours))
    print("The total cost of your booking is : " + str(tc) + "£")
    cpp = tc/(default_players+int(additional_players))
    print("If you are splitting the cost each player should pay : " + str(cpp) + "£")


total_cost()
