import os
import beaupy
from beaupy.spinners import *
from pystyle import Colors, Colorate
import time

#pycryptodome
from Crypto.Random import random



def clear():
    os.system("clear||cls")


def banner():
    banner = """

            ██████╗ ███████╗███╗   ██╗████████╗███████╗██████╗
           ██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
           ██║  ███╗█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝
           ██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
           ╚██████╔╝███████╗██║ ╚████║   ██║   ███████╗██║  ██║
            ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝


      Made by Ori#6338 | @therealOri_ | https://github.com/therealOri
    """
    colored_banner = Colorate.Horizontal(Colors.purple_to_blue, banner, 1)
    return colored_banner




def main():
    while True:
        clear()
        main_options = ["Regular Dice?", "D&D dice set?", "Exit?"]
        print(f'{banner()}\n\nWhat would you like to do?\n-----------------------------------------------------------\n')
        main_option = beaupy.select(main_options, cursor_style="#ffa533")

        if not main_option:
            clear()
            exit("Keyboard Interuption Detected!\nGoodbye <3")


        if main_options[0] in main_option:
            # regular dice menu
            clear()
            while True:
                reg_dice_options = ["1 Die?", "2 Dice?", "3 Dice?", "Custom?", "Back?"]
                print(f'{banner()}\n\nHow many dice would you like to roll?\n-----------------------------------------------------------\n')
                reg_dice_option = beaupy.select(reg_dice_options, cursor_style="#ffa533")

                if not reg_dice_option:
                    clear()
                    break

                if reg_dice_options[0] in reg_dice_option:
                    spinner = Spinner(ARC, "User has rolled 1 die...")
                    spinner.start()
                    time.sleep(2)
                    die1 = random.randint(1, 6)
                    spinner.stop()
                    input(f'The die has landed on: [{die1}]\n\nPress "enter" to continue...')
                    clear()
                    continue


                if reg_dice_options[1] in reg_dice_option:
                    spinner = Spinner(ARC, "User has rolled 2 dice...")
                    spinner.start()
                    time.sleep(2)
                    die1 = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    spinner.stop()
                    input(f'The dice have landed on: [{die1}]  [{die2}]\n\nPress "enter" to continue...')
                    clear()
                    continue

                if reg_dice_options[2] in reg_dice_option:
                    spinner = Spinner(ARC, "User has rolled 3 dice...")
                    spinner.start()
                    time.sleep(2)
                    die1 = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    die3 = random.randint(1, 6)
                    spinner.stop()
                    input(f'The dice have landed on: [{die1}]  [{die2}]  [{die3}]\n\nPress "enter" to continue...')
                    clear()
                    continue

                if reg_dice_options[3] in reg_dice_option:
                    dice_list = []
                    clear()
                    while True:
                        try:
                            dice = int(beaupy.prompt("How many dice do you want to roll?"))
                        except:
                            input('Please choose a number/integer.\n\nPress "enter" to try again...')
                            clear()
                            continue

                        if type(dice) == int:
                            break

                    if dice == 1:
                        msg = f"User has rolled 1 die..."
                    else:
                        msg = f"User has rolled {dice} dice..."

                    spinner = Spinner(ARC, msg)
                    spinner.start()
                    count = 0
                    while count < dice:
                        roll = random.randint(1, 6)
                        dice_list.append(roll)
                        count +=1
                    time.sleep(2)
                    spinner.stop()

                    if dice == 1:
                        input_msg = f'The die has landed on: {dice_list[0]}\n\nPress "enter" to continue...'
                    else:
                        input_msg = f'The set of "{dice}" dice have rolled: {dice_list}\n\nPress "enter" to continue...'

                    input(input_msg)
                    clear()
                    continue


                if reg_dice_options[4] in reg_dice_option:
                    clear()
                    break


        if main_options[1] in main_option:
            # D&D dice menu
            clear()
            while True:
                dnd_dice_options = ["Roll d4?", "Roll d6?", "Roll d8?", "Roll d10?", "Roll d12?", "Roll d20?", "Custom?", "Back?"]
                print(f'{banner()}\n\nWhat dice would you like to roll?\n-----------------------------------------------------------\n')
                dnd_dice_option = beaupy.select(dnd_dice_options, cursor_style="#ffa533")

                if not dnd_dice_option:
                    clear()
                    break

                if dnd_dice_options[0] in dnd_dice_option:
                    spinner = Spinner(ARC, "User has rolled a d4 die...")
                    spinner.start()
                    time.sleep(2)
                    d4 = random.randint(1, 4)
                    spinner.stop()
                    input(f'The d4 die has landed on: [{d4}]\n\nPress "enter" to continue...')
                    clear()
                    continue

                if dnd_dice_options[1] in dnd_dice_option:
                    spinner = Spinner(ARC, "User has rolled a d6 die...")
                    spinner.start()
                    time.sleep(2)
                    d6 = random.randint(1, 6)
                    spinner.stop()
                    input(f'The d6 die has landed on: [{d6}]\n\nPress "enter" to continue...')
                    clear()
                    continue

                if dnd_dice_options[2] in dnd_dice_option:
                    spinner = Spinner(ARC, "User has rolled a d8 die...")
                    spinner.start()
                    time.sleep(2)
                    d8 = random.randint(1, 8)
                    spinner.stop()
                    input(f'The d4 die has landed on: [{d8}]\n\nPress "enter" to continue...')
                    clear()
                    continue

                if dnd_dice_options[3] in dnd_dice_option:
                    if beaupy.confirm("Want to make a 'percentile' role as well?"):
                        d10_00 = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90"]
                        spinner = Spinner(ARC, "User has rolled a d10 die and a percentile die...")
                        spinner.start()
                        time.sleep(2)
                        d10 = random.randint(1, 10)
                        d10p = random.choice(d10_00)
                        spinner.stop()
                        input(f'The d10 die has landed on: [{d10}]\nThe percentile roll is: [{d10p}]\n\nPress "enter" to continue...')
                        clear()
                        continue
                    else:
                        spinner = Spinner(ARC, "User has rolled a d10 die...")
                        spinner.start()
                        time.sleep(2)
                        d10 = random.randint(1, 10)
                        spinner.stop()
                        input(f'The d10 die has landed on: [{d10}]\n\nPress "enter" to continue...')
                        clear()
                        continue

                if dnd_dice_options[4] in dnd_dice_option:
                    spinner = Spinner(ARC, "User has rolled a d12 die...")
                    spinner.start()
                    time.sleep(2)
                    d12 = random.randint(1, 12)
                    spinner.stop()
                    input(f'The d12 die has landed on: [{d12}]\n\nPress "enter" to continue...')
                    clear()
                    continue

                if dnd_dice_options[5] in dnd_dice_option:
                    spinner = Spinner(ARC, "User has rolled a d20 die...")
                    spinner.start()
                    time.sleep(2)
                    d20 = random.randint(1, 20)
                    spinner.stop()
                    input(f'The d20 die has landed on: [{d20}]\n\nPress "enter" to continue...')
                    clear()
                    continue

                if dnd_dice_options[6] in dnd_dice_option:
                    clear()
                    dice_options = ["d4", "d6", "d8", "d10", "d10p", "d12", "d20"]
                    print(f"Dice options: {dice_options} | (d10p = percentile die)")
                    dice_input = beaupy.prompt("Enter dice in format 'XdY' separated by commas (e.g. '3d6, 2d4, 1d20'):")
                    dice_sets = dice_input.split(", ")

                    spinner = Spinner(ARC, "Rolling dice...")
                    spinner.start()
                    time.sleep(2)

                    # Roll each set of dice and store the results in a list
                    all_results = []
                    for dice_set in dice_sets:
                        if "d10p" in dice_set:
                            d10_00 = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90"]
                            d10p = random.choice(d10_00)
                            results = [int(d10p)]
                        else:
                            num_dice, dice_type = dice_set.split("d")
                            results = [random.randint(1, int(dice_type)) for i in range(int(num_dice))]

                        all_results.append(results)

                    spinner.stop()
                    clear()
                    print("Dice Results:\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    for i, results in enumerate(all_results):
                        print(f"{dice_sets[i]} has rolled: {results}\n")
                    input("Press enter to continue...")
                    clear()
                    continue




                if dnd_dice_options[7] in dnd_dice_option:
                    clear()
                    break





        if main_options[2] in main_option:
            clear()
            exit("Goodbye! <3")






if __name__ == '__main__':
    clear()
    main()
