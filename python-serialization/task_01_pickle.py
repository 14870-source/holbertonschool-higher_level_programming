#!/usr/bin/env python3
"""Serialize and deserialize custom objects using pickle."""

import pickle


class CustomObject:
    """Represent a custom Python object."""

    def __init__(self, name, age, is_student):
        """Initialize the object's attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an object from a file."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if not isinstance(obj, cls):
                return None
            return obj
        except (OSError, pickle.PickleError, EOFError, AttributeError,
                ImportError, IndexError, TypeError, ValueError):
            return None
