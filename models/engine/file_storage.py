#!/usr/bin/python3
"""Contains the class for the module's file storage I/O operations."""
import json
# from uuid import UUID, uuid4


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
        # for key in obj.__dict__:
        for key in obj.to_dict():
            if key != '__class__':
                my_dict[key] = obj.__dict__[key]
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

        # """Sets in __objects the obj with key <obj class name>.id."""
        # """Set attributes for new/deserialized BaseModel instance."""
        # Parse given arguments as attributes of created instance
        # if kwargs:
        #     for key in kwargs:
        #         if key != '__class__':
        #             setattr(self, key, kwargs[key])
        # elif args:
        #     attributes = ('id', 'created_at', 'updated_at')
        #     for index in range(len(args)):
        #         if index == len(attributes):
        #             break
        #         else:
        #             setattr(self, attributes[index], args[index])
        # else:
        #     self.id = None
        #
        # # Validate created_at and set to current time if invalid/null
        # try:
        #     datetime(self.created_at)
        # except Exception:
        #     self.created_at = datetime.now()


if __name__ == '__main__':
    # import cmd
    # print(cmd.Cmd)
    my_dict = {'__class__': 'BaseModel',
               'id': '72111833-90f2-4c97-9d21-a1d146681f7b',
               'created_at': '2022-11-09T09:49:18.111316',
               'updated_at': '2022-11-09T09:49:18.111316'}
    print(f'{my_dict}\n')
    __objects = {}
    obj_dict = my_dict
    # obj_dict = obj.to_dict()
    for key in obj_dict:
        if key != '__class__':
            new_key = '{}.{}'.format(obj_dict['__class__'], key)
            __objects[new_key] = obj_dict[key]
    print(__objects)

    class BaseModel:
        pass

    obj = BaseModel()
    obj.id = '72111833-90f2-4c97-9d21-a1d146681f7b'
    obj.created_at = '2022-11-09T09:49:18.111316'
    obj.updated_at = '2022-11-09T09:49:18.111316'
    print(obj.__dict__)
    __objects = {}
    for key in obj.__dict__:
        new_key = '{}.{}'.format(obj.__class__.__name__, key)
        __objects[new_key] = obj_dict[key]
    print(json.dumps(__objects))
    print(json.loads(json.dumps(__objects)))

    # my_dict = {'__class__': 'BaseModel',
    #            'id': '72111833-90f2-4c97-9d21-a1d146681f7b',
    #            'created_at': '2022-11-09T09:49:18.111316',
    #            'updated_at': '2022-11-09T09:49:18.111316'}
    # dct = FileStorage(**my_dict)
    # print('\n{}'.format(dct))
    # print(dct.to_dict())
    #
    # my_str = ['72111833-90f2-4c97-9d21-a1d146681f7b',
    #           '2022-11-09T09:49:18.111316', '2022-11-09T09:49:18.111316']
    # dct = FileStorage(my_str[0], my_str[1], my_str[2])
    # print('\n{}'.format(dct))
    # print(dct.to_dict())
