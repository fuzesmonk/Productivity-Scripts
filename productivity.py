import os
import random
import time
import vlc


reward_chances = {
    'DCS': 0.00000001,
    '5 Min Break': 0.5,
    '10 Minutes on Youtube': 0.1,
    '1 Crucible Match on D2': 0.05,
    'Eat snack or roll again' : 0.05,
    '10 Minutes of anything': 0.05,
    '10 Minutes of Turing Complete': 0.05,
    '10 Minutes of Coding or Roll Again': 0.05,
    'Read 5 Pages of a book': 0.1,
    'Two Spins': 0.049999999
}

def spin():
    return random.choices(list(reward_chances.keys()), list(reward_chances.values()))[0]

def main():
    media = vlc.MediaPlayer('bells.wav')
    media.play()
    time.sleep(10)
    spin_result = spin()
    print(spin_result)
    if (spin_result != 'nothing'):
        with open('rewards.txt', 'a') as f:
            f.write(spin_result + '\n')
    if (spin_result == 'Two Spins'):
            spin()
            spin()
    time.sleep(1200)

if __name__ == '__main__':
    while(True):
        main()
