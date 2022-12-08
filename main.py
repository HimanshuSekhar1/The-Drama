name = input('Enter your name? ')
gender = input('Are you male or female? ')
# f is used to concat string to a variable, we can do it in usual way using '+'
# Story for male
if gender == 'male' or gender == 'm':
  print(f'Hii, I am {name}')
  narration_m1 = input('After leaving from my busy clustered desk, I was waiting for my bus.\nAll the passengers,seemed to be relaxed,some were scrolling their phones and some were in dusky glasses looking for their bus, which took so long to arrive at the stop.')
  mind_m1 = input('Now, your mind is asking: ')
  ask_m1 = input('Should I "wait for the bus" or "book a cab"? ')
# wait for the bus
  if ask_m1 == 'wait for the bus':
    print('"Ugh...why the bus is so late!!!"')
    narration_m2 = input('Let us wait, what can I even do.\nIn this recession time all things are so expensive and even this cab.')
    narration_m3 = input('Suddenly my phone chimed.\nAnd I saw it was her.')
    ask_m2 = input('Should I "pick her call" or "hang up"?')
# pick her call
    if ask_m2 == 'pick her call':
      print("Hi, baby. I am here at the bus stop.")
      narration_m4 = input('On the phone:\nWhen are you reaching home, it\'s already late.')
      ask_m3 = input('Do you want to be "mad at her" or "sweet to her"?')
# mad at her
      if ask_m3 == 'mad at her':
        print('Please, don\'t call me thousand times.\nI am reaching home, bye.')
        end_m1 = print('Then you reached home after some time, had dinner together and slept without even a talk.\n"THE END"') # THIS PART IS DONE.
# sweet to her
      elif ask_m3 == 'sweet to her':
        print("Hi, baby. I am here at the bus stop.")
        narration_m5 = input('Have you got the ride?')
        narration_m6 = input('No....\nYeah.....\nI mean yeah, it just reached.\nSo, what you\'re saying?')
        narration_m7 = input('"No, I was saying....."')
        narration_m8 = input('"What ??"')
        narration_m10 = input('Do you want to say it or not ?')
        ask_m4 = input('You got irritated.\nDo you want to "hang up" or "remain in call"')
# hang up call
        if ask_m4 == 'hang up':
          print('Okay, don\'t say anything.\nBye')
          narration_m11 = print('Then you reached home after some time.\nShe was already sleeping.\nShe woke up, reheated the food for you, sat next to you watching while you eat. And smiled.\nThen you both went to the bed, cuddled and slept happily.\n"THE END"')
# THIS PART IS DONE.
# remain in call
        elif ask_m4 == 'remain in call':
          print('I have took off the covers, please come and screw me up.')
          narration_m12 = input("Damn, really!!!.\nI jumped off the bus stop,stamped on the muddy water and tried my best to get a lift going on that way.")
          narration_m13 = input("Finally, I got a ride and said,")
          narration_m14 = input('"Can you give me a ride ?"')
# hang up
    elif ask_m2 == 'hang up':
      print("Shut up. My brain is already churning up in the heat and now you're calling")
      narration_m9 = print('Then you reached home after some time.\nYou had brought some biryani for her, had dinner together and watched netflix, while she slept on your lap.\n"THE END"')
# THIS PART IS DONE.
# book a cab
  elif ask_m1 == 'book a cab':
    print('"I need to get home quickly."')


    
    
#Story for female
if gender == 'female' or gender == 'f':
  print(f'Hii, I am {name}')
  narration_f1 = input('The day was too tiring for me. After returning from the office, I completed all my chores and started reading my book. But in my mind, I was thinking, "When he would come back?". Does a single person working cannot fullfil or needs that we both are working. Umm...Wish he come home early')
  mind_f1 = input('Now, your mind is asking: ')
  ask_f1 = input('Should I "wait for him" or "give a call"? ')
  if ask_f1 == 'wait for him':
    print('"Ugh...I need fresh air in here. Let me go to the balcony."')
  elif ask_f1 == 'give a call':
    print('The phone started ringing.')


# narration2 = input('On the way you get some meat too.')
# items = input("Let's see what you got from the market: ")
# if items == 'paneer' or items == 'mushroom':
#   print('You vegan piece of shi*!!')
# else:
#   print("Ummm!! You've such a nice taste!!!")

