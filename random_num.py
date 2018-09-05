import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passnum = int(input("number of passwords--> "))
length = int(input("password legnth------> "))
for p in range(passnum):
  password = ""
  for c in range(length):
    password += random.choice(chars)
  print(password)


