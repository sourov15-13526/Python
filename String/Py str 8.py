def occurrenceofusa(a):
    substring = "usa"
    temstring = a.lower()
    count = temstring.count(substring)
    print("The USA count is",count)
occurrenceofusa("Welcome to USA. usa awesome, isn't it? Usa is the greatest country in the world")