import time
import subprocess
import pkg_resources
import sys

needed_packages = 'python-vlc'

#Checking if packages are installed
def checker(needed_packages):
    required = {needed_packages}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
checker(needed_packages)

import vlc
def main():
    done = True
    while(done):
        ready_check = input('Ready [Y/N]? ')
        if ready_check == 'N':
            break
        if ready_check == 'Y':
            def checkin_time(main):
                #       Main Code
                #       Check-in Time
                check_in_time = int(input('Enter Time in minutes before check-in: '))
                convert_sec = check_in_time * 60
                time.sleep(convert_sec)
                vlc.MediaPlayer("""Find Chime""")
            checkin_time(main)
            cont_work = input('Keep Working?[Y/N]: ')
            cont_work = ord(cont_work)
            if cont_work == ascii('Y'):
                







        else:
            print('Format Error')
            break

