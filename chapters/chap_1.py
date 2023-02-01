#import chapters.chap_2
#
def chapter_1(user, stats):
  print("\n~~ CHAPTER 1 ~~")
  print("Right, so our goal is to kit up, get some experience, defeat the boss, save the town and live happily ever after.")
  return d1(user, stats)

def d1(user, stats):
  res = input("So, what should we do first? \n[a] Search the house for supplies \n[b] Find a map and plan our route \n[c] Accept a quest in a questionable pub \n[d] Do some training in the forest \n")
  if res.lower() == 'a':
    inventory.append('Axe', 'Canned Food', '10 Gold', 'Warm Blanket', 'Change of Clothes')
    print("New Items in Inventory! \n" + inventory)
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

chapter_1()