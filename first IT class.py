from msvcrt import getch
keyDown = ord(getch())
while True:
    print('Welcome to pythag calc')
    d = input('Press any key to continue')
    x = int(input('Enter your First number here: '))
    y = int(input('Enter your second number here: '))
    def z():
        z = x**2 + y**2
        return z
    print('Your last number is: ', z())
    
