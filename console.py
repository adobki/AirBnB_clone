#!/usr/bin/python3
"""Command interpreter to issue commands for object management in AirBnb."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter."""

    # Initialize the command line
    intro = 'ALX SE AirBnB Clone. Type help or ? to list commands.'
    prompt = '(hbnb) '
    file = None
    models_list = ['BaseModel']

    # -- Quit the shell
    def do_quit(self, arg):
        """Quit command to exit the program. Same as EOF"""
        self.close()
        quit()

    # -- EOF (End Of File)
    def do_EOF(self, arg):
        """End Of File (EOF). Same as quit"""
        self.do_quit(None)

    def close(self):
        """Closes the file in self.file variable if it is open."""
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        """Prevents empty line/blank input from running previous command."""
        pass

    def do_create(self, model):
        """Creates instance of given model class, saves it, prints its id."""
        if not model:
            print('** class name missing **')
        elif model == 'BaseModel':
            obj = BaseModel()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def _get_obj_instances(self, model, id=None, get_all=False):
        """Helper function for retrieving all instances, or by class and id.
        model must be a defined class name in the models package."""

        # Get list of all available objects or only the given one
        saved_models = storage.all()
        obj = None
        for key in saved_models.keys():
            name = key.split('.')[0]
            if name == model:
                if not get_all:
                    if saved_models[key]['id'] == id:
                        obj = saved_models[key]
                        return obj
                else:
                    obj = [] if not obj else obj
                    obj.append(saved_models[key])
        return obj

    def do_show(self, args):
        """Prints the string representation (__str__) of an instance based \
        on given class name and id."""

        # Validate model/class in args
        if not args:
            print('** class name missing **')
            return
        elif args.split()[0] not in self.models_list:
            print("** class doesn't exist **")
            return

        # Validate id in args
        if len(args.split()) < 2:
            print('** instance id missing **')
            return
        else:
            # Check if id is available as an instance of given class
            obj_class = args.split()[0]
            obj_id = args.split()[1]
            obj = self._get_obj_instances(obj_class, obj_id)
            if obj:
                # noinspection PyArgumentList
                print(BaseModel(**obj))
            else:
                print('** no instance found **')

    def help_show(self):
        """Pretty prints help text for show command."""
        print(self.do_show.__doc__.replace('        ', ''))

    def do_destroy(self, args):
        """Permanently deletes an instance based on given class name and id."""

        # Validate model/class in args
        if not args:
            print('** class name missing **')
            return
        elif args.split()[0] not in self.models_list:
            print("** class doesn't exist **")
            return

        # Validate id in args
        if len(args.split()) < 2:
            print('** instance id missing **')
            return
        else:
            # Check if id is available as an instance of given class
            obj_class = args.split()[0]
            obj_id = args.split()[1]
            obj = self._get_obj_instances(obj_class, obj_id)
            if not obj or not storage.delete(BaseModel(**obj)):
                print('** no instance found **')

    def do_all(self, args):
        """Prints string representation of all available instances. If class \
        name is given, only the instances for that class are printed."""

        # Validate model/class in args if class name is given
        if args and args not in self.models_list:
            print("** class doesn't exist **")
            return

        # Get list of all available model instances/objects
        objs = list(map(lambda obj: obj, storage.all().values()))
        if not objs:
            return

        # Print list of all objects or only the given one
        for obj in objs:
            my_str = BaseModel(**obj).__str__()
            obj_class = my_str.split()[0][1:-1]
            if args and obj_class == args:
                print(my_str)
            else:
                print(my_str)

    def help_all(self):
        """Pretty prints help text for all command."""
        print(self.do_all.__doc__.replace('        ', ''))

    def do_update(self, args):
        """Updates an instance based on the class name \
        and id by adding or updating its attribute."""

        # Validate given model/class name
        if not args:
            print('** class name missing **')
            return
        elif args.split()[0] not in self.models_list:
            print("** class doesn't exist **")
            return

        # Validate id in args
        if len(args.split()) < 2:
            print('** instance id missing **')
            return
        # Check if id is available as an instance of given class
        obj_class = args.split()[0]
        obj_id = args.split()[1]
        obj = self._get_obj_instances(obj_class, obj_id)
        if not obj:
            print('** no instance found **')
            return

        # Validate attribute in args
        if len(args.split()) < 3:
            print('** attribute name missing **')
            return
        obj_attr = args.split()[2]
        bad_attrs = ['id', 'created_at', 'updated_at']
        if obj_attr in bad_attrs:
            print('No!')
            return

        # Validate value in args
        if len(args.split()) < 4:
            print('** value missing **')
            return
        obj_val = args.split()[3]

        # import a library and use it to cast val to the attribute type
        from ast import literal_eval
        try:
            obj_val = literal_eval(obj_val)
        except Exception:
            pass

        # Update or add attribute value in instance
        obj = BaseModel(**obj)
        setattr(obj, obj_attr, obj_val)
        obj.save()

    def help_update(self):
        """Pretty prints help text for all command."""
        print(self.do_update.__doc__.replace('        ', ''))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
