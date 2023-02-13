#!/usr/bin/python3
"""Contains Review class, which is a subclass of the BaseModel class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review for a place/property. Inherits from BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Call superclass init method to invoke inheritance of its methods."""
        super(Review, self).__init__(*args, **kwargs)
