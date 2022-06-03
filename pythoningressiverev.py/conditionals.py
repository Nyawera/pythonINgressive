age = 18
movie = "Money heist"
if age >= 18:
    print("customer can purchase ticket for this movie " + movie)
    if age < 18:
        print("customer is not allowed to watch this movie")
    age = 14
    height = 4
    if age >= 18 and height >= 5:
        print("person can get on this ride")
        if age < 18 or height < 5:
            print("person cannot get on this ride")