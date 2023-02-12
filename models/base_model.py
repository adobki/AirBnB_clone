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
            self.created_at = datetime.now()
            if hasattr(self, 'updated_at'):
                delattr(self, 'updated_at')
            storage.new(self)
            return

        # Validate created_at and set to current time if invalid/null
        try:
            self.created_at = datetime.fromisoformat(self.created_at)
        except Exception:
            self.created_at = datetime.now()

        # Validate updated_at if it exists and set to current time if invalid
        if hasattr(self, 'updated_at'):
            try:
                self.updated_at = datetime.fromisoformat(self.updated_at)
            except Exception:
                self.updated_at = datetime.now()

    def __str__(self):
        """Returns a special string when instance is passed to print()."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns dictionary of all keys/values of instance's  __dict__."""
        my_dict = {'__class__': self.__class__.__name__}
        for key in self.__dict__.keys():
            if key == 'created_at' or key == 'updated_at':
                my_dict[key] = self.__dict__[key].isoformat()
            else:
                my_dict[key] = self.__dict__[key]
        return my_dict
