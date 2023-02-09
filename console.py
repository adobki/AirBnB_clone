#!/usr/bin/python3
import cmd, sys
class HBNBCommand(cmd.Cmd):
	"""Initialize the command line"""
	intro = 'ALX Software Engineering Command line'
	prompt= '(hbnb)'

	# -- Quit the shell
	def do_quit(self):
		'Quit command to exit the program'
		self.close()
		quit()

	def close(self):
		if self.file:
			self.file.close()
			self.file = None

if __name__ = "__main__":
	HBNBCommand().cmdloop()