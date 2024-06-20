###############################################################
#    Assignment:  05 Prove: Milestone - Adventure Game
#    
#    Program: Adventure Game
#
#    File: click_and_point.py
#
#    Author(s): Lincoln Huls
#
#
#    Date: May 21, 2024
###############################################################
import streamlit as st

# Importing the end story function
import sys
import time
import os

# Adding text deplay for the text 
# def st.write(text, speed=0.03):
#     message = st.empty()
#     for i in range(len(text) + 1):
     #    message.markdown(text[:i])
     #    time.sleep(speed)

# Creating the functions for the stories
# Double quotes so that I can use don't
st.write ("You groggily look around. You don't remember what happened or how you got here, but here you are.")
st.write('In front of you lies three objects, a sword, a toy car, and what looks like a lazer gun. It is obvious that you are suppossed to pick one.')

# Picking their story
while True:
     incorrect_answer_0 = 0
     story_choice = st.text_input('Which one will you choose?[Sword, Toy Car, Lazer Gun] ', key='option').strip().lower()
     if story_choice in ['sword', 'toy car', 'lazer gun']:
          break
     else:
          incorrect_answer_0 = 1
if incorrect_answer_0 == 1:
     st.write('Invalid choice, please enter Sword, Toy Car, or Lazer Gun.')
if story_choice.lower() == 'sword':
    st.write('The sword feels heavy in your hand. You hear a clanking behind you, it sounds loud, getting closer.')
    while True:
         turn = st.text_input('Will you turn around? [Yes, No] ', key='option1').strip().lower()
         if turn in ['yes', 'no']:
              break

    if turn.lower() ==  'yes':
         st.write('You see an old, rusted suit of armor approaching you.')
         while True:
              swing = st.text_input('You have three options, run, take a swing, or do nothing. [Run, Swing, Nothing] ', key='option2').strip().lower()
              if swing in ['run', 'swing', 'nothing']:
                   break

         if swing.lower() == 'swing':
              st.write('The sword feels strangely familiar in your hands. The suit crumbles to the ground and you head for the door.')
              while True:
                   outside = st.text_input('You find yourself in a couryard, with a large staute in the center. There seems to be a place you can insert your sword. [Insert, Leave] ', key='option3').strip().lower()
                   if outside in ['insert', 'leave']:
                        break

              if outside.lower() == 'insert':
                   while True:
                        knighting = st.text_input('You hear a loud click, followed by the statue drawing its own sword. It beckons you to come forward. [Go, Run] ', key='option4').strip().lower()
                        if knighting in ['go', 'run']:
                             break

                   if knighting.lower() == 'go':
                        st.write('The statue beckons again, this time for you to kneel. You do so, and it raises its sword, and knights you.')
                        while True:
                             home = st.text_input('You feel a strange, strong, power enter your body and mind. With this power, you can return home, or stay in this world. [Home, Stay] ', key='option5').strip().lower()
                             if home in ['home', 'stay']:
                                  break

                        if home.lower == 'home':
                             st.write('With this new power, you will yourself to be home, and the world begins to shift around you. You find yourself in your bedroom. You can still feel the power inside.')
                             st.write('This will be fun.')
                             time.sleep(3)
                             st.write('Thank you for playing!')
                             time.sleep(5)
                             os.system('cls' if os.name == 'nt' else 'clear')
                             sys.exit()
                        else:
                             st.write('You find that you are excited for a journey that lies ahead. You can always return home later, right?')
                             st.write('This will be fun.')
                             time.sleep(3)
                             st.write('Thank you for playing!')
                             time.sleep(5)
                             os.system('cls' if os.name == 'nt' else 'clear')
                             sys.exit()
                   else:
                        st.write('Turns out that the statue also had a bow, apparently, he would rather you had stayed.')
                        st.write('Thank you for playing!')
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sys.exit()
              else:
                   st.write('You feel a thud in your chest and look down to see an arrow. You look forward to see another suit holding a drawn bow. Apparently they wanted you to stay.')
                   st.write('Thank you for playing!')
                   time.sleep(5)
                   os.system('cls' if os.name == 'nt' else 'clear')
                   sys.exit() 
         elif swing.lower() == 'run':
              st.write('You run for the door, narrowly avoid a swing from the suit. You slam the old door shut behind you and lock it.')
              st.write('You turn around to see that the world around you has changed. It seems that you are standing in a courtyard in a large castle.')
              while True:
                   statue = st.text_input('In the center is a statue of a large knight. It has a slot that you can insert your sword into. [Insert, Leave] ', key='option6').strip().lower()
                   if statue in ['insert', 'lower']:
                        break

              if statue.lower() == 'insert':
                   while True:
                        knighting = st.text_input('You hear a loud click, followed by the statue drawing its own sword. It beckons you to come forward. [Go, Run] ', key='option7').strip().lower()
                        if knighting in ['go', 'run']:
                             break

                   if knighting.lower() == 'go':
                        st.write('The statue beckons again, this time for you to kneel. You do so, and it raises its sword, and knights you.')
                        while True:
                             home = st.text_input('You feel a strange, strong, power enter your body and mind. With this power, you can return home, or stay in this world. [Home, Stay] ', key='option8').strip().lower()
                             if home in ['home', 'stay']:
                                  break

                        if home.lower == 'home':
                             st.write('With this new power, you will yourself to be home, and the world begins to shift around you. You find yourself in your bedroom. You can still feel the power inside.')
                             st.write('This will be fun')
                             time.sleep(3)
                             st.write('Thank you for playing!')
                             time.sleep(5)
                             os.system('cls' if os.name == 'nt' else 'clear')
                             sys.exit()
                        else:
                             st.write('You find that you are excited for a journey that lies ahead. You can always return home later, right?')
                             st.write('This will be fun')
                             time.sleep(3)
                             st.write('Thank you for playing!')
                             time.sleep(5)
                             os.system('cls' if os.name == 'nt' else 'clear')
                             sys.exit()
                   else:
                        st.write('Turns out that the statue also had a bow, apparently, he would rather you had stayed.')
                        st.write('Thank you for playing!')
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sys.exit()
              else:
                   st.write('You feel a thud in your chest and look down to see an arrow. You look forward to see another suit holding a drawn bow. Apparently they wanted you to stay.')
                   st.write('Thank you for playing!')
                   time.sleep(5)
                   os.system('cls' if os.name == 'nt' else 'clear')
                   sys.exit()
         else:
            #   Double quotes for doesn't
              st.write("The suit looks at you, as if confused, then swings his sword, and you fall. He doesn't seem the most friendly.")
              st.write('Thank you for plaing!')
              time.sleep(5)
              os.system('cls' if os.name == 'nt' else 'clear')
              sys.exit
    else:
         st.write('You feel a heavy blow to your shoulder, and the last thing you see is an old, rusted suit of armor standing over you.')
         st.write('Thank you for playing!')
         time.sleep(5)
         os.system('cls' if os.name == 'nt' else 'clear')
         sys.exit()






elif story_choice.lower() == 'toy car':
    st.write('As your hand touches the car, you suddenly find yourself sitting behind the steerting wheel of a car. It seems to be just like the one you picked.')
    st.write('You look in the rearview mirror to see several other cars in hot persuit. You have a bad feeling about this.')
    while True:
         stop_or_go = st.text_input('Step on the gas or try to talk the situation down. [Gas, Stop] ', key='option9').strip().lower()
         if stop_or_go in ['gas', 'stop']:
              break

    if stop_or_go.lower() == 'gas':
         st.write('The engine roars to life with the touch of your foot. Ahead you see an intersection, but it has a red light.')
         while True:
              intersection = st.text_input('You can go straight, turn left, or stop for the light. [Straight, Left, Stop] ', key='option10').strip().lower()
              if intersection in ['straight', 'left', 'stop']:
                   break

         if intersection.lower() == 'straight':
              st.write('You narrowly avoid a crash, but the car you missed makes those following you stop.')
              while True:
                   stay_in = st.text_input('Now that the cars are held up, you can either stay in the car and keep driving, or get out and try to lose them in the people. [Stay, Leave] ', key='option11').strip().lower()
                   if stay_in in ['stay', 'leave']:
                        break

              if stay_in.lower() == 'stay':
                   st.write('You continue to drive down the road that you are on.')
                   while True:
                        fork = st.text_input('Eventually, you come to a fork in the road. [Left, Middle, Right] ', key='option12').strip().lower()
                        if fork in ['left', 'middle', 'right']:
                             break

                   if fork.lower() == 'left':
                        while True:
                             turn_around = st.text_input('The road you are going down seems to get darker with every passing second. You have a bad feeling. [Turn, Go] ', key='option13').strip().lower()
                             if turn_around in ['turn', 'go']:
                                  break

                        if turn_around.lower() == 'turn':
                             st.write('As you turn the steering wheel, you feel a tire blow and you veer off the road, coming to a sudden stop as the car meets a tree.')
                             while True:
                                  venture = st.text_input("You get out of the car, it won't be running anymore. [Walk, Wait] ", key='option14').strip().lower()
                                  if venture in ['walk', 'wait']:
                                       break

                             if venture.lower() == 'walk':
                                  st.write('You begin the long trek down the road. Finally, after what seems like hours, you see an old, broken down building in the distance.')
                                  st.write('You walk in to find a man waiting in a chair for you. "You made it!", he says.')
                                  while True:
                                       follow  = st.text_input('"Congradulations, I know you have questions, just follow me and all will be answered."[Follow, Refuse] ', key='option15').strip().lower()
                                       if follow in ['follow', 'refuse']:
                                            break

                                  if follow.lower() == 'follow':
                                       st.write("You don't know who this man is, or what he wants, but you feel something compelling you to follow.")
                                       st.write('Guess there is only one way to find out what is going on.')
                                       st.write('Thank you for playing!')
                                       time.sleep(5)
                                       os.system('cls' if os.name == 'nt' else 'clear')
                                       sys.exit()
                                  else:
                                       st.write('You begin to walk away, and you hear the man sigh. "You are free to leave, but you will never know why this happened if you do."')
                                       st.write("At this point, you don't even really want to know why, you just want to get home. A car is parked outside with the note, 'For your troubles.'")
                                       st.write('You take the car and head home. You just need some sleep.')
                                       st.write('Thank you for playing!')
                                       time.sleep(5)
                                       os.system('cls' if os.name == 'nt' else 'clear')
                                       sys.exit()
                             else:
                                  st.write('You decide that the best thing that you can do at this time is to wait for another car to drive by and ask for a ride.')
                                  st.write('You get comfortable and begin your long wait. After a while, you see a car off in the distance. But as they get closer, you begin to recognize it.')
                                  while True:
                                       get_away = st.text_input('You should probably get away. [Run, Stay] ', key='option16').strip().lower()
                                       if get_away in ['run', 'stay']:
                                            break

                                  if get_away.lower() == 'run':
                                       st.write ('You run through the trees, dodging sight as you go. You grow tired and begin to walk. After a while the trees clear and you see an old building.')
                                       st.write('You walk in to find a man waiting in a chair for you. "You made it!", he says.')
                                       while True:
                                            follow  = st.text_input('"Congradulations, I know you have questions, just follow me and all will be answered."[Follow, Refuse] ', key='option17').strip().lower()
                                            if follow in ['follow', 'refuse']:
                                                 break

                                       if follow.lower() == 'follow':
                                            st.write("You don't know who this man is, or what he wants, but you feel someting compelling you to follow.")
                                            st.write('Guess there is only one way to find out what is going on.')
                                            st.write('Thank you for playing!')
                                            time.sleep(5)
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            sys.exit()
                                       else:
                                            st.write('You begin to walk away, and you hear the man sigh. "You are free to leave, but you will never know why this happened if you do."')
                                            st.write("At this point, you don't even really want to know why, you just want to get home. A car is parked outside with the note, 'For your troubles.'")
                                            st.write('You take the car and head home. You just need some sleep.')
                                            st.write('Thank you for playing!')
                                            time.sleep(5)
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            sys.exit()
                                  else: 
                                       st.write ("The car doesn't stop. Turns out you plus a car plus a tree isn't a good match.")
                                       st.write('Thank you for playing!')
                                       time.sleep(5)
                                       os.system('cls' if os.name == 'nt' else 'clear')
                                       sys.exit()
                   elif fork.lower() == 'middle':
                        st.write('The road continues on leading you to what looks like an old broken building.')
                        st.write('You walk in to find a man waiting in a chair for you. "You made it!", he says.')
                        while True:
                             follow  = st.text_input('"Congradulations, I know you have questions, just follow me and all will be answered."[Follow, Refuse] ', key='option18').strip().lower()
                             if follow in ['follow', 'refuse']:
                                  break

                        if follow.lower() == 'follow':
                             st.write("You don't know who this man is, or what he wants, but you feel someting compelling you to follow.")
                             st.write('Guess there is only one way to find out what is going on.')
                             st.write('Thank you for playing!')
                             time.sleep(5)
                             os.system('cls' if os.name == 'nt' else 'clear')
                             sys.exit()
                        else:
                             st.write('You begin to walk away, and you hear the man sigh. "You are free to leave, but you will never know why this happened if you do."')
                             st.write("At this point, you don't even really want to know why, you just want to get home. A car is parked outside with the note, 'For your troubles.'")
                             st.write('You take the car and head home. You just need some sleep.')
                             st.write('Thank you for playing!')
                             time.sleep(5)
                             os.system('cls' if os.name == 'nt' else 'clear')
                             sys.exit()

                   else:
                        st.write('As you continue to drive, you begin to recognize where you are. After a bit longer, you find yourself pulling into your driveway.')
                        st.write('What a wild day.')
                        st.write('Thank you for playing!')
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sys.exit()
              else:
                   st.write('You hop out of the car and begin heading down a nearby road. Finally, after what seems like hours, you see an old, broken down building in the distance.')
                   st.write('You walk in to find a man waiting in a chair for you. "You made it!", he says.')
                   while True:
                        follow  = st.text_input('"Congradulations, I know you have questions, just follow me and all will be answered."[Follow, Refuse] ', key='option19').strip().lower()
                        if follow in ['follow', 'refuse']:
                             break

                   if follow.lower() == 'follow':
                        st.write("You don't know who this man is, or what he wants, but you feel something compelling you to follow.")
                        st.write('Guess there is only one way to find out what is going on.')
                        st.write('Thank you for playing!')
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sys.exit()
                   else:
                        st.write('You begin to walk away, and you hear the man sigh. "You are free to leave, but you will never know why this happened if you do."')
                        st.write("At this point, you don't even really want to know why, you just want to get home. A car is parked outside with the note, 'For your troubles.'")
                        st.write('You take the car and head home. You just need some sleep.')
                        st.write('Thank you for playing!')
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sys.ex    
                   
         elif intersection.lower() == 'left':
              st.write('Luckily the car in the intersection saw you, and stopped. The cars following you were able to make it aswell.')
              while True:
                   y_turn = st.text_input('You continue driving, and eventually come to a y in the road. A road to the right and to the left. The cars care still following you.[Left, Right] ', key='option20').strip().lower()
                   if y_turn in ['left', 'right']:
                        break

              if y_turn == 'left':
                   st.write('You floor it down the left road, and quickly find yourself facing an old building.')
                   st.write('The cars following you stop, and you decide to head inside.')
                   st.write('You walk in to find a man waiting in a chair for you. "You made it!", he says.')
                   while True:
                        follow  = st.text_input('"Congradulations, I know you have questions, just follow me and all will be answered."[Follow, Refuse] ', key='option21').strip().lower()
                        if follow in ['follow', 'refuse']:
                             break

                   if follow.lower() == 'follow':
                        st.write("You don't know who this man is, or what he wants, but you feel someting compelling you to follow.")
                        st.write('Guess there is only one way to find out what is going on.')
                        st.write('Thank you for playing!')
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sys.exit()
                   else:
                        st.write('You begin to walk away, and you hear the man sigh. "You are free to leave, but you will never know why this happened if you do."')
                        st.write("At this point, you don't even really want to know why, you just want to get home. A car is parked outside with the note, 'For your troubles.'")
                        st.write('You take the car and head home. You just need some sleep.')
                        st.write('Thank you for playing!')
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sys.exit()
              else: 
                   st.write('As you continue to drive, you begin to recognize where you are. After a bit longer, you find yourself pulling into your driveway.')
                   st.write('What a wild day.')
                   st.write('Thank you for playing!')
                   time.sleep(5)
                   os.system('cls' if os.name == 'nt' else 'clear')
                   sys.exit    
         else:
            #   Double quotes for doesn't and didn't
              st.write("Well, the car following you either doesn't have breaks, or they just don't like you")
              st.write('Thank you for playing!')
              time.sleep(5)
              os.system('cls' if os.name == 'nt' else 'clear')
              sys.exit()
    else: 
        #  Double quotes for didn't
         st.write("Lets just say that the other car didn't want to stop.")
         st.write('Thank you for playing!')
         time.sleep(5)
         os.system('cls' if os.name == 'nt' else 'clear')
         sys.exit()
  



                

else:
    st.write('As you turn your head to look at your surroundings, they seem to fade away and are replaced with a dark backdrop with what look like stars.')
    st.write('You look down at your hands and see you are now wearing a strange suit. All at once you realize, you are actually in space, and it looks like your ship is floating away.')
    while True:
         grab = st.text_input('There are two panels with bars in front of you, which one do you grab?[Left, Right] ', key='option22').strip().lower()
         if grab in ['left', 'right']:
              break

    if grab.lower() == 'left':
         st.write('The panel budges a bit, but holds. You begin to accelerate with your ship.')
         while True:
              door = st.text_input('You make your way to the main body, and you see three doors. Which one will you use? [Left, Middle, Right] ', key='option23').strip().lower()
              if door in ['left', 'middle', 'right']:
                   break

         if door.lower() == 'left':
              st.write('The door whips open to reveal what you recognize to be the cockpit. Time to get to work.')
              while True:
                   land = st.text_input('You take your seat at the front of the ship and see that the ship is accerating towards a planet. You can either try to land or redirect. [Land, Redirect] ', key='option24').strip().lower()
                   if land in ['land', 'redirect']:
                        break

              if land.lower() == 'land':
                   st.write('You steer the ship more directly at the planet. As you begin to enter the atmosphere, you feel the ship begin to strain.')
                   while True:
                        abort = st.text_input('Suddenly, something flies off the ship, hitting the cockpit and cracking it. [Abort, Continue] ', key='option25').strip().lower()
                        if abort in ['abort', 'continue']:
                             break

                   if abort.lower() == 'abort':
                        st.write('You try to turn the ship and see a wing strain under the pressure, then snap. You now see that the rest of the ship is not too far behind.')
                        st.write('Thank you for playing!')
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sys.exit()
                   else:
                        st.write('"It is too late now", you think to yourself.')
                        st.write('You do your best to hold the ship steady as it continues its rapid descent.')
                        while True:
                             gear = st.text_input('As the ground rapidly grows closer, you press the landing gear and find that the thing that must have flown off belonged to that system. You see a lush field and a lake. [Field, Lake] ', key='option26').strip().lower()
                             if gear in ['field', 'lake']:
                                  break

                        if gear.lower() == 'lake':
                             st.write('As the ship touches the water, the entire thing begins to shake rapidly. You hold it steady, and eventually it comes to a slow halt.')
                             st.write('You have no idea what to do next, but pray that there is an outpost somewhere nearby that you can use.')
                             st.write('Might as well get walking.')
                             st.write('Thank you for playing!')
                             time.sleep(5)
                             os.system('cls' if os.name == 'nt' else 'clear')
                             sys.exit()
                        else:
                             st.write('As soon as the ship touches the ground, it lurches forward and you realize that the tail is now rising about you. Turns out that the land was not quite as soft as it first seemed')
                             st.write('Thank you for playing!')
                             time.sleep(5)
                             os.system('cls' if os.name == 'nt' else 'clear')
                             sys.exit()
              else:
                   st.write('You steer the ship away, and are met with a large amount of flashing lights.')
                   while True:
                        problem = st.text_input('The two main issues are the main thrusters are shot and there is a fire in the cargo hold. [Thruster, Cargo] ', key='option27').strip().lower()
                        if problem in ['thruster', 'cargo']:
                             break

                   if problem.lower() == 'thruster':
                        st.write('You begin to make your way through the ship, and as you approach the thruster, you hear a loud bang.')
                        st.write('The next thing you see is your ship floating away, and you realize that the fire melted through the hull, causing a depressurization which pulled you out of the ship.')
                        st.write('Hopefully someone flies by soon, your oxygen is not doing too well')
                        st.write('Thank you for playing!')
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sys.exit()
                   else:
                        st.write('You rush to the cargo hold to find a raging inferno. The sensors in the room have been fried, which led them to make a bad warning.')
                        while True:
                             put_out = st.text_input('There is a fire extinguisher to your left, or the ships automated suppressant to your right [Extinguisher, Auto] ', key='option28').strip().lower()
                             if put_out in ['extinguisher', 'auto']:
                                  break

                        if put_out == 'auto':
                             st.write('You make your way to the switch, only to find that nothing happens when you pull it. It must have been fried to.')
                             st.write('You hear a loud bang as the hull gives out due to the heated metal and find yourself watching your ship drift away.')
                             st.write('Hopefully someone flies by soon, your oxygen is not doing too well')
                             st.write('Thank you for playing!')
                             time.sleep(5)
                             os.system('cls' if os.name == 'nt' else 'clear')
                             sys.exit()
                        else: 
                             st.write('You reach the fire extinguisher and pull the pin. The foam rockets out as you douse the entire area. At long last, the fire putters out and the ship rests.')
                             st.write('With that done, all that is left is the thruster. You start back.')
                             while True:
                                  fix = st.text_input('As you enter the thruster room, you see that the thruster has a piece of metal lodged inside of the main reactor. You can pull it out or push it in. [Pull, Push] ', key='option29').strip().lower()
                                  if fix in ['push', 'pull']:
                                       break

                             if fix == 'pull':
                                  st.write('You pull the metal out. As you do, you see sparks flying off the rubbing metal.')
                                  st.write('You hear a loud bang, and find yourself outside of the ship. The spark must have hit the gas, causing an explosion, and in turn, a depressurization.')
                                  st.write('Hopefully someone flies by soon, your oxygen is not doing too well')
                                  st.write('Thank you for playing!')
                                  time.sleep(5)
                                  os.system('cls' if os.name == 'nt' else 'clear')
                                  sys.exit()
                             else:
                                  st.write('You push the metal in and hear a clank. You look closer and see the metal is now pressed against the hole, effectively clogging it.')
                                  st.write('Huh. Lucky.')
                                  st.write('With that done, you head back to the cockpit and begin a course to the nearest station. Hopefully the ship holds until then.')
                                  st.write('Thank you for playing!')
                                  time.sleep(5)
                                  os.system('cls' if os.name == 'nt' else 'clear')
                                  sys.exit()
         elif door.lower() == 'middle':
              st.write('The door opens and you find yourself looking into what appears to be a cargo hold. A raging fire is engulfing most of the room.')
              while True:
               put_out = st.text_input('There is a fire extinguisher to your left, or the ships automated supressent to your right [Extinguisher, Auto] ', key='option30').strip().lower()
               if put_out in ['extinguisher', 'auto']:
                    break

               if put_out == 'auto':
                    st.write('You make your way to the switch, only to find that nothing happens when you pull it. It must have been fried to.')
                    st.write('You hear a loud bang as the hull gives out due to the heated metal and find yourself watching your ship drift away.')
                    st.write('Hopefully someone flies by soon, your oxygen is not doing too well')
                    st.write('Thank you for playing!')
                    time.sleep(5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    sys.exit()
               else: 
                    st.write('You reach the fire extinguisher and pull the pin. The foam rockets out as you douse the entire area. At long last, the fire putters out and the ship rests.')
                    st.write('You head to the cockpit, and are met with a flashing warning about the truster. You immediately head back to check it out.')
                    while True:
                         fix = st.text_input('As you enter the thruster room, you see that the thruster has a piece of metal lodged inside of the main reactor. You can pull it out or push it in. [Pull, Push] ', key='option31').strip().lower()
                         if fix in ['push', 'pull']:
                              break

                    if fix == 'pull':
                         st.write('You pull the metal out. As you do, you see sparks flying off the rubbing metal.')
                         st.write('You hear a loud bang, and find yourself outside of the ship. The spark must have hit the gas, causing an explosion, and in turn, a depressurization.')
                         st.write('Hopefully someone flies by soon, your oxygen is not doing too well')
                         st.write('Thank you for playing!')
                         time.sleep(5)
                         os.system('cls' if os.name == 'nt' else 'clear')
                         sys.exit()
                    else:
                         st.write('You push the metal in and hear a clank. You look closer and see the metal is now pressed against the hole, effectivly clogging it.')
                         st.write('Huh. Lucky.')
                         st.write('With that done, you head back to the cockpit and begin a course to the nearest station. Hopefully the ship holds until then.')
                         st.write('Thank you for playing!')
                         time.sleep(5)
                         os.system('cls' if os.name == 'nt' else 'clear')
                         sys.exit()
         else:
              st.write('This ship has some really unfortunately placed drawers')
              st.write('Thank you for playing!')
              time.sleep(5)
              os.system('cls' if os.name == 'nt' else 'clear')
              sys.exit() 
    else:
         st.write('The panel whips open, and is torn off with the force. Who decided that this was a good place for a drawer?')
         st.write('Thank you for playing!')
         time.sleep(5)
         os.system('cls' if os.name == 'nt' else 'clear')
         sys.exit

        





# # Double quotes so that I can use don't
# st.write ("You groggily look around. You don't remember what happened or how you got here, but here you are.")
# st.write('In front of you lies three objects, a sword, a toy car, and what looks like a lazer gun. It is obvious that you are suppossed to pick one.')

# # Picking their story
# while True:
#      story_choice = st.text_input('Which one will you choose?[Sword, Toy Car, Lazer Gun] ', key='option0').strip().lower()
#      if story_choice in ['sword', 'toy car', 'lazer gun']:
#           break
#      else:
#           st.write('Invalid choice, please enter Sword, Toy Car, or Lazer Gun.')

# if story_choice.lower() == 'sword':
#      the_knight()
# elif story_choice.lower() == 'toy car':
#      the_getaway()
# else:
#      space_walk()







