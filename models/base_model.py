#!/usr/bin/python3
"""Contains the base class for the module."""
from datetime import datetime
from uuid import UUID, uuid4
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Set attributes for new/deserialized BaseModel instance."""

        # Parse given arguments as attributes of created instance
        if kwargs:
            for key in kwargs:
                if key != '__class__':
                    setattr(self, key, kwargs[key])
        elif args:
            attributes = ('id', 'created_at', 'updated_at')
            for index in range(len(args)):
                if index == len(attributes):
                    break
                else:
                    setattr(self, attributes[index], args[index])
        else:
            self.id = None

        # Validate id and create attributes as new instance if invalid/null id
        try:
            UUID(self.id)
        except Exception:
            self.id = str(uuid4())
            self.created_at = datetime.now().isoformat()
            if hasattr(self, 'updated_at'):
                delattr(self, 'updated_at')
            storage.new(self)
            return

        # Validate created_at and set to current time if invalid/null
        try:
            datetime.fromisoformat(self.created_at)
        except Exception:
            self.created_at = datetime.now().isoformat()

        # Validate updated_at if it exists and set to current time if invalid
        if hasattr(self, 'updated_at'):
            try:
                datetime.fromisoformat(self.updated_at)
            except Exception:
                self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """Returns a special string when instance is passed to print()."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates updated_at attribute with the current datetime."""
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """Returns dictionary of all keys/values of instance's  __dict__."""
        my_dict = {'__class__': self.__class__.__name__}
        for key in self.__dict__.keys():
            my_dict[key] = self.__dict__[key]
        return my_dict


if __name__ == '__main__':
    key = BaseModel(12, 9, 88)
    print(key)
    # tme = datetime.now().isoformat()
    tme = '1900-12-12T12:12:12.120000'
    one = BaseModel('df0fdd3a-3095-43a8-a5c7-bf4bac7c5e01', tme, tme)
    print(one)
    null = BaseModel()
    print(null)
    bad = BaseModel(created_at=2023)
    print('\n{}'.format(bad))

    null.save()
    print('\n{}'.format(null))
    my_model_json = null.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                       my_model_json[key]))

    my_dict = {'__class__': 'BaseModel',
               'id': '72111833-90f2-4c97-9d21-a1d146681f7b',
               'created_at': '2022-11-09T09:49:18.111316',
               'updated_at': '2022-11-09T09:49:18.111316'}
    dct = BaseModel(**my_dict)
    print('\n{}'.format(dct))
    print(dct.to_dict())

    my_str = ['72111833-90f2-4c97-9d21-a1d146681f7b',
              '2022-11-09T09:49:18.111316', '2022-11-09T09:49:18.111316']
    dct = BaseModel(my_str[0], my_str[1], my_str[2])
    print('\n{}'.format(dct))
    print(dct.to_dict())
