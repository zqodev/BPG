import os
import subprocess

from misc.string import ascii_lowercase, ascii_uppercase, ascii_number, ascii_special
from pystyle import Colors, Colorate
from random import choice
from sys import exit, executable


def header() -> str:
    head = """                                                       
                         =+--:...          
                        .**+++++++=:       
                         #-  ...:-=++=:    
                        .#.        .-=+=.  
                        -+            :=+- 
                        *-              -+:
                      :*-                :=
                     =+.                  .
                   .+=                     
                  -#:                      
                .*+                        
               :#-                         
              =#.                          
            -#+.                           
           +%-                             
         :##:                              
        =%+                                                                                    
    """

    return Colorate.Horizontal(Colors.black_to_white, head)


def prefix() -> str:
    return Colors.gray + "[" + Colors.cyan + "»" + Colors.gray + "]" + Colors.dark_gray + " - "


def input_user() -> tuple:
    print(header())

    try:
        status = int(input(prefix() + Colors.white + "1. Generate Password - 2. Quit: "))

        if status == 0:
            return ()
        if status == 2:
            exit(0)

        is_lowercase = bool(int(input(prefix() + Colors.white + "Use lowercase letters? (1: Yes, 0: No): ")))
        is_uppercase = bool(int(input(prefix() + Colors.white + "Use uppercase letters? (1: Yes, 0: No): ")))
        is_numbers = bool(int(input(prefix() + Colors.white + "Use numbers? (1: Yes, 0: No): ")))
        is_specials = bool(int(input(prefix() + Colors.white + "Use special characters? (1: Yes, 0: No): ")))
        length = int(input(prefix() + Colors.white + "Password length: "))
    except ValueError:
        clear()
        return ()

    return status, is_lowercase, is_uppercase, is_numbers, is_specials, length


def generate_password(is_lowercase=True, is_uppercase=True, is_numbers=True, is_specials=True, length=12) -> str:
    characters = ""

    if is_lowercase:
        characters += ascii_lowercase()
    if is_uppercase:
        characters += ascii_uppercase()
    if is_numbers:
        characters += ascii_number()
    if is_specials:
        characters += ascii_special()

    return "".join(choice(characters) for _ in range(length)) if characters else ""


def clear() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def install_dependencies() -> None:
    try:
        import pystyle
    except ModuleNotFoundError:
        try:
            subprocess.check_call([executable, '-m', 'pip', 'install', "pystyle"])
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'installation de la dépendance : {e}")