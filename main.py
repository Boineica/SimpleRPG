HP = 3
WHP = 3
S = 0
name = input('What is your name?\n')
print('Hi, %s!' % name )

ar1 = input('A Wolf tries to attack you, what will you do?\nDefend or attack?\n')
print('.')
print('..')
print('...')
input == ('Attack')
print('You attacked the wolf, the wolf attacks you again.\nYour HP: 2\nThe wolfs HP: 2')
HP = 2
WHP = 2
input == ('Defend')
print('Actually, you dont have a shield, you use your arms instead.\nYou lose 1 HP\nYour HP: 2\nThe wolfs HP: 3')
HP = 2

ar2 = input('\nThe wolf attacks you again.\nAttack, Defend or Look in the water?\n')
print('.')
print('..')
print('...')
input == ('Attack')
print('You and the wolf are almost dying.💀💀💀💀')
HP = 1
WHP = 1
input == ('Defend')
print('YOU DONT HAVE A SHIELD YET!\nYOU ARE ALMOST DEAD!💀💀')
HP = 1
input == ('Look')
print('You just found a hidden choice!\n Its an easter egg!') # if you found this in the code, congratulations!
print('.')
print('..')
print('...')
print('You just found a shield.')
S = 1

ar3 = input('what will you do?\n')
print('.')
print('..')
print('...')
input == ('Attack')
HP = 0
WHP = 0
input == ('Defend') and S == 1
print('You avoided the wolfs attack!')
input == ('Defend') and  S == 0
HP = 0
input == ('Throw a stone') # An easter egg
WHP = 0.5
print('Whoa, the wolf is almost dead!')