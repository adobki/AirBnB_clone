#!/usr/bin/python3
"""Contains City class, which is a subclass of the BaseModel class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a location: city in a state. Inherits from BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Call superclass init method to invoke inheritance of its methods."""
        super(City, self).__init__(*args, **kwargs)
