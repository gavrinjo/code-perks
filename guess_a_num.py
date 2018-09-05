
secret_word = input("tajna riječ :")
word = ""
guess_count = 0
guess_limit = 3
guess_runout = False
game_over = """\n
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
"""
victory = """
 ██▒   █▓ ██▓ ▄████▄  ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓ ▐██▌  ▐██▌ 
▓██░   █▒▓██▒▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒ ▐██▌  ▐██▌ 
 ▓██  █▒░▒██▒▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░ ▐██▌  ▐██▌ 
  ▒██ █░░░██░▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░ ▓██▒  ▓██▒ 
   ▒▀█░  ░██░▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░ ▒▄▄   ▒▄▄  
   ░ ▐░  ░▓  ░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒  ░▀▀▒  ░▀▀▒ 
   ░ ░░   ▒ ░  ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░  ░  ░  ░  ░ 
     ░░   ▒ ░░          ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░      ░     ░ 
      ░   ░  ░ ░                   ░ ░     ░     ░ ░      ░     ░    
     ░       ░                                   ░ ░                 
"""

def clear():
	import os
	os.system("cls" if os.name == "nt" else "clear")

#clear()
print("\n"*100)
print("""
____________________
|Pogodi tajnu riječ|
|------------------|
|-----pravila.-----|
|------------------|
|-imaš 3 pokušaja.-|
|----nakon toga----|
|----GAME OVER!----|
|__________________|
""")


while word != secret_word and not guess_runout:
  if guess_count < guess_limit:
    word = input("pokušaj br." + str(guess_count+1) + ": ")
    guess_count += 1
  else:
    guess_runout = True


if guess_runout:
  print(game_over)
else:
  print(victory)