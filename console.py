#!/usr/bin/python3
""" Command interpreter module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program """
        """print("Am quiting this program")"""
        return True

    def do_EOF(self, arg):
        """This func help exit the program. """
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
