#!/usr/bin/python3
"""Contains Amenity class, which is a subclass of the BaseModel class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines an amenity offered at a place. Inherits from BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Call superclass init method to invoke inheritance of its methods."""
        super(Amenity, self).__init__(*args, **kwargs)
