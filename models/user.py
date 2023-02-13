#!/usr/bin/python3
"""Contains User class, which is a subclass of the BaseModel class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user profile. It inherits from the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Call superclass init method to invoke inheritance of its methods."""
        super(User, self).__init__(*args, **kwargs)
