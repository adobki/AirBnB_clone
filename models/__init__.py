#!/usr/bin/python3
"""Module initialisation script."""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
