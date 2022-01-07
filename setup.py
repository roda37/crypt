from sys import argv
from os import system

def install():
    system('sudo cp crypt /usr/bin')
    system('sudo chmod +x /usr/bin/crypt')

if len(argv)<2:
    print('To install this program execute python sudo setup.py install')

elif argv[1]=='install':
    install()

else:
    print('To install this program execute python sudo setup.py install')