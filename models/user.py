#!/usr/bin/python3
"""Contains User class, which is a subclass of the BaseModel class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user profile. It inherits from the BaseModel class."""

    # Set default class attributes
    email = ''
    password = ''
    first_name = ''
    last_name = ''
