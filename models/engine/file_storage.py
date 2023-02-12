#!/usr/bin/python3
"""Contains the class for the module's file storage I/O operations."""
import json


class FileStorage:
    """Serializes/deserializes object instances to/from a JSON file."""

    def __init__(self):
        """Set private attributes for new instance."""
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """Returns the private dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Stores obj's attributes in __objects dictionary."""
        my_dict = {}
        for key in obj.to_dict():
            if key != '__class__':
                my_dict[key] = obj.to_dict()[key]
        uuid_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[uuid_key] = my_dict

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        my_json = json.dumps(self.__objects)
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            file.write(my_json)

    def reload(self):
        """Deserializes JSON file (__file_path) to __objects dictionary."""
        try:
            with open(self.__file_path, encoding='UTF-8') as file:
                my_json = file.read()
                if my_json:
                    self.__objects = json.loads(my_json)
                # else:
                #     self.__objects = {}
        except FileNotFoundError:
            pass

    def delete(self, obj):
        """Permanently deletes obj from storage."""

        # Check if an instance of given object's type currently exists
        self.reload()
        models_list = list(map(lambda key: key.split('.')[0],
                               self.__objects.keys()))
        if obj.__class__.__name__ not in set(models_list):
            return

        # Find given object instance and delete it
        obj_id = f'{obj.__class__.__name__}.{obj.id}'
        if obj_id in self.__objects.keys():
            str = self.__objects.pop(obj_id)
            self.save()
            return str
