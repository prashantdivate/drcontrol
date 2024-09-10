#!/usr/bin/env python3

from pylibftdi import BitBangDevice

# Commands to turn relays on and off (extended to 8 relays)
relay_on_cmds = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
relay_off_cmds = [0xFE, 0xFD, 0xFB, 0xF7, 0xEF, 0xDF, 0xBF, 0x7F]

# Specify the device id, You can get the FT245RL device id using the below command
# sudo python3 -m pylibftdi.examples.list_devices
bb = BitBangDevice('AQ03BK0Q')
bb.direction = 0xFF  # Set all 8 bits to output (0xFF)

# Function to turn on the relay, rel_num --> relay index (1 to 8)
def relay_on(rel_num, bbobj):
    global relay_on_cmds
    bbobj.port |= relay_on_cmds[rel_num - 1]

# Function to turn off the relay, rel_num --> relay index (1 to 8)
def relay_off(rel_num, bbobj):
    global relay_off_cmds
    bbobj.port &= relay_off_cmds[rel_num - 1]

def init():
    name = "Direction Controller for 8 channel USB relay module"
    version = "1.0"
    date = " 2024-09-10 18:13:01 (Tue, 10 Sep 2024)"
    rev = "1 "
    author = "Prashant Divate [ diwateprashant44@gmail.com ]"

    # ASCII Art
    ascii_art_header = """
     _                     _             _
  __| |_ __ ___ ___  _ __ | |_ _ __ ___ | |
 / _` | '__/ __/ _ \| '_ \| __| '__/ _ \| |
| (_| | | | (_| (_) | | | | |_| | | (_) | |
 \__,_|_|  \___\___/|_| |_|\__|_|  \___/|_|
   """

    ascii_board_art = """
+---------------------------------------------+
|                                             |
|   +--------+               +--------+       |
|   | Relay 1|               | Relay 5|       |
|   +--------+               +--------+       |
|   +--------+               +--------+       |
|   | Relay 2|               | Relay 6|       |
|   +--------+               +--------+       |
|   +--------+               +--------+       |
|   | Relay 3|               | Relay 7|       |
|   +--------+               +--------+       |
|   +--------+               +--------+       |
|   | Relay 4|               | Relay 8|       |
|   +--------+               +--------+       |
|                                             |
|            +-------------------+            |
|            | Relay Driver chip |            |
|            +-------------------+            |
|                                             |
| +-----------------+  +-------------------+  |
| |     DC Input    |  |   USB connector   |  |
| +-----------------+  +-------------------+  |
|                                             |
+---------------------------------------------+
"""

    # Display the initialized values and ASCII art
    print("================================================================================")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("================================================================================\n")
    print(f"Name: {name}")
    print(f"Version: {version}")
    print(f"Build Date: {date}")
    print(f"Revision: {rev}")
    print(f"Author: {author}")
    print(ascii_art_header)
    print("\n")
    print("below is your board layout:")
    print(ascii_board_art)
    print("\n")


# Function to control the relay based on user input
def control_relay():
    while True:
        try:
            # Ask the user which relay they want to control
            relay_num = int(input("Which relay do you want to control? (1-8): "))
            if relay_num < 1 or relay_num > 8:
                print("Please enter a valid relay number between 1 and 8.")
                continue

            # Ask if the user wants to turn the relay on or off
            action = input("Do you want to turn it ON or OFF? (on/off): ").strip().lower()
            if action == 'on':
                relay_on(relay_num, bb)
                print(f"Relay {relay_num} has been turned ON.")
            elif action == 'off':
                relay_off(relay_num, bb)
                print(f"Relay {relay_num} has been turned OFF.")
            else:
                print("Invalid action. Please type 'on' or 'off'.")
                continue

            # Ask if the user wants to continue controlling relays
            continue_control = input("Do you want to control another relay? (yes/no): ").strip().lower()
            if continue_control != 'yes':
                print("Exiting the control script.")
                break

        except ValueError:
            print("Invalid input. Please enter a number for the relay and 'on' or 'off' for the action.")

# main function
init()
control_relay()
