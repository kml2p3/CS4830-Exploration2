import datetime

name = raw_input("What is your name: ")
age = int(input("How old are you: "))
thisYear = int(datetime.date.today().strftime("%Y"))
year = str((thisYear-age)+100)
print(name+" will turn 100 years old in the year "+year)