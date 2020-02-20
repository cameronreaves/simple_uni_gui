import PySimpleGUI as sg
import random


#Set Rules
start_hand = 3
card_types = [1, 2, 3, 4, 5]
size = 100



def type_switch(argument):
    switcher = {
        1: Unicorn(),
        2: Instant(),
        3: Magic(),
        4: Upgrade(),
        5: Downgrade()
    }
    return(switcher.get(argument))



# Deck / Piles

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(size):
            type = random.sample(card_types, 1)
            self.deck.append(type_switch(type[0]))

    def from_top(self):
        return self.deck.pop()

    def to_deck(self,card):
        self.deck.insert(random.randint(0, len(self.deck)),card)

class Trash:
    def __init__(self):
        self.trash = []

    def from_top(self):
        return self.trash.pop()

    def to_trash(self,card):
        self.trash.insert(random.randint(0, len(self.trash)),card)

    def show_trash(self):
        for t in self.trash:
            print(t)


#   Cards

class Card:

    def __init__(self, ):
        self.name = "card"

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

class Unicorn(Card):
    def __init__(self):
        self.name = "Unicorn"

class Instant(Card):
    def __init__(self):
        self.name = "Instant"

class Magic(Card):
    def __init__(self):
        self.name = "Magic"

class Upgrade(Card):
    def __init__(self):
        self.name = "Upgrade"

class Downgrade(Card):
    def __init__(self):
        self.name = "Downgrade"

# Player

class Player:
    def __init__(self, name):
        self.hand = []
        self.my_stable = Stable()
        self.name = name
        for i in range(start_hand):
            self.hand.append(main_deck.from_top())

    def __str__(self):
        return self.name

    def draw_deck(self):
        self.hand.append(main_deck.from_top())

    def draw_trash(self):
        if len(main_trash.trash) > 0:
            self.hand.append(main_deck.from_top())
        else:
            print("Sorry there is no trash")

    def from_hand_to_deck(self,card):
        new = self.check_and_take(card)
        if new:
            main_deck.to_deck(new)
            return True
        else:
            return False

    def from_hand_to_trash(self,card):
        new = self.check_and_take(card)
        if new:
            main_trash.to_trash(new)
            return True
        else:
            return False

    def put_stable(self, card):
        new = self.check_and_take(card)
        if new:
            self.my_stable.stable.append(new)
            return True
        else:
            return False

    def show_hand(self):
        for h in self.hand:
            print(h)

    def get_hand(self):
        return self.hand

    def show_stable(self):
        for s in self.my_stable.stable:
            print(s)

    def check_stable(self):
        types = ["Unicorn", "Upgrade", "Downgrade", "Magic"]
        u_count = 0
        up_count = 0
        down_count = 0
        m_count = 0
        i_count = 0
        for s in self.my_stable.stable:
            if str(s) == types[0]:
                u_count += 1
            elif str(s) == types[1]:
                up_count += 1
            elif str(s) == types[2]:
                down_count += 1
            elif str(s) == types[3]:
                m_count += 1
            else:
                i_count += 1

        counts = [u_count, up_count, down_count, m_count, i_count]
        return counts


#   goes through a players hand and looks for that card, deletes that card from the hand and then returns it
    def check_and_take(self, card_name):
        for i in range(len(self.hand)):
            if self.hand[i].get_name() == card_name:
                card =  self.hand[i]
                del self.hand[i]
                return card

    def steal_my_from_stable(self,card_name):
        if len(self.my_stable.stable) > 0:
            for i in range(len(self.my_stable.stable)):
                if self.my_stable.stable[i].get_name() == card_name:
                    card = self.my_stable.stable[i]
                    del self.my_stable.stable[i]
                    main_trash.to_trash(card)
                    return True
        return False

    def instant_play(self):
        main_trash.to_trash(self.my_stable.stable.pop())

    def reduce_hand(self):
        limit = 1
        self.hand = self.hand[0:limit]




# Stable

class Stable:
    def __init__(self):
        self.stable = []


def update_hands(i, player):
    #first player in the player list assigned to hand 1
    if i == 0:
        j = 1
        for card in player.get_hand():
            window['h_1' + str(j)].update([str(card)])
            j = j + 1
    else:
        j = 1
        for card in player.get_hand():
            window['h_2' + str(j)].update([str(card)])
            j = j + 1



#GAME


#Initializing Game

main_deck = Deck()
main_trash = Trash()
players = []

#Create players for the game
players.append(Player("Cam"))
players.append(Player("Naomi"))

#Logicals
run = True
down = False
magic = False
instant = False


##Layout of GUI
num = 5

stable_1 = [[sg.Text("",size=(10,1), key="st_1" + str(i))] for i in range(1, num)]
stable_2 = [[sg.Text("",size=(10,1), key="st_2" + str(i))] for i in range(1, num)]

hand_1 = [[sg.Text("",size=(10,1), key="h_1" + str(i))] for i in range(1, num)]
hand_2= [[sg.Text("",size=(10,1), key="h_2" + str(i))] for i in range(1, num)]


col = [
        [sg.Button('Unicorn', key = "-UNI-")],
        [sg.Button('Magic', key = "-MAG-")],
        [sg.Button('Upgrade', key = "-UP-")],
        [sg.Button('Downgrade', key = "-DOWN-")],
        [sg.Button('Instant', key = "-INST-")],
       ]


layout = [
          [sg.Column(col),
           sg.Frame('STABLE 1', stable_1, font='Any 12', title_color='blue'),
           sg.Frame('STABLE 2', stable_2, font='Any 12', title_color='blue')],

         [sg.Frame('HAND 1', hand_1, font='Any 12', title_color='blue'),
           sg.Frame('HAND 2', hand_2, font='Any 12', title_color='blue'),
         sg.Text("It's Your Turn, Naomi", size=(15,1))],

        [sg.Button('Press Start', key = "-START-"),sg.Text(" ", key="-MSG-") ]
         ]

window = sg.Window('Unicorns GUI', layout, font=("Helvetica", 12))



while(run):  # Event Loop
    for i in range(len(players)):
        turn = True
        # makes sure that the player doesn't draw again if she inputs the wrong card name
        new_turn = True
        ##turn
        while(turn):
            event, values = window.read()
            ply = players[i]
            print(ply)
            ply.show_hand()
            update_hands(i, ply)
            #checks if button / exit clicked
            if event in  (None, 'Exit'):
                break
            #if player presses Unicorn button
            if event == '-UNI-':
                suc = ply.put_stable("Unicorn")
                if suc:
                    #display unicorn on the board
                    window['st_11'].update(["Unicorn"])
                    turn = False
                    break
                else:
                    window['-MSG-'].update(["Card not in your hand"])
                    new_turn = False
            if event == '-MAG-':
                # Update the "output" text element to be the value of "input" element
                window['st_11'].update("Gone")
                turn = False
                break

window.close()


