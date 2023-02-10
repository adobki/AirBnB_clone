#!/usr/bin/python3
"""Command interpreter to issue commands for object management in AirBnb."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter."""

    # Initialize the command line
    intro = 'ALX Software Engineering Command line. ' \
            'Type help or ? to list commands.'
    prompt = '(hbnb) '
    file = None

    # -- Quit the shell
    def do_quit(self):
        """Quit command to exit the program (quit)"""
        self.close()
        quit()

    # -- EOF (End Of File)
    def do_EOF(self):
        """End Of File (EOF)"""
        self.do_quit()

    def close(self):
        """Closes the file in self.file variable if it is open."""
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        """Prevents empty line/blank input from running previous command."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
