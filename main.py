from misc.util import input_user, generate_password, clear, prefix, install_dependencies
from pystyle import Colors, Colorate

install_dependencies()


class BPS:
    def __init__(self, choices: tuple):
        self.password = generate_password(choices[1], choices[2], choices[3], choices[4], choices[5])
        self.show()

    def show(self):
        print(Colorate.Horizontal(Colors.cyan_to_green, "[✔] - Password: " + self.password))


is_generating = True

while is_generating:
    clear()
    choice = input_user()

    if len(choice) > 5:
        match choice[0]:
            case 1:
                client = BPS(choice)

                if is_generating:
                    input("\n" + prefix() + Colors.white + "Press Enter to continue...")
            case _:
                clear()
