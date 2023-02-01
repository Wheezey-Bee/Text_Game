def prologue(user,stats):
  print("~~ PROLOGUE ~~")
  def p_1():
    res = input("So, are you coming then " + user +"? \n[a] Yes \n[b] Who are you? \n[c] No \n")
    if res.lower() == 'a':
      print("Great! I knew I could count on you!")
      print("... It's going to be dangerous, possibly perilous, but you always said you wanted to go on adventure, so it's now or never!")
      return p_2()
    elif res.lower() == 'b':
      print("Ha Ha. This is no time for jokes, mate! We've got a rather strict deadline after all...")
      return p_1()
    elif res.lower() == 'c':
      print("All right then. I'll try and catch up with you again soon. See you on the flip side!")
      return p_1()
    else:
      err_message()
      return p_1()

  def p_2():
    res = input("Last chance to back out. \n[a] I'm in! \n[b] Like you said... It's now or never... \n[c] Actually, I'm out... \n")
    if res.lower() == 'a':
      print("I never had any doubts!")
      print("""(These are your stats at the moment!): 
        inventory: """ +str(stats.get('inventory'))+ """
        experience: """ +str(stats.get('experience'))+ """
        reputation: """ +str(stats.get('reputation')))
      from chap_1 import chapter_1 #error occurs here 
      return chapter_1(user, stats)

    elif res.lower() == 'b':
      print("That's the spirit!")
      import chapters.chap_1
      return chapters.chap_1(user, stats)
    elif res.lower == 'c': #loop created - doesn't go to p3
      print("Ha. Ha.")
      return p_3()
    else:
      err_message()
      return p_2()

  def p_3():
    res = input("Wait... Are you being serious? \n[a] Yes \n[b] No \n")
    if res.lower() == 'a':
      print("Oh, okay! That's fine. Call me if you change your mind!")
    elif res.lower == 'b':
      print("Had me going there for a sec!")
      import chapters.chap_1
      return chapters.chap_1(user, stats)
    else:
      err_message()
      return p_3

  def err_message():
    print("Sorry, could you repeat that?")
    print("(Please press the corresponding key to your choice of dialogue)")

  p_1()