#!/usr/bin/python3
import cmd, sys
class HBNBCommand(cmd.Cmd):
	"""Initialize the command line"""
	intro = 'ALX Software Engineering Command line. Type help or ? to list commands.'
	prompt= '(hbnb)'
	file = None
	
	# -- Quit the shell
	def do_quit(self, arg):
		'Quit command to exit the program(quit)'
		self.close()
		quit()

	# -- EOF (End Of File)
	def do_EOF(self, arg):
		'End Of File (EOF)'
		EOF()

	def close(self):
		if self.file:
			self.file.close()
			self.file = None

if __name__ == "__main__":
	HBNBCommand().cmdloop()