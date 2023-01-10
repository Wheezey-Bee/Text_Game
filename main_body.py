user = input("What is your name? \n")
print("\n 3... 2... 1... \nWelcome to the adventure, " + user +"! \n \n")

stats =  {'inventory':['empty'], 'experience':0, 'reputation':0}


from chapters.Prologue import prologue
 
def game(user, stats):
  prologue(user, stats)

game(user, stats)