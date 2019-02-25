

class Gun:
    
    def __init__(self, name, fire_range):
        self.name = name
        self.fire_range = fire_range
        self.ammo = 15

    def __repr__(self):
        return f'{self.name}, Range:{self.fire_range}'

    
def player_info(self):
    self.player_name = input('Enter your name: ')
    print('Hey ' + self.player_name + ' i hope that you  are ready for the journey but first')
    self.player_age = int(input('what is your age: '))
    if self.player_age < 13:
        print('system not ready at this time')
        exit()
    else:
        print('Once again welcome to Fire Rangers ' + self.player_name + ' now are you ready to take down the enemy?')
       

def gun_info():
    gun_choice = []
    gun_list = ['Handgun', 'Machinegun', 'Shotgun', 'Sniper']
    gun_details = {
        "Handgun" : 'Handgun: is a small gun with fire range of 5 feet',
        "Machinegun" : 'Machinegun: is a medium range gun approximately 7 feet',
        "Shotgun" : 'Shotgun: has a fair range of 8 feet',
        "Sniper" : 'Sniper: has a long range of 10 feet'
    }
    for i in gun_list:
        print(i)
    pick = input('pick a gun: ').capitalize()
    gun_choice.append(pick)
    if pick in gun_list:
        question = input('Nice choice!\n' + 'would you like to know about that gun? y/n ').lower()
        if question == 'y':
            print(gun_details.get(pick))
        else:
            print('lets start the game')
    else:
        print('does not match our record')
        exit()


def start():
        gun = {
        'Handgun': {
            'fire_range': 5,
        }, 
        'Machinegun': {
            'fire_range': 7,
        },
        'Shotgun': {
            'fire_range': 9,
        },
        'Sniper': {
            'fire_range': 10,
        }
    }
        gun_choice = ['Handgun', 'Machinegun', 'Shotgun', 'Sniper']
        instruction = 'Remember: you can only use each gun once. after you use it gun will be unavailable'
        print(instruction)
        for x in gun_choice:
            print(x)
        challenge_1 = input('you have a Bird that is running 5 feet ahead. which gun would you pick to shoot it: ').title()
        bird = 5 
        if challenge_1 in gun_choice:
            if gun[challenge_1]['fire_range'] >= bird:
                gun_index = gun_choice.index(challenge_1)
                gun_choice.pop(gun_index)
                print('You win')
        else:
            print('Not in the list...try again')
    
        for x in gun_choice:
            print(x)
        challenge_2 = input('Next challenge: you have a deer that is 8 feet away: which gun would you pick to shoot it: ').title()
        deer = 8
        if challenge_2 in gun_choice:
            if gun[challenge_2]['fire_range'] >= deer:
                gun_index = gun_choice.index(challenge_2)
                gun_choice.pop(gun_index)
                print('You win')
            else:
                print("The range is too short")
                exit()
        else:
            print('Not in the list...try again')

        for x in gun_choice:
            print(x)
        challenge_3 = input('Next challenge: you have a bear that is 6 feet away: which gun would you pick to shoot it: ').title()
        bear = 6
        if challenge_3 in gun_choice:
            if gun[challenge_3]['fire_range'] >= bear:
                gun_index = gun_choice.index(challenge_3)
                gun_choice.pop(gun_index)
                print('You win')
            else:
                print("The range is too short")
                exit()
        else:
            print('Not in the list...try again')

        for x in gun_choice:
            print(x)
        challenge_4 = input('Next challenge: you have a zebra that is 10 feet away: which gun would you pick to shoot it: ').title()
        zebra = 10
        if challenge_2 in gun_choice:
            if gun[challenge_4]['fire_range'] >= zebra:
                gun_index = gun_choice.index(challenge_4)
                gun_choice.pop(gun_index)
                print('You win')
            else:
                print("The range is too short")
                exit()
        else:
            print('Congratulation....you won the game')
            exit()


            

class GameUI:

    def __init__(self):
        self.choices = {
            "1" : player_info,
            "2" : gun_info,
            "3" : start,
            "4" : exit
        }

    def player_info(self):
        self.player_name = input('Enter your name: ')
        print('Hey ' + self.player_name + ' thanks for joining our ranks but before we go anyfurther...')
        self.player_age = int(input('what is your age: '))
        if self.player_age < 13:
            print('system not ready at this time')
            exit()
        else:
            print('Once again welcome to Fire Rangers ' + self.player_name + ' now are you ready to take down the enemy?')

    def main(self):
        while True:
            print('Fire Rangers demo')
            user_input = input('1. Player Info\n' +
                            '2. Gun Info\n' +
                            '3. start\n' +
                            '4. Exit\n')
            action = self.choices.get(user_input)
            if action:
                action()
            else:
                print("Input not valid")

    def run(self):
        
        self.player_info()
        self.main()


if __name__ == "__main__":
    gui = GameUI()
    gui.run()