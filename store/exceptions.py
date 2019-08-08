"""
store exceptions classes
"""


class MystoreError(Exception):
    """
    Creating user which already exist.
    """

    def __init__(self, *args, **kwargs):
        super(MystoreError, self).__init__(*args, **kwargs)
