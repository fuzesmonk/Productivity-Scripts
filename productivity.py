import subprocess
import pkg_resources
import sys

needed_packages = 'python-vlc'


def checker(needed_packages):
    required = {needed_packages}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

checker(needed_packages)

import os
import random
import time
import vlc

reward_chances = {
    'DCS': 0.00000001,
    '10 Min Break': 0.5,
    '10 Minutes on Youtube': 0.1,
    '1 Crucible Match on D2': 0.05,
    'Eat snack or roll again': 0.05,
    '10 Minutes of anything': 0.05,
    '10 Minutes of Turing Complete': 0.05,
    '10 Minutes of Coding or Roll Again': 0.05,
    'Read 5 Pages of a book': 0.1,
    'Two Spins': 0.049999999
}


def spin():
    return random.choices(list(reward_chances.keys()), list(reward_chances.values()))[0]

def ready_check():
    done = True
    while done:
        done_check = input("Are you done for the night? Y/N: ")
        if done_check == "Y":
            break
        elif done_check == "N":
            break_check = input("Ready to start next round? Y/N: ")
            if break_check == "Y":
                done = False
            else:
                time.sleep(600)


def main():
    current_time = time.time()
    time.ctime(current_time)
    print("Start Working. Don't stress too much!")
    time.sleep(1200)
    media = vlc.MediaPlayer("C:\Projects\Productivity-Scripts\churchbells.wav")
    media.play()
    time.sleep(10)
    spin_result = spin()
    print(spin_result)
    if spin_result != 'nothing':
        with open('rewards.txt', 'a') as f:
            f.write(spin_result + '\n')
    if spin_result == 'Two Spins':
        spin()
        spin()


if __name__ == '__main__':
    while True:
        main()
#   Check if break is done
        ready_check()


