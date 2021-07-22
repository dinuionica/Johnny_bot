# Copyright 2021 Dinu Ion-Irinel

# imports needed
from subprocess import call
import subprocess

# run the script
def install_applications():
    rc = call("./script.sh", shell=True)
def main():
    install_applications()

main()