#I import the time for use with the Sleep function, to create small time gaps between each line generated.
import time

print("Welcome to the Jungle!")
player_name = input("Please enter your Player Name: ")
print("""
""")

print("Thanks " + player_name + "!")
print("""
""")

time.sleep(1)

age = input("Please enter your age: ")
print("""
""")

if int(age) >= 18:
  print("You are old enough to play!")
  print("""
""")
else:
  print("Sorry, you need to be 18+ to play this game!")
  time.sleep(3)
  print("""
  """)
  print("Goodbye")
  time.sleep(1)
  exit()

#The sections above are the intro to the game, asking for Name and Age, which may be used further down the line.

#The base stats are created; Health keeps you alive, Stamina keeps you fit, Sanity keeps you healthy, armour keeps you safe, and damage makes you strong.

health = 100
stamina = 50
sanity = 20
armour = 0
damage = 0

#Here the players get a choice for some starting equipment, being either Armour or a Sword.

time.sleep(2)

starter = input("To start the game, would you like to choose the Leather Armour, or the Bronze Blade? Type 'B' for the blade, or 'A' for the armour: ")
print("""
""")

if starter=="A":
  armour = 10
  print("Your Armour has been increased to 10")
  print("""
  """)
  time.sleep(2)
elif starter=="a":
  armour = 10
  print("Your Armour has been increased to 10")
  print("""
  """)
  time.sleep(2)
elif starter=="B":
  damage = 10
  print("Your Damage has been increased to 10")
  print("""
  """)
  time.sleep(2)
elif starter=="b":
  damage = 10
  print("Your Damage has been increased to 10")
  print("""
  """)
  time.sleep(2)
else:
  print("Sorry! We did not recognise your choice.")
  print("""
  """)
  time.sleep(1)
  starter = input("To start the game, would you like to choose the Leather Armour, or the Bronze Blade? Type 'B' for the blade, or 'A' for the armour: ")
  print("""
""")

#Sleep function to create small time gaps. The number in the brackets signifies the amount of seconds it will wait for.
time.sleep(2)

print("You begin approaching the Jungle (is massive).")
print("""
""")

time.sleep(2)

#Armour protects you from the thick thorns and branches
if armour >= 10:
  print("As you enter the Jungle, your armour helps defend against the thick branches of thorns that seem to surround it.")
  print("""
        """)
  time.sleep(3)

#You take damage from this if you don't take the armour.
else:
  print("The thick thorns and branches hurt to move through them. You take 5 points of damage.")
  health = health - 5
  print("You have " + str(health) + " remaining health.")
  print("""
  """)
  time.sleep(3)


#This is where the journey truly begins. Left will take you through the standard forest, and Right will lead you towards a tribe of forest folk.
print("You see 2 paths ahead. To the left, you see a very slight path through the trees and bushes. To the right, tracks that lead down a slightly more obvious pathway.")

print("""
""")

time.sleep(3)

left_right = input("Which way would you like to go? Type 'L' for Left, or 'R' for Right: ")

print("""
""")

#if left_right == "L" or "l":
  #open Feral Path script
  
#if left_right == "R" or "r":
  #open Feral Path script