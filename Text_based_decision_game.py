from random import shuffle


class menu():
        
                print("*" * 70)
                print("Welcome Political Warfare!" .center(70))
                print("*" * 70)
                print("The objective is to either start or postpone nuclear war." .center(70))
                print("On each turn, the player will be asked a question." .center(70))
                print("The player must respond to the question in the way that suits them." .center(70))
                print("If the User is USA, GB or Germany, they are expected to make good choices" .center(70))
                print("But if they are, Russia, Saudi Arabia, NK then they are expected to pick bad choices" .center(70))
                print("After the end of one event, another will begin" .center(70))
                print("There's also a Doomsday clock" .center(70))
                print("This is affected by everyone's choices, it deterimines the outcome of the game" .center(70))
                print(" Good luck! " .center(70, "*"))
                print(" Remember " .center(70, "*"))
                print(" Fortune favors the brave... " .center(70, "*"))
                print(" but chance favors the smart! " .center(70, "*"))
                print("I will now decide who starts" .center(70, " "))
              
#############################################################################             
def input_number(prompt='Please enter a number: ', minimum=0, maximum=None):

    while True:
        try:
            number = int(input(prompt))
            if (number < minimum or
                (maximum is not None and number > maximum)):
                    print('Number is not within range: {} to {}'.format(minimum, maximum))              #incomplete
            else:
                break

        except ValueError:
            print('You need to enter a number')
            continue

    return number ###### how many players they want in the game

def main():
    human_players = input_number('How many human players? ')
    computer_players = input_number('How many computer players? ')

    game_manager = GameManager(human_players, computer_players)
    game_manager.play_game()

#################################################################################

#A tree is being used to sort out the questions
tree = {"Event":"Missiles are being created in cuba",#This is the event, it is then followed by many questions
        "q1":{"Response":"What should the you do?","options":[("1. Send stern warnings",(-2,"q3")),("2. send an airstrike",(-5,"q2")),("3. Send a nuke",(4,"q7"))]},
        #"q2" "q3" are the questions that should be played next
        #Each question has either 2 or more responses to it
        "q2":{"Response":"You've been attacked","options":[("1. Fire back",(4,"q4")),("2. Don't fire back, look for peace but with precaution",(-2,"q6"))]},
        #Each response sends the player or players to a certain question and situation within this tree
        "q3":{"Response":"You've been given stern warnings","options":[("1. Choose to ignore and keep creating",(4,"q5")),("2. Stop creating",(-2,"q6"))]},
        #The numbers behind ',q' symbolise the amount of points that are either added or deducted from the clock
        "q4":{"Response":"Russia fired back","options":[("1. Send a nuke",(4,"q8")),("2. Nuke a part of Russia",(-2,"q7"))]},
        "q5":{"Response":"Russia is still creating","options":[("1. propose a treaty",(4,"q6")),("2. Send nukes",(-2,"q8"))]},
        "q6":{"Response":"Russia is no longer creating and is looking for peace","options":[("1. Make peace",(1,"q12")),("2. Time's up, send nuke",(-1,"q2"))]},
        "q7":{"Response":"The US has sent another missle","options":[("1. Fire back with another nuke",(1,"q4")),("2. Stop now and make peace",(-1,"q6"))]},
        "q8":{"Response":"A part of your country has been nuked","options":[("1. Nuke back",(1,"q9")),("2. Make peace",(-1,"q6"))]},
        "q9":{"Response":"Russia just nuked you","options":[("1. Send a nuke",(1,"q10")),("2. Ask for peace right now",(-1,"q11"))]},
        "q10":{"Response":"America has retaliated with a nuke","options":[("1. Send another nuke",(1,"q9")),("2. Ask for peace right now",(-1,"q6"))]},
        "q11":{"Response":"America just asked for peace","options":[("1. Stop attacking and go back to creating",(1,"q5")),("2. Make peace",(-1,"q6"))]},
        "q12":{"Response":"End Of Event","options":[("1. Start next Event",(1,"NextEvent")),("2. End game",(-1,"EndGame"))]},
        #q12 is symbolising the end of this current event
        }

tree2 = {"Event":"British Spy found in Saudi Arabia",
        "q1":{"Response":"What would you like to do with the spy","options":[("1. Hang him",(-5,"q2")),("2. Imprison",(-2,"q3"))]},
        "q2":{"Response":"Saudi Arabia has called for a hanging","options":[("1. Be stern and cut ties",(4,"q4")),("2. Campaign for imprisonment instead",(-2,"q5"))]},
        "q3":{"Response":"Spy will go to prison","options":[("1. make negotiations to bring back",(4,"q6")),("2. Cut trading to bring back",(-2,"q4"))]},
        "q4":{"Response":"Britain has cut ties","options":[("1. dont care and hang",(4,"q10")),("2. delay hanging",(-2,"q11"))]},
        "q5":{"Response":"Britain is campaigning for imprisonment","options":[("1. imprison",(4,"q3")),("2. still execute",(-2,"q10"))]},
        "q6":{"Response":"Britain wants negotiations to get spy back","options":[("1. No",(1,"q7")),("2. okay",(-1,"q8"))]},
        "q7":{"Response":"Saudi Arabia will keep spy","options":[("1. accept fault",(1,"q12")),("2. never give up",(-1,"q4"))]},
        "q8":{"Response":"Saudi Arabia will give spy back","options":[("1. Make peace and apoligise",(1,"q12")),("2. Make peace and apoligise",(-1,"q6"))]},
        "q9":{"Response":"Saudi Arabia finally imprisoned the spy","options":[("1. Say thank you and end",(1,"q12")),("2. Push forward for spy back",(-1,"q12"))]},
        "q10":{"Response":"Saudi Arabia has done the execution","options":[("1. Move on",(1,"q12")),("2. Denounce  Saudi Arabia",(-1,"q12"))]},
        "q11":{"Response":"Saudi Arabia has delayed the hanging","options":[("1. Push for saviour",(1,"q5")),("2. Leave it as it is",(-1,"q12"))]},
        "q12":{"Response":"End of crisis","options":[("1. Start next Event",(1,"Event2")),("2. End game,",(-1,"q"))]},
          }

tree3 = {"Event":"Russia caught stealing arms from Germany",
        "q1":{"Response":"Russia stole from you","options":[("1. Stop trading arms",(-5,"q3")),("2. fine russia",(-2,"q2"))]},
        "q2":{"Response":"Germany has stopped trading arms","options":[("1. Work towards getting arms back",(4,"q5")),("2. retaliate with removing gasses",(-2,"q2"))]},
        "q3":{"Response":"Russia wants to make ties","options":[("1. make negotiations to bring back",(4,"q5")),("2. Cut trading to bring back",(-2,"q5"))]},
        "q4":{"Response":"Russia has stopped sharing their natural gasses","options":[("1. dont care and hang",(4,"q8")),("2. delay hanging",(-2,"q7"))]},
        "q5":{"Response":"Youve been sent a fine","options":[("1. imprison",(4,"q8")),("2. still execute",(-2,"q12"))]},
        "q6":{"Response":"Make negotiatians with Russia","options":[("1. No",(1,"q7")),("2. okay",(-1,"q10"))]}, 
        "q7":{"Response":"Russia won't pay fine","options":[("1. accept fault",(1,"q4")),("2. never give up",(-1,"q6"))]},
        "q8":{"Response":"Germany gave its arms back","options":[("1. Make peace and apoligise",(1,"q12")),("2. Make peace and apoligise",(-1,"q12"))]},
        "q9":{"Response":"Other countries have been set up against you","options":[("1. Say thank you and end",(1,"q6")),("2. Push forward for spy back",(-1,"q12"))]},
        "q10":{"Response":"Germany has stopped trading completely","options":[("1. Give up",(1,"q4")),("2. Cut gasses ",(-1,"q12"))]},
        "q11":{"Response":"Russia paid fine","options":[("1. pay fine",(-1,"q12"))]},
        "q12":{"Response":"End of crisis","options":[("1. Start next Event",(1,"Event2")),("2. End game,",(-1,"q"))]},}

event_list = [tree,tree2,tree3]


DoomsdayClock = 25
#Clock is set to 25

class Country(object):
#A class for the countries is created
        def __init__(self,name):
                self.name = name
                self.score = 0

        def add_score(self, player_score):
                #will add player score to total score

                self.score += player_score

        def __str__(self):
                #returns player name and current score

                return str(self.name) + ": " + str(self.score)

         

     #the bottom part is the ai, ----> needs creating <----
'''  
class ComputerPlayer(Country):
        cpu_names=['CP1', 'CP2', 'CP3']
        
        def __init__(self, number):
        #Assigns a cpu name from cpu_names
                self.personality_type = "insane"
                if number < len(self.cpu_names):
                    name = self.cpu_names[number]
                else:
                    name = 'Cpu{}'.format(number)
                super(ComputerPlayer, self).__init__(name)

        def pick_options(self,options):
            #you need to rearrange tree to have options in correct scenarios e.g. [peaceful][warlike]
            #if peaceful personality -> work out which option is best for reducing doomsday, and pick that          
            #if insanse -> randomly pick option
            #if warlike -> pick options to go to war...
            
            
            #from random import *
             int ran=randint(1,3);
            
                '''
                
p1 = Country("UNITED STATES")                
p2 = Country("GREAT BRITAIN")                
p3 = Country("GERMANY")
#The countries are declared here, 3 good countries


p4 = Country("RUSSIA")
p5 = Country("NORTH KOREA")
p6 = Country("SAUDI ARABIA")
#And 3 bad countries

players = [p1,p4]  
#currently only playing with 2 countries


q = "q1" # this is the starting Q
curr_ev_counter = 0
tree = event_list[curr_ev_counter]

print(tree["Event"])
gamePlaying = True
#print out the event
while gamePlaying:
        #loop -> likely to be loop through players
    print("")
    print("THE CLOCK IS CURRENTLY AT "+str(DoomsdayClock))
    for player in players:
                print("")
                print(player.name+" it is your turn")
    
                print(tree[q]["Response"])
                #print the response to the event
                for opt in tree[q]["options"]:
                        #loop through all options
                    print(opt[0])
                    #display the option
                #if country.is_player then ask for options
                select_opt = int(input("Which option do you want to select? "))-1
                while select_opt not in (range(len(tree[q]["options"]))):
                        print("Enter a valid number")
                        select_opt = int(input("Which option do you want to select? "))-1
                #otherwise call country.pick_option() -> Pass in the options it has


                #"q4":{"Response":"Russia fired back","options":[("1. Send a nuke",(4,"q7")),("2. Nuke a part of Russia",(-2,"q8"))]},

                #get the user to type the number in -> VALIDATE!
                print("You have chosen "+tree[q]["options"][select_opt][0])
                #output chosen (could have confirmation if you have time
                clock_mod = tree[q]["options"][select_opt][1][0]
                #get the clock modifier based on the response chosen
                q = tree[q]["options"][select_opt][1][1]
                #get the next question based on the response chosen
                DoomsdayClock = DoomsdayClock+clock_mod
                print("Q is "+q)
                if q == "NextEvent":
                    curr_ev_counter += 1
                    tree = event_list[curr_ev_counter]
                    q = "q1"
                    print(tree["Event"])
                elif q == "EndGame":
                    gamePlaying = False
                    
                if DoomsdayClock > 50:
                    gamePlaying = False
            


    #Main Game Loop
if DoomsdayClock <= 20:
    print("The world has fully disarmed. Everyone Wins")
elif DoomsdayClock <= 40:
    print("The world keeps on turning but the shadow of war is never far away...")
elif DoomsdayClock <= 50:
    print("The world is on the brink of nuclear war...")
else:
    print("The world is doomed. Everyone Loses")

 

