month = str(raw_input("Please enter one month of the year: "))

if(["December", "January", "February"].__contains__(month)):
    season = "winter"
    sport = "snowboarding"
elif(month in ["March", "April", "May"]):
    season = "spring"
    sport = "biking"

print("In {}, it is {}, I suggest you go {}".format(month, season, sport))
