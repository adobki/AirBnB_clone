#!/usr/bin/python3
"""Contains State class, which is a subclass of the BaseModel class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines a location: state. It inherits from the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Call superclass init method to invoke inheritance of its methods."""
        super(State, self).__init__(*args, **kwargs)
