def total_cost():
    #default_players = 2
    no_of_courts = input("How many courts do you wish to book today? ")
    no_of_hours = input("For how many hours do you wish to book these courts for? ")
    additional_players = input("No of additional players : ")
    basic_cost = 10.50
    additional_players_cost = 3
    tc = (int(no_of_courts)*int(no_of_hours)*basic_cost)+((int(additional_players)*additional_players_cost)*int(no_of_hours))
    print("The total cost of this booking is " + tc)


total_cost()
