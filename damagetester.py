# Damage Tester v1.1 by KNB_The_Noob_1
#
# - NEW: Added messages when player HP is full or player has fainted
# - Lots of bugfixes
# - Resorting to integers for more "stable" outputs haha
#
# End of changelog

# Hello everyone and welcome to another video!

print("\nDamage Tester v1.1 by KNB_The_Noob_1")
print("\nNote that damage values are INTEGERS!")

# Assign Player 1 and 2 base HP values

player_1_hp = int(100)
player_2_hp = int(100)

# And print out that value:

print ("\nPlayer 1's starting HP value is: ")
print (player_1_hp)

print ("\nPlayer 2's starting HP value is: ")
print (player_2_hp)

# Assign damage and heal values to respective players:

damageP1 = int(input ("\nP1 damage taken (in HP): "))
damageP2 = int(input ("\nP2 damage taken (in HP): "))

healP1 = int(input ("\nP1 healed x HP: x="))
healP2 = int(input ("\nP2 healed x HP: x="))

# Add and subtract 'em up!

resultP1 = player_1_hp - damageP1 + healP1
resultP2 = player_2_hp - damageP2 + healP2

# NEW: Checks for conditions

# Player 1 full HP

if resultP1 >= 100:

    print ("\nPlayer 1's new HP value is:\n")
    print (100)
    print ("\nPlayer 1 has full HP!\n")

# Player 1 fainted

elif resultP1 <= 0:

    print ("\nPlayer 1's new HP value is:\n")
    print (0)
    print ("\nPlayer 1 has fainted!\n")

# If resulting value does not meet requirements simply print out resulting HP:

else:

    print ("\nPlayer 1's new HP value is:\n")
    print (resultP1)

# And repeat the same things for player 2:

if resultP2 >= 100:

    print ("\nPlayer 2's new HP value is:\n")
    print (100)
    print ("\nPlayer 2 has full HP!\n")

elif resultP2 <= 0:

    print ("\nPlayer 2's new HP value is:\n")
    print (0)
    print ("\nPlayer 2 has fainted!\n")

else:

    print ("\nPlayer 2's new HP value is:\n")
    print (resultP2)

# End of code, goodbye note:

print ("\nGoodbye World!\n")
