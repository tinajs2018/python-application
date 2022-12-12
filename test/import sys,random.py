import sys,random
print('Welocme to the syche game of wiining the best name')
firt=('megga','wex','tina','max')
last=('landmere','kuria','landia','rabbitman')
while True:
    firstname=random.choice(firt)
    lastname =random.choice(last)
    print('\n\n')
    print('{}{}'.format(firstname,lastname),file=sys.stderr)
    print('\n\n')
    try_again=input('\n\n Try again?(Press Enter else n to quit)\n')
    if try_again.lower() =='n':
        break
    input('\n Press Enter to exit')