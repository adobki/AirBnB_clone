#!/usr/bin/python3
"""Contains Place class, which is a subclass of the BaseModel class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a listed place/property. Inherits from BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Call superclass init method to invoke inheritance of its methods."""
        super(Place, self).__init__(*args, **kwargs)
