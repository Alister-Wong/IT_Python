import datetime
now = datetime.datetime.now().year

name=input('What is your name?')
year=int(input('What year were you born in?'))

print("So young", name, "you are", now - year, "years old")
