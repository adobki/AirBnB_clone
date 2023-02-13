#!/usr/bin/python3
"""Command interpreter to issue commands for object management in AirBnb."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter."""

    # Initialize the command line
    intro = 'ALX SE AirBnB Clone. Type help or ? to list commands.'
    prompt = '(hbnb) '
    file = None
    models_list = ['BaseModel', 'User', 'Place', 'State',
                   'City', 'Amenity', 'Review']

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
            return

        # Create instance according to model/object class
        if model == 'BaseModel':
            obj = BaseModel()
        elif model == 'User':
            obj = User()
        elif model == 'Place':
            obj = Place()
        elif model == 'State':
            obj = State()
        elif model == 'City':
            obj = City()
        elif model == 'Amenity':
            obj = Amenity()
        elif model == 'Review':
            obj = Review()
        else:
            print("** class doesn't exist **")
            return

        # Save object, then print its id.
        obj.save()
        print(obj.id)

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
                if obj_class == 'User':
                    print(User(**obj))
                elif obj_class == 'Place':
                    print(Place(**obj))
                elif obj_class == 'State':
                    print(State(**obj))
                elif obj_class == 'City':
                    print(City(**obj))
                elif obj_class == 'Amenity':
                    print(Amenity(**obj))
                elif obj_class == 'Review':
                    print(Review(**obj))
                else:
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
            if not obj:
                print('** no instance found **')
            else:
                if obj_class == 'User':
                    storage.delete(User(**obj))
                elif obj_class == 'Place':
                    storage.delete(Place(**obj))
                elif obj_class == 'State':
                    storage.delete(State(**obj))
                elif obj_class == 'City':
                    storage.delete(City(**obj))
                elif obj_class == 'Amenity':
                    storage.delete(Amenity(**obj))
                elif obj_class == 'Review':
                    storage.delete(Review(**obj))
                else:
                    storage.delete(BaseModel(**obj))

    def do_all(self, args):
        """Prints string representation of all available instances. If class \
        name is given, only the instances for that class are printed."""

        # Validate model/class in args if class name is given
        if args and args not in self.models_list:
            print("** class doesn't exist **")
            return

        # Get list of all available model instances/objects
        # objs = list(map(lambda obj: obj, storage.all().values()))
        saved_models = storage.all()
        if not saved_models:
            return

        # Print list of all objects or only the given one
        for key in saved_models.keys():
            obj_class = key.split('.')[0]
            obj = saved_models[key]
            if obj_class == 'BaseModel':
                print(BaseModel(**obj))
            elif obj_class == 'User':
                print(User(**obj))
            elif obj_class == 'Place':
                print(Place(**obj))
            elif obj_class == 'State':
                print(State(**obj))
            elif obj_class == 'City':
                print(City(**obj))
            elif obj_class == 'Amenity':
                print(Amenity(**obj))
            elif obj_class == 'Review':
                print(Review(**obj))
            else:
                print(obj)

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
        if obj_class == 'BaseModel':
            obj = BaseModel(**obj)
        elif obj_class == 'User':
            obj = User(**obj)
        elif obj_class == 'Place':
            obj = Place(**obj)
        elif obj_class == 'State':
            obj = State(**obj)
        elif obj_class == 'City':
            obj = City(**obj)
        elif obj_class == 'Amenity':
            obj = Amenity(**obj)
        elif obj_class == 'Review':
            obj = Review(**obj)
        setattr(obj, obj_attr, obj_val)
        obj.save()

    def help_update(self):
        """Pretty prints help text for all command."""
        print(self.do_update.__doc__.replace('        ', ''))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
