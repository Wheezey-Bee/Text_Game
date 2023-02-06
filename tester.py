user = input("What is your name? \n")
print("\n 3... 2... 1... \nWelcome to the adventure, " + user +"! \n \n")

stats =  {'inventory':[], 'experience':0, 'reputation':0}


#from chapters.Prologue import prologue
 
def game(user, stats):
  prologue(user, stats)

def prologue(user,stats):
  print("~~ PROLOGUE ~~")
  def p_1(user, stats):
    res = input("So, are you coming then " + user +"? \n[a] Yes \n[b] Who are you? \n[c] No \n")
    if res.lower() == 'a':
      print("Great! I knew I could count on you!")
      print("... It's going to be dangerous, possibly perilous, but you always said you wanted to go on adventure, so it's now or never!")
      return p_2(user, stats)
    elif res.lower() == 'b':
      print("Ha Ha. This is no time for jokes, mate! We've got a rather strict deadline after all...")
      return p_1(user, stats)
    elif res.lower() == 'c':
      print("All right then. I'll try and catch up with you again soon. See you on the flip side!")
      return p_1(user, stats)
    else:
      err_message()
      return p_1(user, stats)

  def p_2(user, stats):
    res = input("Last chance to back out. \n[a] I'm in! \n[b] Like you said... It's now or never... \n[c] Actually, I'm out... \n")
    if res.lower() == 'a':
      print("I never had any doubts!")
      print("""(These are your stats at the moment!): 
        inventory: """ +str(stats.get('inventory'))+ """
        experience: """ +str(stats.get('experience'))+ """
        reputation: """ +str(stats.get('reputation')))
      #from chap_1 import chapter_1 #error occurs here in seperate files
      return chapter_1(user, stats)

    elif res.lower() == 'b':
      print("That's the spirit!")
      #import chapters.chap_1
      #return chapters.chap_1(user, stats)
      return chapter_1(user, stats)
    elif res.lower == 'c': #loop created - doesn't go to p3
      print("Ha. Ha.")
      return p_3()
    else:
      err_message()
      return p_2()

  def p_3(user, stats):
    res = input("Wait... Are you being serious, " +user+"? \n[a] Yes \n[b] No \n")
    if res.lower() == 'a':
      print("Oh, okay! That's fine. Call me if you change your mind!")
    elif res.lower == 'b':
      print("Had me going there for a sec!")
      #import chapters.chap_1
      return chapter_1(user, stats)
    else:
      err_message()
      return p_3

  def err_message():
    print("Sorry, could you repeat that?")
    print("(Please press the corresponding key to your choice of dialogue)")

  p_1(user,stats)

#import chapters.chap_2
#
def chapter_1(user, stats):
  print("\n~~ CHAPTER 1 ~~")
  print("Right, so our goal is to kit up, get some experience, defeat the boss, save the town and live happily ever after.")
  return d1(user, stats)

def d1(user, stats):
  res = input("So, what should we do first? \n[a] Search the house for supplies \n[b] Find a map and plan our route \n[c] Accept a quest in a questionable pub \n[d] Do some training in the forest \n")
  if res.lower() == 'a':
    stats["inventory"].append('Axe', 'Canned Food', '10 Gold', 'Warm Blanket', 'Change of Clothes')#error in single file
    print("New Items in Inventory! \n" + stats["inventory"])
    print("Great idea! I did bring some supplies but I'm not sure if they were enough for the two of us.")
    return d1_1(user, stats) #create story choice ids/hidden list. Add id to list. If id in user list, you get a different outcome. If already done option, you cannot do it again.
  elif res.lower() == 'b':
    print("Good thinking! Who knows where we would end up otherwise!")
    inventory = inventory.append('Map')
    print("New Items in Inventory!\n" + inventory)
    return d1_2()
  elif res.lower() == 'c':
    print("There's a pub a few hours away, we could check there for any quests... Okay, let's do this!")
  elif res.lower() == 'd':
    print("Let's stay by your house while we train.")
  else:
    err_message()

def d1_1(user, stats):
  print('d1.1' + user + stats)

def d1_2():
  print('d1.2')
  
def err_message():
  print("Sorry, could you repeat that?")
  print("(Please press the corresponding key to your choice of dialogue)")


game(user, stats)